
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
    suspects = None
    type = None

    def __init__(self, space_id, space_type, adjacent_spaces):
        self.space_id = space_id
        self.type = space_type
        self.adjacent_spaces = adjacent_spaces
        
    def set_occupied(self):
        self.occupied = True
    
    def set_notoccupied(self):
        self.occupied = False

    def get_adjacent_spaces(self):
        return self.adjacentSpaces
class HomeSpace(Space):
    """
    This represents the starting space for the players which is the sam each game. starting square only has one occupant at a time.
    """
    def __init__(self, space_id, adjacent_spaces, suspects=None):
        super(Space, self).__init__(space_id, adjacent_spaces, suspects)
    def set_occupied(self):
        self.occupied = True
    
class Hallway(Space):
        """
        The hallway spaces connect two rooms
        """
    def __init__(self, space_id, adjacent_spaces, suspects=None):
        super(Space,self).__init__(space_id, adjacent_spaces, suspects)
    def set_occupied(self):
        self.occupied = True
    
    def set_notoccupied(self):
        self.occupied = False

class Room(Space):
    associated_card = None
    secret_passage = None
    weapons = None
    
    def __init__(self, space_id, space_type, associated_card, weapons, secret_passage=False):
        Space.__init__(space_id, space_type)
        self.associated_card = associated_card
        self.secret_passage = secret_passage
    
    def set_occupied(self):
        self.occupied = True
    
    def set_notoccupied(self):
        self.occupied = False

    if weapons:
            self.weapons = weapons
        else:
            self.weapons = list()
