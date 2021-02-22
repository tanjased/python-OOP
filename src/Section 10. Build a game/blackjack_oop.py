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
            card.show()  # ! here we call show() method of a card instance of class Card. so no need for any specifications

    def shuffle(self):
        # a simple random shuffle could be used as well
        # the Fisher-Yates Shuffle Algorithm implementation.
        for i in range(len(self._cards) - 1, 0, -1):
            rand = random.randint(0, i)
            # initial [i] position will be swapped with [rand] position
            self._cards[i], self._cards[rand] = self._cards[rand], self._cards[i]

    def draw(self):
        # if statement is required because we check if the card list is not empty already
        if self._cards:
            return self._cards.pop()


class Player:
    def __init__(self, name, is_dealer=False):
        self._name = name
        self._hand = []  # this list is going to contain instances of Card class.
        # !! again. we define the hand (list of cards) as an empty list. so no need to put in (self, ...)
        self._is_dealer = is_dealer

    @property
    def name(self):  # read only property as we don't want to change the name after the instance's created
        return self._name

    @property
    def is_dealer(self):
        return self._is_dealer

    # We don't create getters/setters for hand as we don't want to provide access to hand, it will be done by methods
    def draw(self, deck):  # make it through a new var, not Deck.draw() class reference
        self._hand.append(deck.draw())  # deck.draw() will be replaced by an instance of card
        return self  # return the reference to the instance that is calling the method. METHOD CHAINING. so the method can be called a few times

    def show_hand(self,
                  reveal_card=False):  # True if the card of the dealer should be revealed. If the player that called the method is not the dealer, this value has no effect.
        if not self._is_dealer:
            for card in self._hand:
                card.show()
        else:  # when player is the dealer
            for i in range(len(self._hand) - 1):  # because we want to hide the last card in the hand
                self._hand[i].show()
            if reveal_card:
                self._hand[-1].show()
            else:
                print("a X symbol")

    def discard(self):
        return self._hand.pop()

    def get_hand_value(self):
        value = 0
        for card in self._hand:
            value += card.value
        return value  # !!!! here was the error


# The complete logic of the game
class CardGame:
    INSTRUCTIONS = "Welcome to the Blackjack game. The main rule is \n to get to 21 as close as possible. \n That's it."

    def __init__(self, deck, player, dealer):
        self.deck = deck
        self.player = player
        self.dealer = dealer
        # this method starts the game immediately
        self.start_game()

    # The main logic of the game is in this method
    def start_game(self):
        # First the instructions
        print(CardGame.INSTRUCTIONS)

        # Count number of turns
        turn = 1

        self.deck.shuffle()
        # Player and dealer draw 2 cards each. self.deck as an arg as it is defined in the draw() method of class Player
        self.player.draw(self.deck).draw(self.deck)
        self.dealer.draw(self.deck).draw(self.deck)

        while True:
            print(f"--- TURN {turn} ---")

            print("The dealer's hand is:")
            self.dealer.show_hand()
            print("Your hand is:")
            self.player.show_hand()
            # Call self.player in every method because we reference to Player class this way
            if self.player.get_hand_value() > 21:
                print(f"The player lost. The count is {self.player.value} ")
                break
            elif self.player.get_hand_value() == 21:
                print(f"The count is {self.player.value}.")
                break

            choice = self.ask_choice()
            turn += 1

            if choice == 1:
                self.player.draw(self.deck)
            else:
                break

        # When we break out of the loop, we present the results
        player_hand = self.player.get_hand_value()
        print("\nValue - your hand: ", player_hand)
        dealer_hand = self.dealer.get_hand_value()
        print("\nValue - dealer's hand: ", dealer_hand)

        print("\nThe dealer's hand was:")
        self.dealer.show_hand(True)

        # Define lose/win conditions
        if player_hand > 21:
            print(f"You lose, {self.player.name}")
        elif dealer_hand > 21 or player_hand == 21 or player_hand > dealer_hand:
            print(f"You win, {self.player.name}")
        elif player_hand < dealer_hand:
            print(f"You lose, {self.player.name}")
        else:
            print("We have a tie.")

    def ask_choice(self):
        print("Type 1 if you want to ask for another card,\n type 2 if you stand")
        choice = int(input())
        if choice == 1 or choice == 2:
            return choice
        else:
            print("the value was invalid. I assume you want to stand.")
            return 2


# Run the game
deck = Deck()
you = Player("Flower")
dealer = Player("The dealer", is_dealer=True)

game = CardGame(deck, you, dealer)
