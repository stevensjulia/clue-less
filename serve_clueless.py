from clueless.game import Game
from utils.display import Display
import asyncio


class EchoServerProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        peername = transport.get_extra_info('peername')
        print('Connection from {}'.format(peername))
        self.transport = transport

    def data_received(self, data):
        message = data.decode()
        print('Data received: {!r}'.format(message))

        print('Send: {!r}'.format(message))
        self.transport.write(data)

        print('Close the client socket')
        self.transport.close()


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


async def main():
    # Get a reference to the event loop as we plan to use
    # low-level APIs.
    loop = asyncio.get_running_loop()

    server = await loop.create_server(
        lambda: EchoServerProtocol(),
        '54.183.100.229', 8888)

    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())



