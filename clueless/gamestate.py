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

class GameState:
    players = []
    board = None
    }
     
    def __init__(self):
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
   # this gives the current suggestion. it is waiting for a response
    self.current_suggestion = current_suggestion
   # this gives the player that needs to respond to the suggestions
    self.suggestion_response_player = suggestion_response_player
   
    if case_file:
        self.case_file = case_file
    else:
        self.case_file = list()
    self.game_active=game_active
    self.game_winner = game_winner
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
              
                
                
  
