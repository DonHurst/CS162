# Author: Don Hurst
# Date: 02/22/2020
# Description: This file contains all of the definitions for the xiangqi game. This includes a board class, the game
# class, and classes for each of the pieces. All of the functionality is explained in docstrings at the head of each
# method


class Board:
    """The Board class contains an initializer that creates the board and places the pieces. It also has functions to
     return the piece at a specific location, a function to return the board, and a function to print the board for
     testing"""

    def __init__(self):
        """Initializer function creates the board and sets the pieces"""

        # Variables for number of rows / columns
        self.__rows = 10
        self.__columns = 9

        self.__gameBoard = []

        for x in range(self.__rows):
            board_y = []
            for y in range(self.__columns):
                board_y.append('0')
            self.__gameBoard.append(board_y)

        # Initialize Soldier Piece Placement
        self.__gameBoard[3][0] = Soldier('red')
        self.__gameBoard[3][2] = Soldier('red')
        self.__gameBoard[3][4] = Soldier('red')
        self.__gameBoard[3][6] = Soldier('red')
        self.__gameBoard[3][8] = Soldier('red')
        self.__gameBoard[6][0] = Soldier('black')
        self.__gameBoard[6][2] = Soldier('black')
        self.__gameBoard[6][4] = Soldier('black')
        self.__gameBoard[6][6] = Soldier('black')
        self.__gameBoard[6][8] = Soldier('black')

        # initialize Cannon Piece Placement
        self.__gameBoard[2][1] = Cannon('red')
        self.__gameBoard[2][7] = Cannon('red')
        self.__gameBoard[7][1] = Cannon('black')
        self.__gameBoard[7][7] = Cannon('black')

        # initialize Chariot Piece Placement
        self.__gameBoard[0][0] = Chariot('red')
        self.__gameBoard[0][8] = Chariot('red')
        self.__gameBoard[9][0] = Chariot('black')
        self.__gameBoard[9][8] = Chariot('black')

        # Initialize Horse Piece Placement
        self.__gameBoard[0][1] = Horse('red')
        self.__gameBoard[0][7] = Horse('red')
        self.__gameBoard[9][1] = Horse('black')
        self.__gameBoard[9][7] = Horse('black')

        # Initialize Elephant Piece Placement
        self.__gameBoard[0][2] = Elephant('red')
        self.__gameBoard[0][6] = Elephant('red')
        self.__gameBoard[9][2] = Elephant('black')
        self.__gameBoard[9][6] = Elephant('black')

        # Initialize Advisor Piece Placement
        self.__gameBoard[0][3] = Advisor('red')
        self.__gameBoard[0][5] = Advisor('red')
        self.__gameBoard[9][3] = Advisor('black')
        self.__gameBoard[9][5] = Advisor('black')

        # Initialize General Piece Placement
        self.__gameBoard[0][4] = General('red')
        self.__gameBoard[9][4] = General('black')

    def get_piece(self, x, y):
        """Get piece takes the row and column as parameters and returns the piece at that location on the board"""
        return self.__gameBoard[x][y]

    def get_board(self):
        """Get board returns the gameboard"""
        return self.__gameBoard

    def print_board(self):
        """The print board function prints the board in a way that makes sense visually. Used for testing"""

        row_counter = 1
        for row in reversed(self.__gameBoard):

            print(row)
            row_counter += 1


