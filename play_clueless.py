from clueless.game import Game
from utils.display import Display
import asyncio


def play_game():
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


async def main():
    # Get a reference to the event loop as we plan to use
    # low-level APIs.
    loop = asyncio.get_running_loop()

    on_con_lost = loop.create_future()
    message = 'Hello World!'

    transport, protocol = await loop.create_connection(
        lambda: ClientProtocol(message, on_con_lost, loop),
        '54.183.147.155', 8888)

    # Wait until the protocol signals that the connection
    # is lost and close the transport.
    try:
        await on_con_lost
    finally:
        transport.close()

if __name__ == "__main__":
    asyncio.run(main())
