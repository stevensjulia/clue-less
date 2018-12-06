
class GameBoard:
    spaces = []
    def __init__(self):
        #newspace = Space( space_id = 1, occupied = False, adjacentSpaces = [10,2], type = None)
        #Library = Room( space_id = 2, occupied = False, adjacentSpaces = [1,3], type = Room)
        pass

    def get_space(space_id):
        return space_id


class Space:
    space_id = None
    occupied = False
    adjacent_spaces = []
    type = None

    def __init__(self, space_id, space_type, adjacent_spaces):
        self.space_id = space_id
        self.type = space_type
        self.adjacent_spaces = adjacent_spaces

    def set_occupied(self):
        self.occupied = True

    def get_adjacent_spaces(self):
        return self.adjacentSpaces


class Room(Space):
    associated_card = None
    secret_passage = None

    def __init__(self, space_id, space_type, associated_card, secret_passage=False):
        Space.__init__(space_id, space_type)
        self.associated_card = associated_card
        self.secret_passage = secret_passage