class XiangqiGame:
    """The XiangqiGame class contains the functionality for the game. To keep it brief, it contains an initializer to
    instantiate the board, a list for the corresponding letter positions, a value to store the current turn, and a val
    to store the current game state. It has a get game state function, is in check function, is in checkmate function,
    test move function, try all moves function, make move function, and functions to check the move for each of the
     pieces"""

    def __init__(self):
        """Init function for the game initializes the game board and a list to hold the corresponding letter values
        the user may enter to make a move. Initializes the current turn to red"""
        self.__gameBoard = Board()
        self.__letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
        self.__current_turn = 'red'
        self.__game_state = 'UNFINISHED'

    def get_game_state(self):
        """returns the current game state"""
        return self.__game_state

    def is_in_check(self, color):
        """the is in check function takes a color as the parameter. It searches the board and stores the red/black gens
        positions as tuples of row and column. It compares their columns and if they are the same, checks for the flying
        general rule. Else it runs through the board and sees if any of the opposing pieces has a valid move to take the
        general. IF so, it returns true."""

        # get red general position
        # nested for loop steps through the possible locations in the castle to find the general
        for row in range(0, 3):
            for col in range(3, 6):

                # checking if each space is an instance of the general class. If so, set that position as a tuple
                if isinstance(self.__gameBoard.get_piece(row, col), General):
                    red_general_position = (row, col)

        # nested for loop steps through the possible locations in the castle to find the general
        for row in range(7, 10):
            for col in range(3, 6):

                # checking if each space is an instance of the general class. If so, set that position as a tuple
                if isinstance(self.__gameBoard.get_piece(row, col), General):
                    black_general_position = (row, col)

        # create an empty list to check if generals are facing
        interim = []

        # if the general's column position is equal, search all interim values and append any non empty spaces to list
        if red_general_position[1] == black_general_position[1]:
            for x in range(red_general_position[0] + 1, black_general_position[0]):
                piece = self.__gameBoard.get_piece(x, black_general_position[1])
                if piece != '0':
                    interim.append(piece)

            # if the list is empty, the generals are facing. Will return TRUE. Else, continues through function
            if len(interim) == 0:
                flying_general = True
            else:
                flying_general = False

            if flying_general is True:
                return True

        # if the color to check is red
        if color == 'red':

            # nested for loop to step through board
            for row in range(0, 10):
                for col in range(0, 9):

                    # set current piece equal to the current space on the board
                    current_piece = self.__gameBoard.get_piece(row, col)

                    # if the current space is empty, continue to next loop iteration
                    if current_piece == '0':
                        continue

                    # if the current piece's color is black
                    if current_piece.get_color() == 'black':

                        # check if a move to take the general would be valid
                        valid_move = self.check_move(row, col, red_general_position[0], red_general_position[1])

                        # if said move is valid, return True
                        if valid_move is True:
                            return True

            # if all pieces are checked and none have general in check, return false
            return False

        # if the color to check is black
        elif color == 'black':

            # nested for loop to step through board
            for row in range(0, 10):
                for col in range(0, 9):

                    # set current piece equal to the current space on the board
                    current_piece = self.__gameBoard.get_piece(row, col)

                    # if the current space is empty, continue to next loop iteration
                    if current_piece == '0':
                        continue

                    # if the current piece's color is black
                    if current_piece.get_color() == 'red':

                        # check if a move to take the general would be valid
                        valid_move = self.check_move(row, col, black_general_position[0], black_general_position[1])

                        # if said move is valid, return True
                        if valid_move is True:
                            return True

            # if all pieces are checked and none have general in check, return false
            return False

        # if the color entered is not valid, return False
        else:
            return False

    def is_in_checkmate(self, color):
        """The is in checkmate function takes a color as the parameter. It works by calling the try all moves function
        with the color indicated. If that function returns true(there is a valid move available) it returns false.
        Else, it returns true"""

        if color == 'red':

            any_valid_moves = self.try_all_moves('red')

            if any_valid_moves is True:
                return False

            else:
                return True

        if color == 'black':

            any_valid_moves = self.try_all_moves('black')

            if any_valid_moves is True:
                return False

            else:
                return True

    def test_move(self, from_row, from_col, to_row, to_col):
        """The test move function takes the row and column values for the starting and ending position as parameters.
        It works by getting the item in the space at each position. It makes the move and then checks to see if the gen
        is in check. It returns the pieces to their position, then returns False if the general is in check. Else it
        returns False"""

        board = self.__gameBoard.get_board()

        moving_piece = self.__gameBoard.get_piece(from_row, from_col)
        target_piece = self.__gameBoard.get_piece(to_row, to_col)

        # make test move
        board[from_row][from_col] = '0'
        board[to_row][to_col] = moving_piece

        if moving_piece.get_color() == 'red':
            red_check = self.is_in_check('red')

            # move piece back
            board[from_row][from_col] = moving_piece
            board[to_row][to_col] = target_piece

            if red_check is True:
                return False
            else:
                return True

        elif moving_piece.get_color() == 'black':
            black_check = self.is_in_check('black')

            # move piece back
            board[from_row][from_col] = moving_piece
            board[to_row][to_col] = target_piece

            if black_check is True:
                return False
            else:
                return True

        else:
            # move piece back
            board[from_row][from_col] = moving_piece
            board[to_row][to_col] = target_piece
            return False


    def try_all_moves(self, color):
        """The try all moves function takes the color as a parameter. it creates a list to hold all the moves. It then
        steps through the board and checks to see if the color can make any valid moves that don't result in check. If
        the list is empty (no valid moves) it returns false. Else, it returns true."""

        move_list = []

        if color == 'red':

            # nested for loop to step through board
            for row in range(0, 10):
                for col in range(0, 9):

                    current_piece = self.__gameBoard.get_piece(row, col)

                    # if the space is not empty and it's the same color
                    if current_piece != '0' and current_piece.get_color() == 'red':

                        for x in range(0, 10):
                            for y in range(0, 9):
                                valid_move = self.check_move(row, col, x, y)

                                if valid_move is True:
                                    a_valid_move = self.test_move(row, col, x, y)
                                    if a_valid_move is True:
                                        move_list.append(a_valid_move)

                                else:
                                    continue

            if len(move_list) == 0:
                return False
            else:
                return True

        if color == 'black':

            # nested for loop to step through board
            for row in range(0, 10):
                for col in range(0, 9):

                    current_piece = self.__gameBoard.get_piece(row, col)

                    # if the space is not empty and it's the same color
                    if current_piece != '0' and current_piece.get_color() == 'black':

                        for x in range(0, 10):
                            for y in range(0, 9):
                                valid_move = self.check_move(row, col, x, y)

                                if valid_move is True:
                                    a_valid_move = self.test_move(row, col, x, y)
                                    if a_valid_move is True:
                                        move_list.append(a_valid_move)

                                else:
                                    continue

            if len(move_list) == 0:
                return False
            else:
                return True

    def make_move(self, pos_from, pos_to):
        """The make move takes the position from and to strings as parameters. It converts the strings to meaningful
        positions in the list. It checks if the move is valid and if so, it makes the move. Then it checks to see if
        the move put the moving pieces general in check. If so, it resets the position and returns false. Next it checks
        to see if the opposing side has valid moves. If not, it declares red the winner. If either side still has valid
        moves, it changes the current turn and returns"""

        # if the game is done, return false
        if self.__game_state != "UNFINISHED":
            return False

        # if the length of the from value is greater than 2 (aka if 10 is entered)
        if len(pos_from) > 2:

            # set from row position to the concatenated 1 & 2 positions (10) and subtracting one so it's the 9 index
            from_row_pos = int(pos_from[1] + pos_from[2]) - 1

        else:

            # from row position set to the int in the second part of the string
            from_row_pos = int(pos_from[1]) - 1

        # instantiate a variable to hold the integer that corresponds with the letter
        from_col_pos = int(self.__letters.index(pos_from[0]))

        # create variable for the piece to be moved
        moving_piece = self.__gameBoard.get_piece(from_row_pos, from_col_pos)

        # if the piece to be moved is just an empty space
        if moving_piece == '0':

            # return false since no piece is on indicated space
            return False

        # if the piece to be moved is not the current turn's color, return false
        if moving_piece.get_color() != self.__current_turn:
            return False

        # if the length of the 2 value is greater than 2 (aka if 10 is entered)
        if len(pos_to) > 2:

            # set to row position to the concatenated 1 & 2 positions (10) and subtracting one so it's the 9 index
            to_row_pos = int(pos_to[1] + pos_to[2]) - 1

        else:

            # to row position set to the int in the second part of the string
            to_row_pos = int(pos_to[1]) - 1

        # instantiate a variable to hold the integer that corresponds with the letter
        to_col_pos = int(self.__letters.index(pos_to[0]))

        valid_move = self.check_move(from_row_pos, from_col_pos, to_row_pos, to_col_pos)

        board = self.__gameBoard.get_board()

        # if the move is valid
        if valid_move is True:

            # change new space to the moving piece
            board[to_row_pos][to_col_pos] = moving_piece

            # change the starting position to empty space
            board[from_row_pos][from_col_pos] = '0'

            red_general_check = self.is_in_check('red')
            black_general_check = self.is_in_check('black')

            if moving_piece.get_color() == 'red':

                # check if move put own general in check. If so, return pieces to original position and return False
                if red_general_check is True:
                    board[from_row_pos][from_col_pos] = moving_piece
                    board[to_row_pos][to_col_pos] = '0'
                    return False

                if black_general_check is True:
                    if self.is_in_checkmate('black') is True:
                        self.__game_state = 'RED_WON'

                elif black_general_check is False:
                    if self.is_in_checkmate('black') is True:
                        self.__game_state = 'RED_WON'

            elif moving_piece.get_color() == 'black':

                # check if move put own general in check. If so, return pieces to original position and return False
                if black_general_check is True:
                    board[from_row_pos][from_col_pos] = moving_piece
                    board[to_row_pos][to_col_pos] = '0'
                    return False

                if red_general_check is True:
                    if self.is_in_checkmate('red') is True:
                        self.__game_state = 'BLACK_WON'

                elif red_general_check is False:
                    if self.is_in_checkmate('red') is True:
                        self.__game_state = 'BLACK_WON'

            # change the color of the current turn
            if self.__current_turn == 'red':
                self.__current_turn = 'black'

            elif self.__current_turn == 'black':
                self.__current_turn = 'red'

            return True

        else:
            return False

    def check_move(self, from_row_pos, from_col_pos, to_row_pos, to_col_pos):
        """Check move takes the row and column of the starting and ending positions. It uses get piece to check the
        type of piece before using that to call the subsequent check move for that piece."""

        moving_piece = self.__gameBoard.get_piece(from_row_pos, from_col_pos)

        if isinstance(moving_piece, General):
            return self.check_move_general(from_row_pos, from_col_pos, to_row_pos, to_col_pos, moving_piece)

        elif isinstance(moving_piece, Advisor):
            return self.check_move_advisor(from_row_pos, from_col_pos, to_row_pos, to_col_pos, moving_piece)

        elif isinstance(moving_piece, Elephant):
            return self.check_move_elephant(from_row_pos, from_col_pos, to_row_pos, to_col_pos, moving_piece)

        elif isinstance(moving_piece, Horse):
            return self.check_move_horse(from_row_pos, from_col_pos, to_row_pos, to_col_pos, moving_piece)

        elif isinstance(moving_piece, Chariot):
            return self.check_move_chariot(from_row_pos, from_col_pos, to_row_pos, to_col_pos, moving_piece)

        elif isinstance(moving_piece, Cannon):
            return self.check_move_cannon(from_row_pos, from_col_pos, to_row_pos, to_col_pos, moving_piece)

        elif isinstance(moving_piece, Soldier):
            return self.check_move_soldier(from_row_pos, from_col_pos, to_row_pos, to_col_pos, moving_piece)

    def check_move_general(self, from_row_pos, from_col_pos, to_row_pos, to_col_pos, moving_piece):
        """check move general takes the starting and ending position and the piece moving as parameters. It creates a
         variable to hold the targeted space. Then, based on the generals color, it ensures the move doesnt push the gen
         out of the castle. Next, it compares to see if the row or column is staying consistent. After that, it checks
         to see how the other parameter moved to determine which direction to move. Lastly, it checks to see if the
         desired position is empty or an opposing color. If so it returns true. Else, it returns False"""

        # instantiate variable to hold the target space
        target_space = self.__gameBoard.get_piece(to_row_pos, to_col_pos)

        # if moving piece is red
        if moving_piece.get_color() == 'red':

            # if the row position is outside the castle, return false
            if to_row_pos < 0 or to_row_pos > 2:
                return False

            # if the column position is outside the castle, return false
            elif to_col_pos < 3 or to_col_pos > 5:
                return False

            # if the move would not put the piece outside the castle
            else:
                # if x value is consistent
                if from_row_pos == to_row_pos:

                    # if the y position is the current position + 1
                    if to_col_pos == from_col_pos + 1:

                        # if the space is empty
                        if target_space == '0' or target_space.get_color() == 'black':
                            return True

                    # if the y position is the current position - 1
                    elif to_col_pos == from_col_pos - 1:

                        # if the space is empty
                        if target_space == '0' or target_space.get_color() == 'black':
                            return True

                    # if the move is not an increment of 1, return false
                    else:
                        return False

                # If the y value is consistent
                elif from_col_pos == to_col_pos:

                    # if the x position is the current position + 1
                    if to_row_pos == from_row_pos + 1:

                        # if the space is empty
                        if target_space == '0' or target_space.get_color() == 'black':
                            return True

                    # if the x position is the current position - 1
                    elif to_row_pos == from_row_pos - 1:

                        # if the space is empty
                        if target_space == '0' or target_space.get_color() == 'black':
                            return True

                    # if the move is not an increment of 1, return false
                    else:
                        return False

                # if move is not valid
                else:
                    return False

        elif moving_piece.get_color() == 'black':

            # if the row position is outside the castle, return false
            if to_row_pos < 7 or to_row_pos > 9:
                return False

            # if the column position is outside the castle, return false
            elif to_col_pos < 3 or to_col_pos > 5:
                return False

            else:

                # if x value is consistent
                if from_row_pos == to_row_pos:

                    # if the y position is the current position + 1
                    if to_col_pos == from_col_pos + 1:

                        # if the space is empty
                        if target_space == '0' or target_space.get_color() == 'red':
                            return True

                    # if the y position is the current position - 1
                    elif to_col_pos == from_col_pos - 1:

                        # if the space is empty
                        if target_space == '0' or target_space.get_color() == 'red':
                            return True

                    # if the move is not an increment of 1, return false
                    else:
                        return False

                # If the y value is consistent
                elif from_col_pos == to_col_pos:

                    # if the x position is the current position + 1
                    if to_row_pos == from_row_pos + 1:

                        # if the space is empty
                        if target_space == '0' or target_space.get_color() == 'red':
                            return True

                    # if the x position is the current position - 1
                    elif to_row_pos == from_row_pos - 1:

                        # if the space is empty
                        if target_space == '0' or target_space.get_color() == 'red':
                            return True

                    # if the move is not an increment of 1, return false
                    else:
                        return False

                # if move is not valid
                else:
                    return False

    def check_move_advisor(self, from_row_pos, from_col_pos, to_row_pos, to_col_pos, moving_piece):
        """check move advisor takes the starting and ending position and the piece moving as parameters. It runs the
         same check as general to ensure pieces stay in the castle. Next it checks to see how the row and column changed
          in the to position to determine which way to go. If it is not diagonal, it returns false. If the target pos is
          empty or the opposite color, it returns True"""

        # instantiate variable to hold the targeted space
        target_space = self.__gameBoard.get_piece(to_row_pos, to_col_pos)

        # if moving piece is red
        if moving_piece.get_color() == 'red':

            # if the row position is outside the castle, return false
            if to_row_pos < 0 or to_row_pos > 2:
                return False

            # if the column position is outside the castle, return false
            elif to_col_pos < 3 or to_col_pos > 5:
                return False

            else:

                # checking the diagonal position row + 1 | col - 1
                if to_row_pos == from_row_pos + 1 and to_col_pos == from_col_pos - 1:


                    # if the position is empty
                    if target_space == '0':
                        return True

                    # if the position is held by opposing color
                    elif target_space.get_color() == 'black':
                        return True

                    else:
                        return False


                # checking the diagonal position row + 1 | col + 1
                elif to_row_pos == from_row_pos + 1 and to_col_pos == from_col_pos + 1:

                    # if the position is empty
                    if target_space == '0':
                        return True

                    elif target_space.get_color() == 'black':
                        return True

                # checking the diagonal position row - 1 | col - 1
                elif to_row_pos == from_row_pos - 1 and to_col_pos == from_col_pos - 1:

                    # if the position is empty
                    if target_space == '0':
                        return True

                    elif target_space.get_color() == 'black':
                        return True

                    else:
                        return False

                # checking the diagonal position row - 1 | col + 1
                elif to_row_pos == from_row_pos - 1 and to_col_pos == from_col_pos + 1:

                    # if the position is empty
                    if target_space == '0':
                        return True

                    elif target_space.get_color() == 'black':
                        return True

                    else:
                        return False

                # if move is not valid
                else:
                    return False

        # if moving piece is black
        if moving_piece.get_color() == 'black':

            # if the row position is outside the castle, return false
            if to_row_pos < 7 or to_row_pos > 9:
                return False

            # if the column position is outside the castle, return false
            elif to_col_pos < 3 or to_col_pos > 5:
                return False

            else:

                # checking the diagonal position row + 1 | col - 1
                if to_row_pos == from_row_pos + 1 and to_col_pos == from_col_pos - 1:

                    # if the position is empty
                    if target_space == '0':
                        return True

                    elif target_space.get_color() == 'red':
                        return True

                    else:
                        return False

                # checking the diagonal position row + 1 | col + 1
                elif to_row_pos == from_row_pos + 1 and to_col_pos == from_col_pos + 1:

                    # if the position is empty
                    if target_space == '0':
                        return True

                    elif target_space.get_color() == 'red':
                        return True

                    else:
                        return False

                # checking the diagonal position row - 1 | col - 1
                elif to_row_pos == from_row_pos - 1 and to_col_pos == from_col_pos - 1:

                    # if the position is empty
                    if target_space == '0':
                        return True

                    elif target_space.get_color() == 'red':
                        return True

                    else:
                        return False

                # checking the diagonal position row - 1 | col + 1
                elif to_row_pos == from_row_pos - 1 and to_col_pos == from_col_pos + 1:

                    # if the position is empty
                    if target_space == '0':
                        return True

                    elif target_space.get_color() == 'red':
                        return True

                    else:
                        return False

                # if move is not valid
                else:
                    return False

    def check_move_elephant(self, from_row_pos, from_col_pos, to_row_pos, to_col_pos, moving_piece):
        """check move elephant takes the starting and ending position and the piece moving as parameters. it works like
         the general check but instead of checking to remain in the castle, it checks to ensure the elephant doesn't
         cross the river. Since it moves 2 diagonal spaces at a time, it also checks to see if the interim step is
         occupied. If so, the move isn't valid. Else if the move is valid (empty or opposite color position) it ret.
         True"""

        # instantiate variable to hold the targeted space
        target_space = self.__gameBoard.get_piece(to_row_pos, to_col_pos)

        # if color is red
        if moving_piece.get_color() == 'red':

            # check if row position would cross the river
            if to_row_pos > 4:
                return False

            # check diagonal position, row + 2 | column - 2
            if to_row_pos == from_row_pos + 2 and to_col_pos == from_col_pos - 2:

                # check if the intermediate position is empty, return false if it isn't
                if self.__gameBoard.get_piece(from_row_pos + 1, from_col_pos - 1) != '0':
                    return False

                # if the targeted space is empty, return true
                if target_space == '0':
                    return True

                elif target_space.get_color() == 'black':
                    return True

                else:
                    return False

            # check diagonal position, row + 2 | column + 2
            elif to_row_pos == from_row_pos + 2 and to_col_pos == from_col_pos + 2:

                # check if the intermediate position is empty, return false if it isn't
                if self.__gameBoard.get_piece(from_row_pos + 1, from_col_pos + 1) != '0':
                    return False

                # if the targeted space is empty, return true
                if target_space == '0':
                    return True

                elif target_space.get_color() == 'black':
                    return True

                else:
                    return False

            # check diagonal position, row - 2 | column - 2
            elif to_row_pos == from_row_pos - 2 and to_col_pos == from_col_pos - 2:

                # check if the intermediate position is empty, return false if it isn't
                if self.__gameBoard.get_piece(from_row_pos - 1, from_col_pos - 1) != '0':
                    return False

                # if the targeted space is empty, return true
                if target_space == '0':
                    return True

                elif target_space.get_color() == 'black':
                    return True

                else:
                    return False

            # check diagonal position, row - 2 | column + 2
            elif to_row_pos == from_row_pos - 2 and to_col_pos == from_col_pos + 2:

                # check if the intermediate position is empty, return false if it isn't
                if self.__gameBoard.get_piece(from_row_pos - 1, from_col_pos + 1) != '0':
                    return False

                # if the targeted space is empty, return true
                if target_space == '0':
                    return True

                elif target_space.get_color() == 'black':
                    return True

                else:
                    return False

            # if move is not valid
            else:
                return False

        # if color is black
        if moving_piece.get_color() == 'black':

            # if the piece would cross the river
            if to_row_pos < 5:
                return False

            # check diagonal position, row + 2 | column - 2
            if to_row_pos == from_row_pos + 2 and to_col_pos == from_col_pos - 2:

                # check if the intermediate position is empty, return false if it isn't
                if self.__gameBoard.get_piece(from_row_pos + 1, from_col_pos - 1) != '0':
                    return False

                # if the targeted space is empty, return true
                if target_space == '0':
                    return True

                # if the targeted space is an opposing piece, return True
                elif target_space.get_color() == 'red':
                    return True

                else:
                    return False

            # check diagonal position, row + 2 | column + 2
            elif to_row_pos == from_row_pos + 2 and to_col_pos == from_col_pos + 2:

                # check if the intermediate position is empty, return false if it isn't
                if self.__gameBoard.get_piece(from_row_pos + 1, from_col_pos + 1) != '0':
                    return False

                # if the targeted space is empty, return true
                if target_space == '0':
                    return True

                # if the targeted space is an opposing piece, return True
                elif target_space.get_color() == 'black':
                    return True

                else:
                    return False

            # check diagonal position, row - 2 | column - 2
            elif to_row_pos == from_row_pos - 2 and to_col_pos == from_col_pos - 2:

                    # check if the intermediate position is empty, return false if it isn't
                    if self.__gameBoard.get_piece(from_row_pos - 1, from_col_pos - 1) != '0':
                        return False

                    # if the targeted space is empty, return true
                    if target_space == '0':
                        return True

                    # if the targeted space is an opposing piece, return True
                    elif target_space.get_color() == 'black':
                        return True

                    else:
                        return False

            # check diagonal position, row - 2 | column + 2
            elif to_row_pos == from_row_pos - 2 and to_col_pos == from_col_pos + 2:

                    # check if the intermediate position is empty, return false if it isn't
                    if self.__gameBoard.get_piece(from_row_pos - 1, from_col_pos + 1) != '0':
                        return False

                    # if the targeted space is empty, return true
                    if target_space == '0':
                        return True

                    # if the targeted space is an opposing piece, return True
                    elif target_space.get_color() == 'black':
                        return True

                    else:
                        return False

            else:
                return False

    def check_move_horse(self, from_row_pos, from_col_pos, to_row_pos, to_col_pos, moving_piece):
        """check move horse takes the starting and ending position and the piece moving as parameters. It uses the end
        pos to determine which way the horse is moving Like the elephant, it checks that first interim step for a piece
        and returns false if it isn't empty. Else it checks the target location to see if it's empty or an opposite col.
        if so, it returns True"""

        # instantiate variable to hold the targeted space
        target_space = self.__gameBoard.get_piece(to_row_pos, to_col_pos)

        # if color is red
        if moving_piece.get_color() == 'red':

            # check piece move row - 2| col + 1
            if to_row_pos == from_row_pos - 2 and to_col_pos == from_col_pos + 1:

                # check if the horse is blocked. IF it is, return False
                if self.__gameBoard.get_piece(from_row_pos - 1, from_col_pos) != '0':
                    return False

                # if the target space is empty, return True
                if target_space == '0':
                    return True

                # if the target space is an opposing piece, return True
                elif target_space.get_color() == 'black':
                    return True

                else:
                    return False
            # check piece move row - 2| col - 1
            elif to_row_pos == from_row_pos - 2 and to_col_pos == from_col_pos - 1:

                # check if the horse is blocked. IF it is, return False
                if self.__gameBoard.get_piece(from_row_pos - 1, from_col_pos) != '0':
                    return False

                # if the target space is empty, return True
                if target_space == '0':
                    return True

                # if the target space is an opposing piece, return True
                elif target_space.get_color() == 'black':
                    return True

                else:
                    return False

            # check piece move row + 2| col - 1
            elif to_row_pos == from_row_pos + 2 and to_col_pos == from_col_pos - 1:

                # check if the horse is blocked. IF it is, return False
                if self.__gameBoard.get_piece(from_row_pos + 1, from_col_pos) != '0':
                    return False

                # if the target space is empty, return True
                if target_space == '0':
                    return True

                # if the target space is an opposing piece, return True
                elif target_space.get_color() == 'black':
                    return True

                else:
                    return False

            # check piece move row + 2| col + 1
            elif to_row_pos == from_row_pos + 2 and to_col_pos == from_col_pos + 1:

                # check if the horse is blocked. IF it is, return False
                if self.__gameBoard.get_piece(from_row_pos + 1, from_col_pos) != '0':
                    return False

                # if the target space is empty, return True
                if target_space == '0':
                    return True

                # if the target space is an opposing piece, return True
                elif target_space.get_color() == 'black':
                    return True

                else:
                    return False

            # check piece move col - 2 | row - 1
            elif to_col_pos == from_col_pos - 2 and to_row_pos == from_row_pos - 1:

                # check if the horse is blocked. IF it is, return False
                if self.__gameBoard.get_piece(from_row_pos, from_col_pos - 1) != '0':
                    return False

                # if the target space is empty, return True
                if target_space == '0':
                    return True

                # if the target space is an opposing piece, return True
                elif target_space.get_color() == 'black':
                    return True

                else:
                    return False

            # check piece move col - 2 | row + 1
            elif to_col_pos == from_col_pos - 2 and to_row_pos == from_row_pos + 1:

                # check if the horse is blocked. IF it is, return False
                if self.__gameBoard.get_piece(from_row_pos, from_col_pos - 1) != '0':
                    return False

                # if the target space is empty, return True
                if target_space == '0':
                    return True

                # if the target space is an opposing piece, return True
                elif target_space.get_color() == 'black':
                    return True

                else:
                    return False

            # check piece move col + 2 | row - 1
            elif to_col_pos == from_col_pos + 2 and to_row_pos == from_row_pos - 1:

                # check if the horse is blocked. IF it is, return False
                if self.__gameBoard.get_piece(from_row_pos, from_col_pos + 1) != '0':
                    return False

                # if the target space is empty, return True
                if target_space == '0':
                    return True

                # if the target space is an opposing piece, return True
                elif target_space.get_color() == 'black':
                    return True

                else:
                    return False

            # check piece move col + 2 | row + 1
            elif to_col_pos == from_col_pos + 2 and to_row_pos == from_row_pos + 1:

                # check if the horse is blocked. IF it is, return False
                if self.__gameBoard.get_piece(from_row_pos, from_col_pos + 1) != '0':
                    return False

                # if the target space is empty, return True
                if target_space == '0':
                    return True

                # if the target space is an opposing piece, return True
                elif target_space.get_color() == 'black':
                    return True

                else:
                    return False

            # if move is not valid
            else:
                return False

        # if color is black
        if moving_piece.get_color() == 'black':

            # check piece move row - 2| col + 1
            if to_row_pos == from_row_pos - 2 and to_col_pos == from_col_pos + 1:

                # check if the horse is blocked. IF it is, return False
                if self.__gameBoard.get_piece(from_row_pos - 1, from_col_pos) != '0':
                    return False

                # if the target space is empty, return True
                if target_space == '0':
                    return True

                # if the target space is an opposing piece, return True
                elif target_space.get_color() == 'red':
                    return True

                else:
                    return False
            # check piece move row - 2| col - 1
            elif to_row_pos == from_row_pos - 2 and to_col_pos == from_col_pos - 1:

                # check if the horse is blocked. IF it is, return False
                if self.__gameBoard.get_piece(from_row_pos - 1, from_col_pos) != '0':
                    return False

                # if the target space is empty, return True
                if target_space == '0':
                    return True

                # if the target space is an opposing piece, return True
                elif target_space.get_color() == 'red':
                    return True

                else:
                    return False

            # check piece move row + 2| col - 1
            elif to_row_pos == from_row_pos + 2 and to_col_pos == from_col_pos - 1:

                # check if the horse is blocked. IF it is, return False
                if self.__gameBoard.get_piece(from_row_pos + 1, from_col_pos) != '0':
                    return False

                # if the target space is empty, return True
                if target_space == '0':
                    return True

                # if the target space is an opposing piece, return True
                elif target_space.get_color() == 'red':
                    return True

                else:
                    return False

            # check piece move row + 2| col + 1
            elif to_row_pos == from_row_pos + 2 and to_col_pos == from_col_pos + 1:

                # check if the horse is blocked. IF it is, return False
                if self.__gameBoard.get_piece(from_row_pos + 1, from_col_pos) != '0':
                    return False

                # if the target space is empty, return True
                if target_space == '0':
                    return True

                # if the target space is an opposing piece, return True
                elif target_space.get_color() == 'red':
                    return True

                else:
                    return False

            # check piece move col - 2 | row - 1
            elif to_col_pos == from_col_pos - 2 and to_row_pos == from_row_pos - 1:

                # check if the horse is blocked. IF it is, return False
                if self.__gameBoard.get_piece(from_row_pos, from_col_pos - 1) != '0':
                    return False

                # if the target space is empty, return True
                if target_space == '0':
                    return True

                # if the target space is an opposing piece, return True
                elif target_space.get_color() == 'red':
                    return True

                else:
                    return False

            # check piece move col - 2 | row + 1
            elif to_col_pos == from_col_pos - 2 and to_row_pos == from_row_pos + 1:

                # check if the horse is blocked. IF it is, return False
                if self.__gameBoard.get_piece(from_row_pos, from_col_pos - 1) != '0':
                    return False

                # if the target space is empty, return True
                if target_space == '0':
                    return True

                # if the target space is an opposing piece, return True
                elif target_space.get_color() == 'red':
                    return True

                else:
                    return False

            # check piece move col + 2 | row - 1
            elif to_col_pos == from_col_pos + 2 and to_row_pos == from_row_pos - 1:

                # check if the horse is blocked. IF it is, return False
                if self.__gameBoard.get_piece(from_row_pos, from_col_pos + 1) != '0':
                    return False

                # if the target space is empty, return True
                if target_space == '0':
                    return True

                # if the target space is an opposing piece, return True
                elif target_space.get_color() == 'red':
                    return True

                else:
                    return False

            # check piece move col + 2 | row + 1
            elif to_col_pos == from_col_pos + 2 and to_row_pos == from_row_pos + 1:

                # check if the horse is blocked. IF it is, return False
                if self.__gameBoard.get_piece(from_row_pos, from_col_pos + 1) != '0':
                    return False

                # if the target space is empty, return True
                if target_space == '0':
                    return True

                # if the target space is an opposing piece, return True
                elif target_space.get_color() == 'red':
                    return True

                else:
                    return False

            # if move is not valid
            else:
                return False

    def check_move_chariot(self, from_row_pos, from_col_pos, to_row_pos, to_col_pos, moving_piece):
        """check move chariot takes the starting and ending position and the piece moving as parameters. It works by
         first determining if the row or column is changing. Next, it uses a for loop to step through the range
         between the lesser position and greater position. If there is anything obstructing from the start to end loc.
          it returns false. Then it checks the target location and if the space is valid, it returns true."""

        target_space = self.__gameBoard.get_piece(to_row_pos, to_col_pos)

        if moving_piece.get_color() == 'red':

            # if the row position is consistent
            if from_row_pos == to_row_pos:

                # if the piece is moving right
                if to_col_pos > from_col_pos:

                    # for loop to step through all the interim pieces
                    for x in range(from_col_pos + 1, to_col_pos):

                        # if statement to check if any of the spaces are not empty
                        if self.__gameBoard.get_piece(from_row_pos, x) != '0':
                            return False

                    # if the target space is empty, return true
                    if target_space == '0':
                            return True

                    # if the target space is an opposing color
                    elif target_space.get_color() == 'black':
                            return True

                    # if move isn't valid
                    else:
                        return False

                # if the piece is moving left
                elif to_col_pos < from_col_pos:

                    # for loop to step through all the interim pieces
                    for x in range(to_col_pos + 1, from_col_pos):

                        # if statement to check if any of the spaces are not empty
                        if self.__gameBoard.get_piece(from_row_pos, x) != '0':
                            return False

                    # if the target space is empty, return true
                    if target_space == '0':
                            return True

                    # if the target space is an opposing color
                    elif target_space.get_color() == 'black':
                            return True

                    # if move isn't valid
                    else:
                        return False

            # if the column position is consistent
            elif from_col_pos == to_col_pos:

                # if the piece is moving up
                if to_row_pos > from_row_pos:

                    # for loop to step through all the interim pieces
                    for x in range(from_row_pos + 1, to_row_pos):

                        # if statement to check if any of the spaces are not empty
                        if self.__gameBoard.get_piece(x, to_col_pos) != '0':
                            return False

                    # if the target space is empty, return true
                    if target_space == '0':
                        return True

                    # if the target space is an opposing color
                    elif target_space.get_color() == 'black':
                        return True

                    # if move isn't valid
                    else:
                        return False

                # if the piece is moving down
                elif to_row_pos < from_row_pos:

                    # for loop to step through all the interim pieces
                    for x in range(to_row_pos + 1, from_row_pos):

                        # if statement to check if any of the spaces are not empty
                        if self.__gameBoard.get_piece(x, to_col_pos):
                            return False

                    # if the target space is empty, return true
                    if target_space == '0':
                         return True

                    # if the target space is an opposing color
                    elif target_space.get_color() == 'black':
                        return True

                    # if move isn't valid
                    else:
                        return False

            # if the move isn't valid
            else:
                return False

        if moving_piece.get_color() == 'black':

            # if the row position is consistent
            if from_row_pos == to_row_pos:

                # if the piece is moving right
                if to_col_pos > from_col_pos:

                    # for loop to step through all the interim pieces
                    for x in range(from_col_pos + 1, to_col_pos):

                        # if statement to check if any of the spaces are not empty
                        if self.__gameBoard.get_piece(from_row_pos, x) != '0':
                            return False

                    # if the target space is empty, return true
                    if target_space == '0':
                        return True

                    # if the target space is an opposing color
                    elif target_space.get_color() == 'red':
                        return True

                    # if move isn't valid
                    else:
                        return False

                        # if the piece is moving left
                elif to_col_pos < from_col_pos:

                    # for loop to step through all the interim pieces
                    for x in range(to_col_pos + 1, from_col_pos):

                        # if statement to check if any of the spaces are not empty
                        if self.__gameBoard.get_piece(from_row_pos, x) != '0':
                            return False

                    # if the target space is empty, return true
                    if target_space == '0':
                        return True

                    # if the target space is an opposing color
                    elif target_space.get_color() == 'red':
                        return True

                    # if move isn't valid
                    else:
                        return False

            # if the column position is consistent
            elif from_col_pos == to_col_pos:

                # if the piece is moving up
                if to_row_pos > from_row_pos:

                    # for loop to step through all the interim pieces
                    for x in range(from_row_pos + 1, to_row_pos):

                        # if statement to check if any of the spaces are not empty
                        if self.__gameBoard.get_piece(x, to_col_pos) != '0':
                            return False

                    # if the target space is empty, return true
                    if target_space == '0':
                        return True

                    # if the target space is an opposing color
                    elif target_space.get_color() == 'red':
                        return True

                    # if move isn't valid
                    else:
                        return False

                # if the piece is moving down
                elif to_row_pos < from_row_pos:

                    # for loop to step through all the interim pieces
                    for x in range(to_row_pos + 1, from_row_pos):

                        # if statement to check if any of the spaces are not empty
                        if self.__gameBoard.get_piece(x, to_col_pos) != '0':
                            return False

                    # if the target space is empty, return true
                    if target_space == '0':
                        return True

                    # if the target space is an opposing color
                    elif target_space.get_color() == 'red':
                        return True

                    # if move isn't valid
                    else:
                        return False

            # if the move isn't valid
            else:
                return False

    def check_move_cannon(self, from_row_pos, from_col_pos, to_row_pos, to_col_pos, moving_piece):
        """check move cannon takes the starting and ending position and the piece moving as parameters. It works like
         the chariot but has the added step of checking captures with a single interim piece. To do this, it creates a
         list and appends it for each value between the start and end location. If the end point is blank and the list
         is empty, the move is true. Else if the list has exactly one item in it and the target space is an opposing pc
         it's a valid capture. Else it returns False"""

        # instantiate variable for the target space
        target_space = self.__gameBoard.get_piece(to_row_pos, to_col_pos)

        # instantiate list to hold interim spaces
        interim_spaces = []

        # if piece color is red
        if moving_piece.get_color() == 'red':

            # if the row position is consistent
            if from_row_pos == to_row_pos:

                # if the piece is moving right
                if to_col_pos > from_col_pos:

                    # for loop to step through all the interim pieces
                    for x in range(from_col_pos + 1, to_col_pos):

                        # if statement to check if any of the spaces are not empty
                        if self.__gameBoard.get_piece(from_row_pos, x) != '0':
                            interim_spaces.append(self.__gameBoard.get_piece(from_row_pos, x))

                    if target_space == '0':
                        # if there are no pieces between the cannon and it's target location
                        if len(interim_spaces) == 0:
                            return True
                        else:
                            return False

                    # if there is exactly one piece between the cannon and targeted space
                    elif len(interim_spaces) == 1 and target_space.get_color() == 'black':
                        return True

                    # if move isn't valid
                    else:
                        return False

                # if the piece is moving left
                elif to_col_pos < from_col_pos:

                    # for loop to step through all the interim pieces
                    for x in range(to_col_pos + 1, from_col_pos):

                        # if statement to check if any of the spaces are not empty
                        if self.__gameBoard.get_piece(from_row_pos, x) != '0':
                            interim_spaces.append(self.__gameBoard.get_piece(from_row_pos, x))

                    if target_space == '0':
                        if len(interim_spaces) == 0:
                            return True
                        else:
                            return False

                    # if there is exactly one piece between the cannon and targeted space
                    elif len(interim_spaces) == 1 and target_space.get_color() == 'black':
                        return True

                    else:
                        return False

            # if the column position is consistent
            elif from_col_pos == to_col_pos:

                # if the piece is moving up
                if to_row_pos > from_row_pos:

                    # for loop to step through all the interim pieces
                    for x in range(from_row_pos + 1, to_row_pos):

                        # if statement to check if any of the spaces are not empty
                        if self.__gameBoard.get_piece(x, to_col_pos) != '0':
                            interim_spaces.append(self.__gameBoard.get_piece(x, to_col_pos))

                    if target_space == '0':
                        # if there are no pieces between the cannon and it's target location
                        if len(interim_spaces) == 0:
                            return True

                        else:
                            return False

                    # if there is exactly one piece between the cannon and targeted space
                    elif len(interim_spaces) == 1 and target_space.get_color() == 'black':
                        return True

                    else:
                        return False

                # if the piece is moving down
                elif to_row_pos < from_row_pos:

                    # for loop to step through all the interim pieces
                    for x in range(to_row_pos + 1, from_row_pos):

                        # if statement to check if any of the spaces are not empty
                        if self.__gameBoard.get_piece(x, to_col_pos) != '0':
                            interim_spaces.append(self.__gameBoard.get_piece(x, to_col_pos))

                    if target_space == '0':
                        # if there are no pieces between the cannon and it's target location
                        if len(interim_spaces) == 0:

                            return True

                        else:
                            return False

                    # if there is exactly one piece between the cannon and targeted space
                    elif len(interim_spaces) == 1 and target_space.get_color() == 'black':
                        return True

                    else:
                        return False

            # if the move isn't valid
            else:
                return False

        elif moving_piece.get_color() == 'black':

            # if the row position is consistent
            if from_row_pos == to_row_pos:

                # if the piece is moving right
                if to_col_pos > from_col_pos:

                    # for loop to step through all the interim pieces
                    for x in range(from_col_pos + 1, to_col_pos):

                        # if statement to check if any of the spaces are not empty
                        if self.__gameBoard.get_piece(from_row_pos, x) != '0':
                            interim_spaces.append(self.__gameBoard.get_piece(from_row_pos, x))

                    if target_space == '0':
                        # if there are no pieces between the cannon and it's target location
                        if len(interim_spaces) == 0:

                            return True

                        else:
                            return False

                    # if there is exactly one piece between the cannon and targeted space
                    elif len(interim_spaces) == 1 and target_space.get_color() == 'red':
                        return True

                    # if move isn't valid
                    else:
                        return False

                # if the piece is moving left
                elif to_col_pos < from_col_pos:

                    # for loop to step through all the interim pieces
                    for x in range(to_col_pos + 1, from_col_pos):

                        # if statement to check if any of the spaces are not empty
                        if self.__gameBoard.get_piece(from_row_pos, x) != '0':
                            interim_spaces.append(self.__gameBoard.get_piece(from_row_pos, x))

                    if target_space == '0':
                        # if there are no pieces between the cannon and it's target location
                        if len(interim_spaces) == 0:
                            return True
                        else:
                            return False

                    # if there is exactly one piece between the cannon and targeted space
                    elif len(interim_spaces) == 1 and target_space.get_color() == 'red':
                        return True

                    else:
                        return False

            # if the column position is consistent
            elif from_col_pos == to_col_pos:

                # if the piece is moving up
                if to_row_pos > from_row_pos:

                    # for loop to step through all the interim pieces
                    for x in range(from_row_pos + 1, to_row_pos):

                        # if statement to check if any of the spaces are not empty
                        if self.__gameBoard.get_piece(x, to_col_pos) != '0':
                            interim_spaces.append(self.__gameBoard.get_piece(x, to_col_pos))

                    if target_space == '0':

                        # if there are no pieces between the cannon and it's target location
                        if len(interim_spaces) == 0:
                            return True
                        else:
                            return False

                    # if there is exactly one piece between the cannon and targeted space
                    elif len(interim_spaces) == 1 and target_space.get_color() == 'red':
                        return True
                    else:
                        return False

                # if the piece is moving down
                elif to_row_pos < from_row_pos:

                    # for loop to step through all the interim pieces
                    for x in range(to_row_pos + 1, from_row_pos):

                        # if statement to check if any of the spaces are not empty
                        if self.__gameBoard.get_piece(x, to_col_pos) != '0':
                            interim_spaces.append(self.__gameBoard.get_piece(x, to_col_pos))

                    if target_space == '0':

                        # if there are no pieces between the cannon and it's target location
                        if len(interim_spaces) == 0:
                            return True
                        else:
                            return False

                    # if there is exactly one piece between the cannon and targeted space
                    elif len(interim_spaces) == 1 and target_space.get_color() == 'red':
                        return True

                    else:
                        return False

            # if the move isn't valid
            else:
                return False

        else:
            return False

    def check_move_soldier(self, from_row_pos, from_col_pos, to_row_pos, to_col_pos, moving_piece):
        """check move Soldier takes the starting and ending position and the piece moving as parameters. It first checks
         to see if the soldier has crossed the river(by checking the starting row). If so, it offers the ability to move
         left, right, or forward. If not, it only allows the soldier to move forward. It does this similarly to other
         pieces by checking to see what has changed between the row/column values. If the move is a valid direction
         and the space is empty or occupied by enemy piece, it returns True"""

        # instantiate variable for the target space
        target_space = self.__gameBoard.get_piece(to_row_pos, to_col_pos)

        if moving_piece.get_color() == 'red':

            # if piece has just crossed the river
            if from_row_pos > 4:

                # if horizontal move to the right
                if from_row_pos == to_row_pos and to_col_pos == from_col_pos + 1:

                    # if the space is empty
                    if target_space == '0':
                        return True

                    # if the space is a piece of opposing color
                    elif target_space.get_color() == 'black':
                        return True

                    else:
                        return False

                # if horizontal move to the left
                elif from_row_pos == to_row_pos and to_col_pos == from_col_pos - 1:

                    # if the space is empty
                    if target_space == '0':
                        return True

                    # if the space is a piece of opposing color
                    elif target_space.get_color() == 'black':
                        return True

                    else:
                        return False

                # if move is straight forward
                elif to_row_pos == from_row_pos + 1 and to_col_pos == from_col_pos:

                    # if the space is empty
                    if target_space == '0':
                        return True

                    # if the space is a piece of opposing color
                    elif target_space.get_color() == 'black':
                        return True

                    else:
                        return False

            # if the soldier moves forward one space
            if to_row_pos == from_row_pos + 1 and to_col_pos == from_col_pos:

                # if the space is empty
                if target_space == '0':
                    return True

                # if the space is a piece of opposing color
                elif target_space.get_color() == 'black':
                    return True

                else:
                    return False

            # if the move is not valid
            else:
                return False

        if moving_piece.get_color() == 'black':

            # if piece has just crossed the river
            if from_row_pos < 5:

                # if horizontal move to the right
                if from_row_pos == to_row_pos and to_col_pos == from_col_pos + 1:

                    # if the space is empty
                    if target_space == '0':
                        return True

                    # if the space is a piece of opposing color
                    elif target_space.get_color() == 'red':
                        return True

                    else:
                        return False

                # if horizontal move to the left
                elif from_row_pos == to_row_pos and to_col_pos == from_col_pos - 1:

                    # if the space is empty
                    if target_space == '0':
                        return True

                    # if the space is a piece of opposing color
                    elif target_space.get_color() == 'red':
                        return True

                    else:
                        return False

                # if the soldier moves forward one space
                elif to_row_pos == from_row_pos - 1 and to_col_pos == from_col_pos:

                    # if the space is empty
                    if target_space == '0':
                        return True

                    # if the space is a piece of opposing color
                    elif target_space.get_color() == 'red':
                        return True

                    else:
                        return False

            # if the soldier is moving straight forward
            if to_row_pos == from_row_pos - 1 and to_col_pos == from_col_pos:

                    # if the space is empty
                    if target_space == '0':
                        return True

                    # if the space is a piece of opposing color
                    elif target_space.get_color() == 'red':
                        return True

                    else:
                        return False

            # if move is not valid
            else:
                return False


