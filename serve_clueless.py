from clueless.game import Game
from utils.display import Display
import asyncio
import json


class internal:
    current_players = {}
    current_game = None
    num_players = 0
    expected_players = 0

    def handle_input(message, peername):
        host, port = peername
        actions = json.loads(message)

        if 'join_game' in actions:
            data = actions.get('join_game').split(',')
            player_name = data[0]
            character = data[1]
            if internal.num_players == 0:
                expected_players = data[2]
            internal.current_players[host] = (player_name, character)

            if internal.current_game is None:
                internal.current_game = Game()
                internal.expected_players = expected_players

            # add player to game
            internal.current_game.add_player(player_name, character)
            internal.num_players += 1

            if internal.num_players == internal.expected_players:
                return 'Everyone has joined! Lets begin.'
            else:
                return 'Thanks for joining!'

        if 'terminate_game' in actions:
            internal.current_players = {}
            internal.current_game = None
            internal.num_players = 0
            internal.expected_players = 0

            return 'Please play again!'



    def play_server():
        current_game = Game()
        num_players = 0

        while True:
            try:
                # Note: Python 2.x users should use raw_input, the equivalent of 3.x's input
                name = input("\nPlease enter your name:\n")
                char = input("\nPlease choose a character from the following: Miss Scarlet, Mrs White, Mrs Peacock, "
                             "Col Mustard, Prof Plum, Mr Green \n")

                # add players to game
                current_game.add_player(name, char)
                num_players += 1

                if num_players != 6:
                    again = input("\nWould you like to add another character? Please enter 'yes' or 'no'.\n")

                    if again == 'yes':
                        continue
                    else:
                        break
                else:
                    break

            except ValueError:
                print("Sorry, I didn't understand that.")
                # better try again... Return to the start of the loop
                continue

        print("Welcome to the game!\n")

        # initialize the game
        current_game.initialize_game()

        weapons = current_game.get_cards().get_weapons()
        characters = current_game.get_cards().get_characters()
        rooms = current_game.get_cards().get_rooms()

        players = current_game.get_players()

        for player in players:
            print(player.name + " : " + player.selected_character)

        Display.display_board(current_game.board)

        current_game.terminate_game()


class ServerProtocol(asyncio.Protocol):

    def connection_made(self, transport):
        peername = transport.get_extra_info('peername')
        print('Connection from {}'.format(peername))
        self.transport = transport
        self.peername = peername

    def data_received(self, data):
        message = data.decode()
        print('Data received: {!r}'.format(message))

        message = internal.handle_input(message, self.peername)

        print('Send: {!r}'.format(message))
        self.transport.write(data)

        if 'terminate_game' is in message:
            print('Close the client socket')
            self.transport.close()


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



