from player import Player
from deck import Deck
from casefile import CaseFile
from board import GameBoard

#GAME CONSTANTS
SUSPECT= 'Suspect'

SCARLET= 'Miss Scarlet'
WHITE= 'Mrs White'
PEACOCK= 'Mrs Peacock'
MUSTARD= 'Colonel Mustard'
PLUM= 'Professor Plum'
GREEN= 'Mr Green'

SUSPECTS = [
    MUSTARD,
    SCARLET,
    PLUM,
    GREEN,
    WHITE,
    PEACOCK
    }
WEAPON = 'Weapon'

ROPE= 'Rope'
LEAD_PIPE= 'Lead Pipe'
KNIFE= 'Knife'
WRENCH= 'Wrench'
CANDLESTICK= 'Candlestick'
REVOLVER= 'Revolver'
    
WEAPONS= [
    ROPE,
    LEAD_PIPE,
    KNIFE,
    WRENCH,
    CANDLESTICK,
    REVOLVER
]

ROOM= 'Room'

BALLROOM= 'Ballroom'
BILLIARD_ROOM= 'Billiard room'
CONSERVATORY= 'Conservatory'
DINING_ROOM= 'Dining room'
HALL= 'Hall'
KITCHEN = 'Kitchen'
LIBRARY= 'Library'
LOUNGE= 'Lounge'
STUDY= 'Study'

Rooms = [
    BALLROOM, 
    BILLIARD_ROOM,
    CONSERVATORY,
    DINING_ROOM,
    HALL,
    KITCHEN,
    LIBRARY,
    LOUNGE,
    STUDY
]
STUDY_LIBRARY = 'Study to library hallway'
STUDY_HALL ='studyhall hallway'
HALL_BILLIARD='hall to billiard hallway'
HALL_LOUNGE='hall to lounge hallway'
LOUNGE_DINING='lounge to dining hallway'
LIBRARY_CONSERVATORY='library to conservatory hallway'
LIBRARY_BILLIARD='library to billiard hallway'
BILLIARD_BALLROOM='billiard to ballroom hallway'
BILLIARD_DINING='billiard to dining room hallway'
DINING_KITCHEN='dining room to kitchen hallway'
CONSERVATORY_BALLROOM='conservatory to ballroom hallway'
BAllROOM_KITCHEN='ballroom to kitchen hallway'
      
HALLWAYS = [
    STUDY_LIBRARY,
    STUDY_HALL,
    HALL_BILLIARD,
    HALL_LOUNGE,
    LOUNGE_DINING,
    LIBRARY_CONSERVATORY,
    LIBRARY_BILLIARD,
    BILLIARD_BALLROOM,
    BILLIARD_DINING,
    DINING_KITCHEN,
    CONSERVATORY_BALLROOM,
    BAllROOM_KITCHEN
]
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


    def __init__(self, players, turn_list=None, current_player=None, turn_status=None, current_suggestions=None, 
                 suggestion_response=None, case_file=None, game-active=True, game_winner=None, game_board=None):
        
        __instance = self
        self.deck = Deck()
        self.board = GameBoard()
        self.players= players
    
    if turn_list:
        self.turn_list = turn_list
    else:
        self.turn_list = list(players)
    
    if current_player:
        self.current_player = current_player
    else:   
        self.current_player = self.turn_list[0]
   
    
    if game_board:
        self.game_board = game_board
    else:
        self.game_board = {
                KITCHEN: Room(
                space_id = KITCHEN,
                adjacent_spaces = [
                DINING_KITCHEN,
                BALLROOM_KITCHEN,
                STUDY
                ]
                weapons=[ROPE]
            ),
            STUDY_LIBRARY: Hallway(
                space_id = STUDY_LIBRARY
                adjacent_spaces = [STUDY, LIBRARY]
            ),
            MUSTARD: HomeSpace(
                space_id = MUSTARD,
                connected_spaces=[
                    LOUNGE_DINING
                ],
                suspects=[MUSTARD]
              
                
                
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
