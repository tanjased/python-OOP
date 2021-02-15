import random  # to choose a random value from a list, random module or secrets module can be used


# random.choice(mylist) or secrets.choice(mylist)

# noinspection PyShadowingNames
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
        move = str(row) + col           # !! we can't sum up int and str. so need to convert int -> str. and also use print so user can see the comp choice
        print("Computer move (O): ", move)
        return move


# Now define the board
# noinspection PyShadowingNames
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

    # this method is defined after is_move_valid()
    def submit_move(self, move, player):
        if not self.is_move_valid(move):            # ALWAYS add self. when calling other methods.
            print("Invalid input. Format example - '1A'. ")
            return  # !!! not sure. Because we want to end the function. That's the way. AA it returns FALSE and automatically ends
        else:
            row_index = int(move[0]) - 1        # move is str (input). we define index position in the list, which are 0, 1, 2
            col_index = Board.COLUMNS[move[1]]  # first i put self.COLUMNS, which is not right as it calls the instance while it's a class attr
            # retrieve value el from a 2 dim list
            value = self.game_board[row_index][col_index]
            # if the value is EMPTY (zero), it means that the cell is empty and we can set player's marker there
            if value == Board.EMPTY:
                self.game_board[row_index][col_index] = player.marker
            else:
                print("This position is already taken.")

    # Format: "1A". We check if the length of input move is 2 el., if 1st el is in class attr ROWS
    # and if 2nd el is in class attr COLUMNS.
    # If all conditions are satisfied, True is returned.
    def is_move_valid(self, move):
        return (len(move) == 2) and (int(move[0]) in Board.ROWS) and (move[1] in Board.COLUMNS)

    # Check if the player wins. Next methods are necessary to complete this method
    def is_winner(self, player, row, col):
        # assume rows and cols as str
        if self.check_row(row, player):
            return True
        elif self.check_col(col, player):
            return True
        elif self.check_diagonal(player):
            return True
        elif self.check_antidiagonal(player):
            return True
        else:               # this means player hasn't won the game
            return False

    # So these are: check row, check column, check diagonal, check antidiagonal
    # !! besides checking if all the elements are equal, we also should check if the number of elements
    # equals to 3, as a zero value still might be there
    # !! don't forget the input arg row.. are passed in as str. so we need to convert them into int
    def check_row(self, row, player):
        row_index = int(row) - 1
        # this line returns the current row
        board_row = self.game_board[row_index]
        # var.count(el) counts how many times the marker appears in the list
        if board_row.count(player.marker) == 3:
            return True
        else:
            return False

    # don't forget col is str
    def check_col(self, col, player):
        col_index = Board.COLUMNS[col]
        # keep track of a total number of markers we found for the player
        total_markers = 0
        # counts how many markers of the same player are in the column
        for i in range(3):
            if self.game_board[i][col_index] == player.marker:
                total_markers += 1
        # this means the user has won the game
        if total_markers == 3:
            return True
        else:
            return False

    # ! the els have the same index row and col positions: row=1 and col=1, row=2 and col=2
    def check_diagonal(self, player):
        total_markers = 0
        # which we implement here el[i][i]
        for i in range(3):
            if self.game_board[i][i] == player.marker:
                total_markers += 1
        if total_markers == 3:
            return True
        else:
            return False

    # dif combinations: [2][0], [1][1], [0][2]
    # So here we check these particular positions in for loop
    def check_antidiagonal(self, player):
        total_markers = 0
        # so we need to satisfy this scheme:
        #   row     col                         so the order is reverse. [i][2-i] satisfies this condition
        #   0       2
        #   1       1
        #   2       0
        for i in range(3):
            if self.game_board[i][2-i] == player.marker:
                total_markers += 1
        if total_markers == 3:
            return True
        else:
            return False


# The final part
# welcoming
print("****************")
print(" TIC-TAC-TOE ")
print("****************")
board = Board()
player = Player()
computer = Player("O", False)
board.print_board()

# keep continuing looping until the condition is met
while True:
    # first we define the human's move input value
    move = player.get_player_move()
    # submit the move to the board, check if it's valid or not and update the board accordingly
    board.submit_move(move, player)
    # visualize the update on the board
    board.print_board()

    # before checking if player won, we check if the move was valid
    if board.is_move_valid(move) and board.is_winner(player, move[0], move[1]):
        print("You win")
        break

    # if player hasn't won, ask for computer's move. Same steps as for the player
    comp_move = computer.get_player_move()
    board.submit_move(comp_move, computer)
    board.print_board()

    # repeat the check but now for the computer's move. No need for input validation as it was generated from the data
    if board.is_winner(computer, comp_move[0], comp_move[1]):
        print("The computer wins")
        break
# So basically the last while loop first checks the user input and if he wins the game is over
# if not the computer makes the move and if his move was to win, the game is over
# the loop keeps running until one of two conditions is satisfied.