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
    PEACOCK,
    ]

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
BILLIARD_ROOM= 'Billiard Room'
CONSERVATORY= 'Conservatory'
DINING_ROOM= 'Dining Room'
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

STUDY_LIBRARY = 'three'
STUDY_HALL ='one'
HALL_BILLIARD='four'
HALL_LOUNGE='two'
LOUNGE_DINING='five'
LIBRARY_CONSERVATORY='eight'
LIBRARY_BILLIARD='six'
BILLIARD_BALLROOM='nine'
BILLIARD_DINING='seven'
DINING_KITCHEN='ten'
CONSERVATORY_BALLROOM='eleven'
BAllROOM_KITCHEN='twelve'
      
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


    def __init__(self, players, turn_list=None, current_player=None, turn_status=None, current_suggestions=None,
                 suggestion_response=None, case_file=None, game_active=True, game_winner=None, game_board=None):


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
                BALLROOM: Room(
                    space_id=BALLROOM,
                    adjacent_spaces=[
                            BALLROOM_KITCHEN,
                            CONSERVATORY_BALLROOM,
                            BILLIARD_BALLROOM
                        ],
                    weapons=[LEAD_PIPE]
                    ),
                BILLIARD_ROOM: Room(
                    space_id=BILLIARD_ROOM,
                    adjacent_spaces=[
                            HALL_BILLIARD,
                            LIBRARY_BILLIARD,
                            BILLIARD_BALLROOM,
                            BILLIARD_DINING
                        ],
                    weapons=[KNIFE]
                    ),
                CONSERVATORY: Room(
                    space_id=CONSERVATORY,
                    adjacent_spaces=[
                    CONSERVATORY_BALLROOM,
                    LIBRARY_CONSERVATORY,
                    LOUNGE
                        ],
                    weapons=[CANDLESTICK]
                    ),
                DINING_ROOM: Room(
                    space_id=DINING_ROOM,
                    adjacent_spaces=[
                            LOUNGE_DINING,
                            BILLIARD_DINING,
                            DINING_KITCHEN
                        ]
                    ),
                HALL: Room(
                    space_id=HALL,
                    adjacent_spaces=[
                            STUDY_HALL,
                            HALL_BILLIARD,
                            HALL_LOUNGE
                        ]
                    ),

                KITCHEN: Room(
                    space_id = KITCHEN,
                    adjacent_spaces = [
                    DINING_KITCHEN,
                    BALLROOM_KITCHEN,
                    STUDY
                    ]
                    weapons=[ROPE]
                    ),
                LIBRARY: Room(
                    space_id=LIBRARY,
                    adjacent_spaces=[
                            STUDY_LIBRARY,
                            LIBRARY_CONSERVATORY,
                            LIBRARY_BILLIARD
                        ],
                    weapons=[WRENCH]
                    ),
                LOUNGE: Room(
                    space_id=LOUNGE,
                    adjacent_spaces=[
                            CONSERVATORY,
                            HALL_LOUNGE,
                            LOUNGE_DINING
                        ]
                    ),
                 STUDY: Room(
                     space_id=STUDY,
                     adjacent_spaces=[
                            KITCHEN,
                            STUDY_LIBRARY,
                            STUDY_HALL
                        ],
                     weapons=[REVOLVER]
                    ),
                STUDY_LIBRARY: Hallway(
                    space_id = STUDY_LIBRARY
                    adjacent_spaces = [STUDY, LIBRARY]
                ),
                STUDY_HALL: Hallway(
                    space_id=STUDY_HALL,
                    adjacent_spaces=[
                            STUDY,
                            HALL
                        ]
                    ),
                HALL_BILLIARD: Hallway(
                    space_id=HALL_BILLIARD,
                    adjacent_spaces=[
                            HALL,
                            BILLIARD_ROOM
                        ]
                    ),
                HALL_LOUNGE: Hallway(
                    space_id=HALL_LOUNGE,
                    adjacent_spaces=[
                            HALL,
                            LOUNGE
                        ]
                    ),
                LOUNGE_DINING: Hallway(
                    space_id=LOUNGE_DINING,
                    adjacent_spaces=[
                            LOUNGE,
                            DINING_ROOM
                        ]
                    ),
                 BALLROOM_KITCHEN:  Hallway(
                     space_id=BALLROOM_KITCHEN,
                     adjacent_spaces=[
                            BALLROOM,
                            KITCHEN
                        ]
                    ),
                 LIBRARY_CONSERVATORY: Hallway(
                    space_id=LIBRARY_CONSERVATORY,
                    adjacent_spaces=[
                            LIBRARY,
                            CONSERVATORY
                        ]
                    ),
                 LIBRARY_BILLIARD: Hallway(
                     space_id=LIBRARY_BILLIARD,
                     adjacent_spaces=[
                            LIBRARY,
                            BILLIARD_ROOM
                        ]
                    ),
                 BILLIARD_BALLROOM:  Hallway(
                     space_id=BILLIARD_BALLROOM,
                     adjacent_spaces=[
                            BILLIARD_ROOM,
                            BALLROOM
                        ]
                    ),
                 DINING_KITCHEN: Hallway(
                     space_id=DINING_KITCHEN,
                     adjacent_spaces=[
                            DINING_ROOM,
                            KITCHEN
                        ]
                    ),
                 CONSERVATORY_BALLROOM: Hallway(
                     space_id=CONSERVATORY_BALLROOM,
                     adjacent_spaces=[
                            CONSERVATORY,
                            BALLROOM
                        ]
                    ),
                 BILLIARD_DINING: Hallway(
                     space_id=BILLIARD_DINING,
                     adjacent_spaces=[
                            BILLIARD_ROOM,
                            DINING_ROOM
                        ]
                    ),
                SCARLET: HomeSpace(
                    space_id=SCARLET,
                    adjacent_spaces=[
                            HALL_LOUNGE
                        ],
                    suspects=[SCARLET]
                    ),
                 WHITE: HomeSpace(
                     space_id=WHITE,
                     adjacent_spaces=[
                          BALLROOM_KITCHEN
                        ],
                     suspects=[WHITE]
                    ),
                PEACOCK: HomeSpace(
                     space_id=PEACOCK,
                     adjacent_spaces=[
                            LIBRARY_CONSERVATORY
                        ],
                     suspects=[PEACOCK]
                    ),
                PLUM: HomeSquare(
                     space_id=PLUM,
                     adjacent_spaces=[
                            STUDY_LIBRARY
                        ],
                     suspects=[PLUM]
                    ),
                MUSTARD: HomeSpace(
                    space_id = MUSTARD,
                    connected_spaces=[
                        LOUNGE_DINING
                    ],
                    suspects=[MUSTARD]
                ),
                GREEN: HomeSquare(
                    space_id=GREEN,
                    adjacent_spaces=[
                            CONSERVATORY_BALLROOM
                        ],
                    suspects=[GREEN]
                    )
            }

 class BuidGameState(object):
    def build_gamestate_from_dict(self, game_state_dict):

        game_state = game_state_dict.copy()

        #build the list of Player objects
        game_state["players"] = self._build_players(game_state["players"])

        #reference the Player objects that are in the turn list
        game_state["turn_list"] = [
            player for player in game_state["players"]
            if player.username in [
                turn_list_player["username"]
                for turn_list_player in game_state["turn_list"]
            ]
        ]

        #reference the Player object for the current turn
        if game_state["current_player"]:
            game_state["current_player"] = [
                player for player in game_state["players"]
                if player.username == game_state["current_player"]["username"]
            ][0]

        if game_state["current_suggestion"]:
            game_state["current_suggestion"] = Suggestion(
                **game_state["current_suggestion"]
            )
        if game_state["suggestion_response_player"]:
            game_state["suggestion_response_player"] = [
                player for player in game_state["players"]
                if player.username ==
                game_state["suggestion_response_player"]["username"]
            ][0]

        #build the list of winning GameCard objects
        game_state["case_file"] = self._build_game_cards(
            game_state["case_file"])

        if game_state["game_winner"]:
            game_state["game_winner"] = [
                player for player in game_state["players"]
                if player.username == game_state["game_winner"]["username"]
            ][0]

        game_board = dict()
        #assign the lists of newly created gamespace objects to the game_board
        for key in game_state["game_board"]:
            if key in ROOMS:
                game_board[key] = Room(**game_state["game_board"][key])
            if key in HALLWAYS:
                game_board[key] = Hallway(**game_state["game_board"][key])
            if key in SUSPECTS:
                game_board[key] = HomeSquare(**game_state["game_board"][key])

        game_state["game_board"] = game_board

        #return a new GameState object built from the game state dictionary
        return GameState(**game_state)

    

    def _build_players(self, players):
        for player_dict in players:
            player_dict["game_cards"] = self._build_game_cards(
                player_dict["game_cards"])
            player_dict["card_items_seen"] = self._build_game_cards(
                player_dict["card_items_seen"])

        return [Player(**player_dict) for player_dict in players]
 
    def _build_game_cards(self, game_cards):
        return [
            GameCard(**game_card_dict) for game_card_dict in game_cards
        ]    
              
                
                
  
