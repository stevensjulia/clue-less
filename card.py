from space import Space

class Card:
    value = None
    card_type = None

    def __init__(self, value, card_type):
        self.value = value
        self.type = card_type

    def get_value(self):
        return self.value

    def get_type(self):
        return self.card_type
