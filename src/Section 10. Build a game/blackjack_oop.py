import random

class Card:
    # Lists of card instances will be defined in class Board. So you'll be able to choose only a certain predefined value
    def __init__(self, suit, value):
        self._suit = suit
        self._value = value

    @property
    def suit(self):
        return self._suit

    @property
    def value(self):
        return self._value

    # !! Values must be presented in "self._<attr>" format! Otherwise it's an error as the method doesn't where to call value from
    def show(self):
        print(f'{self._value} of {self._suit}')


class Deck:
    # Here we define the list of suits. As a class attr as all cards will have a value from this list
    suits = ["Spades", "Clubs", "Diamonds", "Hearts"]

    def __init__(self):
        # this attr is protected with no getters/setters as no one should change it
        # this method by default create an empty list of cards.
        self._cards = []
        self.build()  # !! after creating a card list we immediately fill it with all cards

    #
    def build(self):
        # [(suit, value) for suit in Deck.suits for value in range(1, 12)]  # for a list
        # An extended version of the loop above
        for suit in Deck.suits:
            for value in range(1, 12):
                # print(suit, val)    it's not good as we need to save the data
                # Card(suit, value) is an instance of class Card, and we append it to the list of cards created in init method
                self._cards.append(Card(suit, value))

    def show(self):
        for card in self._cards:
            card.show()   # ! here we call show() method of a card instance of class Card. so no need for any specifications

    def shuffle(self):
        # a simple random shuffle could be used as well
        # the Fisher-Yates Shuffle Algorithm implementation.
        for i in range(len(self._cards)-1, 0, 1):
            rand = random.randint(0, i)
            # initial [i] position will be swapped with [rand] position
            self._cards[i], self._cards[rand] = self._cards[i]

    def draw(self):
        # if statement is required because we check if the card list is not empty already
        if self._cards:
            return self._cards.pop()


class Player:
    def __init__(self, name, hand, is_dealer=False):
        self._name = name
        self._hand = hand
        self._is_dealer = is_dealer



class CardGame:
    pass
