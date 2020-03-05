# Author: Don Hurst
# Date: 02/22/2020
# Description:

from typing import List


class Board:
    """The Board class """

    def __init__(self):
        """"""

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
        self.__gameBoard[3][0] = Soldier('black')
        self.__gameBoard[3][2] = Soldier('black')
        self.__gameBoard[3][4] = Soldier('black')
        self.__gameBoard[3][6] = Soldier('black')
        self.__gameBoard[3][8] = Soldier('black')
        self.__gameBoard[6][0] = Soldier('red')
        self.__gameBoard[6][2] = Soldier('red')
        self.__gameBoard[6][4] = Soldier('red')
        self.__gameBoard[6][6] = Soldier('red')
        self.__gameBoard[6][8] = Soldier('red')

        # initialize Cannon Piece Placement
        self.__gameBoard[2][1] = Cannon('black')
        self.__gameBoard[2][7] = Cannon('black')
        self.__gameBoard[7][1] = Cannon('red')
        self.__gameBoard[7][7] = Cannon('red')

        # initialize Chariot Piece Placement
        self.__gameBoard[0][0] = Chariot('black')
        self.__gameBoard[0][8] = Chariot('black')
        self.__gameBoard[9][0] = Chariot('red')
        self.__gameBoard[9][8] = Chariot('red')

        # Initialize Horse Piece Placement
        self.__gameBoard[0][1] = Horse('black')
        self.__gameBoard[0][7] = Horse('black')
        self.__gameBoard[9][1] = Horse('red')
        self.__gameBoard[9][7] = Horse('red')

        # Initialize Elephant Piece Placement
        self.__gameBoard[0][2] = Elephant('black')
        self.__gameBoard[0][6] = Elephant('black')
        self.__gameBoard[9][2] = Elephant('red')
        self.__gameBoard[9][6] = Elephant('red')

        # Initialize Advisor Piece Placement
        self.__gameBoard[0][3] = Advisor('black')
        self.__gameBoard[0][5] = Advisor('black')
        self.__gameBoard[9][3] = Advisor('red')
        self.__gameBoard[9][5] = Advisor('red')

        # Initialize General Piece Placement
        self.__gameBoard[0][4] = General('black')
        self.__gameBoard[9][4] = General('red')

    def get_piece(self, x, y):
        return self.__gameBoard[x][y]

    def get_board(self):
        return self.__gameBoard

    def print_board(self):
        """The print board function"""

        row_counter = 1
        for row in self.__gameBoard:

            print(row)
            row_counter += 1


