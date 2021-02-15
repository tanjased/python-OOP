import random  # to choose a random value from a list, random module or secrets module can be used


# random.choice(mylist) or secrets.choice(mylist)

class Player:

    # Assign a default value to the human marker and True if the player is a human user.
    # So by default we set the parameters to a human user
    def __init__(self, marker="X", is_human=True):
        self._marker = marker
        self._is_human = is_human

    # Now we need to get access to the attributes for further use as they are protected
    @property
    def marker(self):
        return self._marker

    @property
    def is_human(self):
        return self._is_human

    # Now we define methods. get_player_move will call 2 other functions for user and computer
    # depending on whose move it is.
    def get_player_move(self):
        if self._is_human:  # !! firstly I typed just "if is_human", which is wrong as we have to refer to the init func
            return self.get_human_move()
        else:
            return self.get_computer_move()

    def get_human_move(self):
        move = input("Player input (X): ")
        return move  # but we assume here the user input has a correct format: 1A

    def get_computer_move(self):
        # Here we generate random move from 1-3 rows and A-C columns
        row = random.choice([1, 2, 3])  # or random.randint(1, 4)
        col = random.choice(['A', 'B', 'C'])  # or secrets.choice()
        move = str(row) + col
        print("Computer move (O): ",
              move)  # !! we can't sum up int and str. so need to convert int -> str. and also use print so user can see the comp choice
        return move


# Now define the board
class Board:
    # class attributes in UPPERCASE are constants and shouldn't be changed
    EMPTY = 0  # use a symbol to denote an empty cell
    COLUMNS = {"A": 0, "B": 1, "C": 2}
    ROWS = (1, 2, 3)  # create as a tuple to get advantage of the immutability, it can't be changed

    def __init__(self, game_board=None):
        # defined as None because user might want to start the game with a specific board. so there's a choice
        # customize the game board. in this case game_board is not None.
        if game_board:
            self.game_board = game_board
        # the default gameboard with zeros
        else:
            self.game_board = [[0, 0, 0],  # zeros are related to the constant EMPTY = 0
                               [0, 0, 0],
                               [0, 0, 0]]

    def print_board(self):
        print("    A   B   C")
        for i, row in enumerate(self.game_board, 1):
            print(i, end=" | ")
            for col in row:
                if col != Board.EMPTY:
                    print(col, end=" | ")
                else:
                    print("  | ", end="")
            print("\n---------------")


boa = Board()
boa.print_board()
