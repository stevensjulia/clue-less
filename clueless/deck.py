import random
from collections import defaultdict


class Deck:
    weapon_cards = []
    character_cards = []
    room_cards = []

    def __init__(self):
        rooms = ['Kitchen', 'Conservatory', 'Dining Room', 'Ballroom', 'Study', 'Hall', 'Lounge', 'Library',
                 'Billiard Room']
        weapons = ['Revolver', 'Lead Pipe', 'Rope', 'Candle Stick', 'Wrench', 'Knife']
        characters = ['Miss Scarlet', 'Mrs Peacock', 'Col Mustard', 'Prof Plum', 'Mrs White', 'Mr Green']

        self.character_cards = Deck.initialize_cards(characters, 'Character')
        self.weapon_cards = Deck.initialize_cards(weapons, 'Weapon')
        self.room_cards = Deck.initialize_cards(rooms, 'Room')

    def get_characters(self):
        return self.character_cards

    def get_weapons(self):
        return self.weapon_cards

    def get_rooms(self):
        return self.room_cards

    @staticmethod
    def initialize_cards(values, card_type):
        cards = []

        for value in values:
            cards.append(Card(value, card_type))

        return cards

    @staticmethod
    def shuffle(characters, weapons, rooms):
        deck = characters + weapons + rooms
        random.shuffle(deck)

        return deck

    @staticmethod
    def deal_cards(deck, num_players):
        players_cards = defaultdict(list)
        player_num = 0

        for i in range(0, len(deck)):
            if player_num < num_players:
                players_cards[player_num].append(deck[i])
            else:
                player_num = 0
                players_cards[player_num].append(deck[i])
            player_num += 1

        return players_cards

    @staticmethod
    def fill_case_file(deck):
        case_file = deck[0:3]
        deck = deck[3:]

        return case_file, deck

    def initialize_game(self, num_players):
        # shuffle cards
        deck = Deck.shuffle(self.character_cards, self.weapon_cards, self.room_cards)

        # fill the case file and remove those cards from the deck
        case_file, deck = Deck.fill_case_file(deck)

        # deal a set of cards for each player
        players_cards = Deck.deal_cards(deck, num_players)

        return tuple(case_file), players_cards


class Card:
    value = None
    card_type = None

    def __init__(self, value, card_type):
        self.value = value
        self.card_type = card_type

    def get_value(self):
        return self.value

    def get_type(self):
        return self.card_type
