from board import GameBoard


class Space:
    space_id = None
    occupied = False
    adjacentSpaces = []
    type = None

    def __init__(self, space_id, type):
        self.space_id = space_id
        self.type = type
        self.get_adjacent_spaces = GameBoard.get_adjacent_spaces(space_id)

    def set_occupied(self):
        self.occupied = True


class Room(Space):
    associated_card = None
    secret_passage = None

    def __init__(self, space_id, type, associated_card, secret_passage=False):
        Space.__init__(space_id, type)