class Piece:
    """Piece parent class. Initializes with a color and has a function to return that color"""

    def __init__(self, color):
        self.__color = color

    def get_color(self):
        return self.__color


class General(Piece):
    """General Child class"""

    def __init__(self, color):
        super().__init__(color)


class Advisor(Piece):
    """Advisor child class. Inherits members and functionality from Piece class"""

    def __init__(self, color):
        super().__init__(color)


class Elephant(Piece):
    """Elephant child class. Inherits members and functionality from Piece class"""

    def __init__(self, color):
        super().__init__(color)


class Horse(Piece):
    """Horse child class. Inherits members and functionality from Piece class"""

    def __init__(self, color):
        super().__init__(color)


class Chariot(Piece):
    """Chariot child class. Inherits members and functionality from Piece class"""

    def __init__(self, color):
        super().__init__(color)


class Cannon(Piece):
    """Cannon child class. Inherits members and functionality from Piece class"""

    def __init__(self, color):
        super().__init__(color)


class Soldier(Piece):
    """Soldier child class. Inherits members and functionality from Piece class"""

    def __init__(self, color):
        super().__init__(color)


if __name__ == '__main__':
    game = XiangqiGame()
    print(game.make_move('b3', 'e3'))
    print(game.make_move('h8', 'e8'))
    print(game.make_move('h3', 'h6'))
    print(game.make_move('b8', 'b4'))
    print(game.make_move('e3', 'e7'))
    print(game.make_move('e8', 'e4'))
    print(game.make_move('h6', 'e6'))
    print(game.get_game_state())