class XiangqiGame:
    """

    """

    def __init__(self):
        """Init function for the game initializes the game board and a list to hold the corresponding letter values
        the user may enter to make a move. Initializes the current turn to red"""
        self.__gameBoard = Board()
        self.__letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
        self.__current_turn = 'red'
        self.__game_state = 'UNFINISHED'

    def get_game_state(self):
        return self.__game_state

    def is_in_check(self, color):
        pass

    def make_move(self, pos_from, pos_to):
        """
        """

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

            print('space empty, returning now')
            # return false since no piece is on indicated space
            return False

        # if the piece to be moved is not the current turn's color, return false
        if moving_piece.get_color() != self.__current_turn:
            return False

        # if the length of the 2 value is greater than 2 (aka if 10 is entered)
        if len(pos_to) > 2:

            # set to row position to the concatenated 1 & 2 positions (10) and subtracting one so it's the 9 index
            to_row_pos = int(pos_to[1] + pos_to[2]) - 1
            print("too long")

        else:

            # to row position set to the int in the second part of the string
            to_row_pos = int(pos_to[1]) - 1

        # instantiate a variable to hold the integer that corresponds with the letter
        to_col_pos = int(self.__letters.index(pos_to[0]))

        valid_move = self.check_move(from_row_pos, from_col_pos, to_row_pos, to_col_pos)
        print(valid_move)
        board = self.__gameBoard.get_board()

        # if the move is valid
        if valid_move is True:

            # change new space to the moving piece
            board[to_row_pos][to_col_pos] = moving_piece

            # change the starting position to empty space
            board[from_row_pos][from_col_pos] = '0'

            # change the color of the current turn
            if self.__current_turn == 'red':
                self.__current_turn = 'black'

            elif self.__current_turn == 'black':
                self.__current_turn = 'red'

            self.__gameBoard.print_board()

        else:
            return False

    def check_move(self, from_row_pos, from_col_pos, to_row_pos, to_col_pos):
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

        # if moving piece is red
        if moving_piece.get_color() == 'red':

            # if the row position is outside the castle, return false
            if to_row_pos < 7 or to_row_pos > 9:
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
                        if self.__gameBoard.get_piece(to_row_pos, to_col_pos) == '0':
                            return True

                    # if the y position is the current position - 1
                    elif to_col_pos == from_col_pos - 1:

                        # if the space is empty
                        if self.__gameBoard.get_piece(to_row_pos, to_col_pos) == '0':
                            return True

                    # if the move is not an increment of 1, return false
                    else:
                        return False

                # If the y value is consistent
                elif from_col_pos == to_col_pos:

                    # if the x position is the current position + 1
                    if to_row_pos == from_row_pos + 1:

                        # if the space is empty
                        if self.__gameBoard.get_piece(to_row_pos, to_col_pos) == '0':
                            return True

                    # if the x position is the current position - 1
                    elif to_row_pos == from_row_pos - 1:

                        # if the space is empty
                        if self.__gameBoard.get_piece(to_row_pos, to_col_pos) == '0':
                            return True

                    # if the move is not an increment of 1, return false
                    else:
                        return False

        elif moving_piece.get_color() == 'black':

            # if the row position is outside the castle, return false
            if to_row_pos < 0 or to_row_pos > 2:
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
                        if self.__gameBoard.get_piece(to_row_pos, to_col_pos) == '0':
                            return True

                    # if the y position is the current position - 1
                    elif to_col_pos == from_col_pos - 1:

                        # if the space is empty
                        if self.__gameBoard.get_piece(to_row_pos, to_col_pos) == '0':
                            return True

                    # if the move is not an increment of 1, return false
                    else:
                        return False

                # If the y value is consistent
                elif from_col_pos == to_col_pos:

                    # if the x position is the current position + 1
                    if to_row_pos == from_row_pos + 1:

                        # if the space is empty
                        if self.__gameBoard.get_piece(to_row_pos, to_col_pos) == '0':
                            return True

                    # if the x position is the current position - 1
                    elif to_row_pos == from_row_pos - 1:

                        # if the space is empty
                        if self.__gameBoard.get_piece(to_row_pos, to_col_pos) == '0':
                            return True

                    # if the move is not an increment of 1, return false
                    else:
                        return False

    def check_move_advisor(self, from_row_pos, from_col_pos, to_row_pos, to_col_pos, moving_piece):

        # instantiate variable to hold the targeted space
        target_space = self.__gameBoard.get_piece(to_row_pos, to_col_pos)

        # if moving piece is red
        if moving_piece.get_color() == 'red':

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

                    # if the position is held by opposing color
                    elif target_space.get_color() == 'black':
                        return True

                    else:
                        return False


                # checking the diagonal position row + 1 | col + 1
                if to_row_pos == from_row_pos + 1 and to_col_pos == from_col_pos + 1:

                    # if the position is empty
                    if target_space == '0':
                        return True

                    elif target_space.get_color() == 'black':
                        return True

                # checking the diagonal position row - 1 | col - 1
                if to_row_pos == from_row_pos - 1 and to_col_pos == from_col_pos - 1:

                    # if the position is empty
                    if target_space == '0':
                        return True

                    elif target_space.get_color() == 'black':
                        return True

                    else:
                        return False

                # checking the diagonal position row - 1 | col + 1
                if to_row_pos == from_row_pos - 1 and to_col_pos == from_col_pos + 1:

                    # if the position is empty
                    if target_space == '0':
                        return True

                    elif target_space.get_color() == 'black':
                        return True

                    else:
                        return False

        # if moving piece is black
        if moving_piece.get_color() == 'black':

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

                    elif target_space.get_color() == 'red':
                        return True

                    else:
                        return False

                # checking the diagonal position row + 1 | col + 1
                if to_row_pos == from_row_pos + 1 and to_col_pos == from_col_pos + 1:

                    # if the position is empty
                    if target_space == '0':
                        return True

                    elif target_space.get_color() == 'red':
                        return True

                    else:
                        return False

                # checking the diagonal position row - 1 | col - 1
                if to_row_pos == from_row_pos - 1 and to_col_pos == from_col_pos - 1:

                    # if the position is empty
                    if target_space == '0':
                        return True

                    elif target_space.get_color() == 'red':
                        return True

                    else:
                        return False

                # checking the diagonal position row - 1 | col + 1
                if to_row_pos == from_row_pos - 1 and to_col_pos == from_col_pos + 1:

                    # if the position is empty
                    if target_space == '0':
                        return True

                    elif target_space.get_color() == 'red':
                        return True

                    else:
                        return False
                           
    def check_move_elephant(self, from_row_pos, from_col_pos, to_row_pos, to_col_pos, moving_piece):

        target_space = self.__gameBoard.get_piece(to_row_pos, to_col_pos)

        # if color is red
        if moving_piece.get_color() == 'red':

            # check if row position would cross the river
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

                elif target_space.get_color() == 'black':
                    return True

                else:
                    return False

            # check diagonal position, row + 2 | column + 2
            if to_row_pos == from_row_pos + 2 and to_col_pos == from_col_pos + 2:

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
            if to_row_pos == from_row_pos - 2 and to_col_pos == from_col_pos - 2:

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
            if to_row_pos == from_row_pos - 2 and to_col_pos == from_col_pos + 2:

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


        # if color is black
        if moving_piece.get_color() == 'black':
            pass

    def check_move_horse(self, from_row_pos, from_col_pos, to_row_pos, to_col_pos, moving_piece):
        pass

    def check_move_chariot(self, from_row_pos, from_col_pos, to_row_pos, to_col_pos, moving_piece):
        pass

    def check_move_cannon(self, from_row_pos, from_col_pos, to_row_pos, to_col_pos, moving_piece):
        pass

    def check_move_soldier(self, from_row_pos, from_col_pos, to_row_pos, to_col_pos, moving_piece):
        pass


class Piece:
    """"""

    def __init__(self, color):
        self.__color = color

    def get_color(self):
        return self.__color


class General(Piece):
    """"""

    def __init__(self, color):
        super(General, self).__init__(color)


class Advisor(Piece):
    """"""

    def __init__(self, color):
        super().__init__(color)


class Elephant(Piece):
    """"""

    def __init__(self, color):
        super().__init__(color)


class Horse(Piece):
    """"""

    def __init__(self, color):
        super().__init__(color)


class Chariot(Piece):
    """"""

    def __init__(self, color):
        super().__init__(color)


class Cannon(Piece):
    """"""

    def __init__(self, color):
        super().__init__(color)


class Soldier(Piece):
    """"""

    def __init__(self, color):
        super().__init__(color)



if __name__ == '__main__':

    board = Board()
    board.print_board()
    game = XiangqiGame()
    move_result = game.make_move('d10', 'e9')

    """
    black_in_check = game.is_in_check('black')
    game.make_move('e7', 'e6')
    state = game.get_game_state()
    """
