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
    def __init__(self, name, is_dealer=False):
        self._name = name
        self._hand = []     # this list is going to contain instances of Card class.
                            # !! again. we define the hand (list of cards) as an empty list. so no need to put in (self, ...)
        self._is_dealer = is_dealer

    @property
    def name(self):     # read only property as we don't want to change the name after the instance's created
        return self._name

    @property
    def is_dealer(self):
        return self._is_dealer

    # We don't create getters/setters for hand as we don't want to provide access to hand, it will be done by methods
    def draw(self, deck):                # make it through a new var, not Deck.draw() class reference
        self._hand.append(deck.draw())   # deck.draw() will be replaced by an instance of card
        return self     # return the reference to the instance that is calling the method

    def show_hand(self, reveal_card=False):      # True if the card of the dealer should be revealed. If the player that called the method is not the dealer, this value has no effect.
        if self._is_dealer:
            for card in self._hand:
                card.show()
        else:       # when player is the dealer
            for i in range(len(self._hand)-1):      # because we want to hide the last card in the hand
                self._hand[i].show()
            if reveal_card:
                self._hand[-1].show()
            else:
                print("Print a symbol to hide the card. X")

    def discard(self):
        return self._hand.pop()

    def get_hand_value(self):
        value = 0
        for card in self._hand:
            value += card.value



class CardGame:
    pass
