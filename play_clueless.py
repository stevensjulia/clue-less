from clueless.game import Game
from utils.display import Display

if __name__ == "__main__":
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
