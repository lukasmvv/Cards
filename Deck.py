from random import randint

from Card import Card


class Deck():
    """Class for a deck of cards"""

    def __init__(self, jokers=False):

        self.jokers = jokers
        self.deck = self.create_deck()

    def create_deck(self):
        """Creates a deck of 52 (or 54) Cards"""

        deck = []

        # Suits and face values
        suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        face_values = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

        # Creating deck
        for suit in suits:
            for value in face_values:
                deck.append(Card(suit[0], value))

        # Adding jokers
        if self.jokers:
            deck.append(Card('Jk', 0))
            deck.append(Card('Jk', 0))

        return deck

    def print_deck(self):
        """Printing deck as a list"""

        ls = []
        for card in self.deck:
            ls.append(card.get_card())
        print(ls)

    def get_deck_as_str_list(self):
        """Getting deck as string list"""

        ls = []
        for card in self.deck:
            ls.append(card.get_card())
        return ls

    def shuffle_deck(self, num):
        """Shuffles deck"""

        # Length of current deck
        length = len(self.deck)

        # Shuffling deck
        for y in range(num):
            for i in range(length):
                new_index = randint(0, length)
                temp_card = self.deck[i]
                self.deck[i] = self.deck[new_index]
                self.deck[new_index] = temp_card
