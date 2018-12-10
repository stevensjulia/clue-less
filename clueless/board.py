
# Game constants

SUSPECT = 'Suspect'
SCARLET = 'Miss Scarlet'
WHITE = 'Mrs White'
PEACOCK = 'Mrs Peacock'
MUSTARD = 'Col Mustard'
PLUM = 'Prof Plum'
GREEN = 'Mr Green'

SUSPECTS = [
    MUSTARD,
    SCARLET,
    PLUM,
    GREEN,
    WHITE,
    PEACOCK,
]

WEAPON = 'Weapon'
ROPE = 'Rope'
LEAD_PIPE = 'Lead Pipe'
KNIFE = 'Knife'
WRENCH = 'Wrench'
CANDLESTICK = 'Candlestick'
REVOLVER = 'Revolver'

WEAPONS = [
    ROPE,
    LEAD_PIPE,
    KNIFE,
    WRENCH,
    CANDLESTICK,
    REVOLVER
]

ROOM = 'Room'
BALLROOM = 'Ballroom'
BILLIARD_ROOM = 'Billiard Room'
CONSERVATORY = 'Conservatory'
DINING_ROOM = 'Dining Room'
HALL = 'Hall'
KITCHEN = 'Kitchen'
LIBRARY = 'Library'
LOUNGE = 'Lounge'
STUDY = 'Study'

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
STUDY_HALL = 'one'
HALL_BILLIARD = 'four'
HALL_LOUNGE = 'two'
LOUNGE_DINING = 'five'
LIBRARY_CONSERVATORY = 'eight'
LIBRARY_BILLIARD = 'six'
BILLIARD_BALLROOM = 'nine'
BILLIARD_DINING = 'seven'
DINING_KITCHEN = 'ten'
CONSERVATORY_BALLROOM = 'eleven'
BALLROOM_KITCHEN = 'twelve'

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
    BALLROOM_KITCHEN
]


