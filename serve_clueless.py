from clueless.game import Game
from utils.display import Display
import asyncio
import json


class internal:
    current_players = {}
    current_game = None
    num_players = 0
    expected_players = 0
    remaining_characters = ["Miss Scarlet", "Mrs White", "Mrs Peacock", "Col Mustard", "Prof Plum", "Mr Green"]

    @staticmethod
    def handle_input(message, transport, peername):
        host, port = peername
        actions = json.loads(message)

        if 'join_game' in actions:
            data = actions.get('join_game').split(',')
            player_name = data[0]
            character = data[1]
            if internal.num_players == 0:
                expected_players = data[2]
            internal.current_players[host] = {"name": player_name, "character": character, "transport": transport}

            if internal.current_game is None:
                internal.current_game = Game()
                internal.expected_players = int(expected_players)

            # add player to game
            internal.current_game.add_player(player_name, character)
            internal.num_players += 1
            internal.remaining_characters.remove(character)

            players_left_to_join = str(internal.expected_players - internal.num_players)

            if internal.num_players == internal.expected_players:
                ServerProtocol.message_all_players('Everyone has joined! Lets begin.')
                internal.begin_game()
            else:
                ServerProtocol.message_all_players(
                    '{0} just joined the game as {1}. Waiting for {2} more player(s) to join!'.format(
                        player_name, character, players_left_to_join))

        if 'terminate_game' in actions:
            ServerProtocol.message_all_players('Please play again!')
            internal.current_players = {}
            internal.current_game = None
            internal.num_players = 0
            internal.expected_players = 0

        if 'enter_game' in actions:
            ServerProtocol.message_current_player(
                transport, "Please choose from the remaining characters: " + str(internal.remaining_characters))


    @staticmethod
    def begin_game():
        # initialize the game
        internal.current_game.initialize_game()
        ServerProtocol.message_all_players(Display.display_board(internal.current_game.board))

class ServerProtocol(asyncio.Protocol):

    def connection_made(self, transport):
        peername = transport.get_extra_info('peername')
        print('Connection from {}'.format(peername))
        self.transport = transport
        self.peername = peername

    def data_received(self, data):
        message = data.decode()
        print('Data received: {!r}'.format(message))

        internal.handle_input(message, self.transport, self.peername)

        if 'terminate_game' in message:
            print('Close the client socket')
            self.transport.close()

    @staticmethod
    def message_all_players(message):
        for k in internal.current_players:
            record = internal.current_players.get(k)
            curr_transport = record.get("transport")
            curr_transport.write(message.encode())

    @staticmethod
    def message_current_player(curr_transport, message):
        curr_transport.write(message.encode())


async def main():
    # Get a reference to the event loop as we plan to use
    # low-level APIs.
    loop = asyncio.get_running_loop()

    server = await loop.create_server(
        lambda: ServerProtocol(),
        '172.31.15.89', 8888)

    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())



