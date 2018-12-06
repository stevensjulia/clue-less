class Notepad:
    possibleCharacters = []
    possibleWeapons = []
    possibleRooms = []

    def __init__(self, deck):
        self.possibleCharacters = deck.get_characters()
        self.possibleWeapons = deck.get_weapons()
        self.possibleRooms = deck.get_rooms()

    def get_possible_characters(self):
        return self.possibleCharacters

    def get_possible_weapons(self):
        return self.possibleWeapons

    def get_possible_rooms(self):
        return self.possibleRooms

    def remove_character(self, name):
        self.possibleCharacters.remove(name)

    def remove_weapon(self, name):
        self.possibleWeapons.remove(name)

    def remove_room(self, name):
        self.possibleRooms.remove(name)
