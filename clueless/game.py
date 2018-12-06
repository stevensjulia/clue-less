from player import Player
from deck import Deck
from casefile import CaseFile
from board import GameBoard


class Game:
    players = []
    board = None
    case_file = None
    deck = None

    character_color_mapping = {
        'Miss Scarlet': 'red',
        'Mrs. Peacock': 'blue',
        'Colonel Mustard': 'yellow',
        'Professor Plum': 'purple',
        'Mrs. White': 'white',
        'Mr. Green': 'green',
    }

    # THESE ARE PLACEHOLDER SPACE IDS
    character_starting_location = {
        'Miss Scarlet': 0,
        'Mrs. Peacock': 1,
        'Colonel Mustard': 2,
        'Professor Plum': 3,
        'Mrs. White': 4,
        'Mr. Green': 5,
    }

    def __init__(self):
        __instance = self
        self.deck = Deck()
        self.board = GameBoard()

    def add_player(self, player_name, character):
        player_num = len(self.players)
        initial_location = self.character_starting_location[character]
        color = self.character_color_mapping[character]

        new_player = Player(self.deck, player_name, selected_character=character, color=color,
                            order=player_num, location=initial_location)
        self.players.append(new_player)

    def initialize_game(self):
        num_players = len(self.players)
        if num_players != 0:
            solution, player_cards = self.deck.initialize_game(num_players)
            character, weapon, room = solution
            self.case_file = CaseFile(character, weapon, room)
        else:
            raise Exception("There are no players in your game! Add players before initializing game.")

    def terminate_game(self):
        self.players = []
        self.board = None
        self.case_file = None
        self.deck = None

    def get_space_by_id(self, space_id):
        return self.board.get_space(space_id)

    def check_solution(self, character, weapon, room):
        return self.case_file.check_solution(character, weapon, room)

    def get_players(self):
        return self.players

    def get_cards(self):
        return self.deck
