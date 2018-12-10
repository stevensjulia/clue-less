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
        self.transport.write(message.encode())

        if 'terminate_game' in message:
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



