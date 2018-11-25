from notepad import Notepad
from game import Game


class Player:

    name = ""
    selected_character = None
    color = None
    game_order = 0
    current_location = None
    active = False
    notepad = None
    cards = []

    def __init__(self, name, selected_character, color, order, location):
        self.name = name
        self.selected_character = selected_character
        self.color = color
        self.notepad = Notepad()
        self.game_order = order
        self.current_location = location
        self.active = True

    def make_move(self):
        pass

    def make_suggestion(self):
        pass

    def view_cards(self):
        return self.cards

    def annotate_notepad(self, card):
        if card.getType() == 'character':
            self.notepad.remove_character(card)
        elif card.getType() == 'weapon':
            self.notepad.remove_weapon(card)
        elif card.getType() == 'room':
            self.notepad.remove_room(card)

    def get_player_number(self):
        return self.game_order

    def get_player_color(self):
        return self.color

    def get_player_location(self):
        return self.current_location

    def update_player_location(self, space_id):
        self.current_location = Game.get_space_by_id(space_id)

    def deactivate_player(self):
        self.active = False
