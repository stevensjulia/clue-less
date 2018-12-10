from clueless.game import Game
from utils.display import Display
import asyncio
import socket


def begin_game():

    while True:
        try:
            num_players = input("\nHow many players will be joining the game?\n")
            name = input("\nPlease enter your name:\n")
            char = input("\nPlease choose a character from the following: Miss Scarlet, Mrs White, Mrs Peacock, "
                         "Col Mustard, Prof Plum, Mr Green \n")

            vars = name + "," + char + "," + num_players

            break

        except ValueError:
            print("\nSorry, I didn't understand that.")
            # better try again... Return to the start of the loop
            continue

    print("\nThanks for starting a game!\n")

    return vars

    #Display.display_board(current_game.board)


class ClientProtocol(asyncio.Protocol):
    def __init__(self, message, on_con_lost, loop):
        self.message = message
        self.loop = loop
        self.on_con_lost = on_con_lost

    def connection_made(self, transport):
        transport.write(self.message.encode())
        print('Data sent: {!r}'.format(self.message))

    def data_received(self, data):
        print('Data received: {!r}'.format(data.decode()))

    def connection_lost(self, exc):
        print('The server closed the connection')
        self.on_con_lost.set_result(True)


async def main(vars):
    # Get a reference to the event loop as we plan to use
    # low-level APIs.
    loop = asyncio.get_running_loop()

    on_con_lost = loop.create_future()

    transport, protocol = await loop.create_connection(
        lambda: ClientProtocol(vars, on_con_lost, loop),
        '54.183.147.155', 8888)

    # Wait until the protocol signals that the connection
    # is lost and close the transport.
    try:
        await on_con_lost
    finally:
        transport.close()

if __name__ == "__main__":
    vars = begin_game()

    asyncio.run(main(vars))

