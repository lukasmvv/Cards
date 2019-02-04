class Card():
    """Class for a single card"""

    def __init__(self, suit, value):

        self.suit = suit
        self.value = value

    def get_card(self):
        """Getting string value of single card"""

        if self.value == 0:
            return str(self.suit)
        else:
            return str(self.value) + str(self.suit)
