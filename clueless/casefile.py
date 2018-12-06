class CaseFile:
    character = None
    weapon = None
    room = None

    def __init__(self, character, weapon, room):
        self.character = character
        self.weapon = weapon
        self.room = room

    def check_solution(self, character, weapon, room):
        return (self.character is character) and (self.weapon is weapon) and (self.room is room)