class GameBoard:
    spaces = {}
    character_positions = {}

    def __init__(self):
        self.spaces = {
            BALLROOM: Room(
                space_id=BALLROOM,
                adjacent_spaces=[BALLROOM_KITCHEN, CONSERVATORY_BALLROOM, BILLIARD_BALLROOM],
                weapons=[LEAD_PIPE]
            ),
            BILLIARD_ROOM: Room(
                space_id=BILLIARD_ROOM,
                adjacent_spaces=[HALL_BILLIARD, LIBRARY_BILLIARD, BILLIARD_BALLROOM, BILLIARD_DINING],
                weapons=[KNIFE]
            ),
            CONSERVATORY: Room(
                space_id=CONSERVATORY,
                adjacent_spaces=[CONSERVATORY_BALLROOM, LIBRARY_CONSERVATORY, LOUNGE],
                weapons=[CANDLESTICK],
                secret_passage=LOUNGE,
            ),
            DINING_ROOM: Room(
                space_id=DINING_ROOM,
                adjacent_spaces=[LOUNGE_DINING, BILLIARD_DINING, DINING_KITCHEN]
            ),
            HALL: Room(
                space_id=HALL,
                adjacent_spaces=[STUDY_HALL, HALL_BILLIARD, HALL_LOUNGE]
            ),
            KITCHEN: Room(
                space_id=KITCHEN,
                adjacent_spaces=[DINING_KITCHEN, BALLROOM_KITCHEN, STUDY],
                weapons=[ROPE],
                secret_passage=STUDY,
            ),
            LIBRARY: Room(
                space_id=LIBRARY,
                adjacent_spaces=[STUDY_LIBRARY, LIBRARY_CONSERVATORY, LIBRARY_BILLIARD],
                weapons=[WRENCH]
            ),
            LOUNGE: Room(
                space_id=LOUNGE,
                adjacent_spaces=[CONSERVATORY, HALL_LOUNGE, LOUNGE_DINING],
                secret_passage=CONSERVATORY,
            ),
            STUDY: Room(
                 space_id=STUDY,
                 adjacent_spaces=[KITCHEN, STUDY_LIBRARY, STUDY_HALL],
                 weapons=[REVOLVER],
                 secret_passage=KITCHEN,
            ),
            STUDY_LIBRARY: Space(
                space_id=STUDY_LIBRARY,
                adjacent_spaces=[STUDY, LIBRARY]
            ),
            STUDY_HALL: Space(
                space_id=STUDY_HALL,
                adjacent_spaces=[STUDY, HALL]
            ),
            HALL_BILLIARD: Space(
                space_id=HALL_BILLIARD,
                adjacent_spaces=[HALL, BILLIARD_ROOM]
            ),
            HALL_LOUNGE: Space(
                space_id=HALL_LOUNGE,
                adjacent_spaces=[HALL, LOUNGE]
            ),
            LOUNGE_DINING: Space(
                space_id=LOUNGE_DINING,
                adjacent_spaces=[LOUNGE, DINING_ROOM]
            ),
             BALLROOM_KITCHEN:  Space(
                 space_id=BALLROOM_KITCHEN,
                 adjacent_spaces=[BALLROOM, KITCHEN]
             ),
             LIBRARY_CONSERVATORY: Space(
                space_id=LIBRARY_CONSERVATORY,
                adjacent_spaces=[LIBRARY, CONSERVATORY]
             ),
             LIBRARY_BILLIARD: Space(
                 space_id=LIBRARY_BILLIARD,
                 adjacent_spaces=[LIBRARY, BILLIARD_ROOM]
             ),
             BILLIARD_BALLROOM:  Space(
                 space_id=BILLIARD_BALLROOM,
                 adjacent_spaces=[BILLIARD_ROOM, BALLROOM]
             ),
             DINING_KITCHEN: Space(
                 space_id=DINING_KITCHEN,
                 adjacent_spaces=[DINING_ROOM, KITCHEN]
                ),
             CONSERVATORY_BALLROOM: Space(
                 space_id=CONSERVATORY_BALLROOM,
                 adjacent_spaces=[CONSERVATORY, BALLROOM]
                ),
             BILLIARD_DINING: Space(
                 space_id=BILLIARD_DINING,
                 adjacent_spaces=[BILLIARD_ROOM, DINING_ROOM]
                ),
        }

        self.initialize_adjacent_spaces()

    def initialize_adjacent_spaces(self):
        # initalize adjacent spaces as actual Space objects rather than Strings
        for space in self.spaces:
            space_obj = self.spaces.get(space)
            new_spaces = []
            space_strings = space_obj.adjacent_spaces
            for val in space_strings:
                new_spaces.append(self.spaces.get(val))

            space_obj.adjacent_spaces = new_spaces

    def get_space(self, space_id):
        return self.spaces.get(space_id)

    def get_character_in_space(self, space_id):
        if space_id not in self.spaces:
            raise Exception('This is not a valid space!')
        else:
            characters = self.spaces.get(space_id).suspects
            if characters is None:
                return ""
            else:
                return characters

    def get_weapon_in_space(self, space_id):
        if space_id not in self.spaces:
            raise Exception('This is not a valid space!')
        else:
            return ",".join(self.spaces.get(space_id).weapons)

    def initialize_character_position(self, character):
        character_starting_location = {
            SCARLET: HALL_LOUNGE,
            PEACOCK: LIBRARY_CONSERVATORY,
            MUSTARD: LOUNGE_DINING,
            PLUM: STUDY_LIBRARY,
            WHITE: BALLROOM_KITCHEN,
            GREEN: CONSERVATORY_BALLROOM,
        }

        if character not in character_starting_location:
            raise Exception("This is not a valid character name!")
        else:
            loc = character_starting_location.get(character)
            spc = self.spaces.get(loc)
            spc.add_suspect(character)

            # keep track of character locations
            self.character_positions[character] = spc
            return spc

    def locate_character(self, character):
        if character in self.character_positions:
            return self.character_positions.get(character)
        else:
            raise ValueError("Invalid character name.")

class Space:
    space_id = None
    occupied = False
    adjacent_spaces = []
    suspects = ""

    def __init__(self, space_id, adjacent_spaces, suspects=None):
        self.space_id = space_id
        self.adjacent_spaces = adjacent_spaces
        self.suspects = suspects

    def set_occupied(self):
        self.occupied = True

    def set_not_occupied(self):
        self.occupied = False

    def get_adjacent_spaces(self):
        return self.adjacentSpaces

    def add_suspect(self, character):
        if self.suspects is not None:
            raise Exception("This room is already occupied!")
        else:
            self.suspects = character
            self.occupied = True

    def remove_suspect(self, character):
        if self.suspects is not character:
            raise Exception("Cannot remove suspect from room as suspect is not currently occupying this room.")
        else:
            self.suspects = None
            self.occupied = False


class Room(Space):
    secret_passage = None
    weapons = []
    suspects = []

    def __init__(self, space_id, adjacent_spaces, weapons=[], secret_passage=None):
        Space.__init__(self, space_id, adjacent_spaces)
        self.secret_passage = secret_passage
        self.weapons = weapons
        self.suspects = []

    def set_occupied(self):
        self.occupied = True

    def set_not_occupied(self):
        self.occupied = False

    def add_suspect(self, character):
        self.suspects.append(character)
        self.occupied = True

    def remove_suspect(self, character):
        if character not in self.suspects:
            raise Exception("Cannot remove suspect from room as suspect is not currently occupying this room.")
        else:
            self.suspects.remove(character)
            if len(self.suspects) == 0:
                self.occupied = False
