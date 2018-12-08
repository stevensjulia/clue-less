from clueless.game import Game
from utils.display import Display

if __name__ == "__main__":
    current_game = Game()

    # add players to game
    current_game.add_player("Roxanne", "Mr. Green")
    current_game.add_player("Julie", "Mrs. Peacock")

    # initialize the game
    current_game.initialize_game()

    weapons = current_game.get_cards().get_weapons()
    characters = current_game.get_cards().get_characters()
    rooms = current_game.get_cards().get_rooms()

    for weapon in weapons:
        print(weapon.card_type + " : " + weapon.value)
    for character in characters:
        print(character.card_type + " : " + character.value)
    for room in rooms:
        print(room.card_type + " : " + room.value)

    players = current_game.get_players()

    for player in players:
        print(player.name + " : " + player.selected_character)

    Display.display_board(current_game.board)

    current_game.terminate_game()

