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
        self.__gameBoard[3][0] = Soldier(3, 0, 'black')
        self.__gameBoard[3][2] = Soldier(3, 2, 'black')
        self.__gameBoard[3][4] = Soldier(3, 4, 'black')
        self.__gameBoard[3][6] = Soldier(3, 6, 'black')
        self.__gameBoard[3][8] = Soldier(3, 8, 'black')
        self.__gameBoard[6][0] = Soldier(6, 0, 'red')
        self.__gameBoard[6][2] = Soldier(6, 2, 'red')
        self.__gameBoard[6][4] = Soldier(6, 4, 'red')
        self.__gameBoard[6][6] = Soldier(6, 6, 'red')
        self.__gameBoard[6][8] = Soldier(6, 8, 'red')

        # initialize Cannon Piece Placement
        self.__gameBoard[2][1] = Cannon(2, 1, 'black')
        self.__gameBoard[2][7] = Cannon(2, 7, 'black')
        self.__gameBoard[7][1] = Cannon(7, 1, 'red')
        self.__gameBoard[7][7] = Cannon(7, 7, 'red')

        # initialize Chariot Piece Placement
        self.__gameBoard[0][0] = Chariot(0, 0, 'black')
        self.__gameBoard[0][8] = Chariot(0, 8, 'black')
        self.__gameBoard[9][0] = Chariot(9, 0, 'red')
        self.__gameBoard[9][8] = Chariot(9, 8, 'red')

        # Initialize Horse Piece Placement
        self.__gameBoard[0][1] = Horse(0, 1, 'black')
        self.__gameBoard[0][7] = Horse(0, 1, 'black')
        self.__gameBoard[9][1] = Horse(9, 1, 'red')
        self.__gameBoard[9][7] = Horse(9, 7, 'red')

        # Initialize Elephant Piece Placement
        self.__gameBoard[0][2] = Elephant(0, 2, 'black')
        self.__gameBoard[0][6] = Elephant(0, 6, 'black')
        self.__gameBoard[9][2] = Elephant(9, 2, 'red')
        self.__gameBoard[9][6] = Elephant(9, 6, 'red')

        # Initialize Advisor Piece Placement
        self.__gameBoard[0][3] = Advisor(0, 3, 'black')
        self.__gameBoard[0][5] = Advisor(0, 5, 'black')
        self.__gameBoard[9][3] = Advisor(9, 3, 'red')
        self.__gameBoard[9][5] = Advisor(9, 5, 'red')

        # Initialize General Piece Placement
        self.__gameBoard[0][4] = General(0, 4, 'black')
        self.__gameBoard[9][4] = General(9, 4, 'red')

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

    def get_game_state(self):
        pass

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

        print(moving_piece)
        # print(moving_piece.get_color())

        # if the piece to be moved is not the current turn's color, return false
        if moving_piece.get_color() != self.__current_turn:
            print('wrong color')
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

        # instantiate a variable to hold the game board
        board = self.__gameBoard.get_board()

        # call function to move the piece passing in the moved-to location
        moving_piece.move(to_row_pos, to_col_pos, board)

        self.__gameBoard.print_board()





class Piece:
    """"""

    def __init__(self, x, y, color):
        self.__x_position = x
        self.__y_position = y
        self.__color = color

    def move(self, x_pos, y_pos, gameboard):
        pass

    def check_move(self, x_pos, y_pos, gameboard):
        pass

    def get_x_position(self):
        return self.__x_position

    def get_y_position(self):
        return self.__y_position

    def get_color(self):
        return self.__color

    def set_x_position(self, position):
        self.__x_position = position

    def set_y_position(self, position):
        self.__y_position = position


class General(Piece):
    """"""

    def __init__(self, x, y, color):
        super(General, self).__init__(x, y, color)

    def move(self, x_pos, y_pos, gameboard):
        """"""

        # set move checker equal to the result of the check move function
        move_checker = self.check_move(x_pos, y_pos, gameboard)

        # if the move checker is True
        if move_checker is True:

            # set variables for the current x and y values
            current_x = self.get_x_position()
            current_y = self.get_y_position()
            print(current_x)
            print(current_y)

            # set the x and y positions for the piece
            self.set_x_position(x_pos)
            self.set_y_position(y_pos)

            # change the moved from space to empty and set the new space equal to the piece
            gameboard[x_pos][y_pos] = self
            gameboard[current_x][current_y] = '0'

        else:
            return False

    def check_move(self, x_pos, y_pos, gameboard):

        # instantiating variables to hold the current x, y, and color
        current_x = self.get_x_position()
        current_y = self.get_y_position()
        piece_color = self.get_color()

        print(current_x)
        print(current_y)
        print(x_pos)
        print(y_pos)

        # if the general is red
        if piece_color == 'red':

            # if the row position is outside the castle, return false
            if x_pos < 7 or x_pos > 9:
                return False

            # if the column position is outside the castle, return false
            elif y_pos < 3 or y_pos > 5:
                return False

            # if the move would not put the piece outside the castle
            else:
                # if x value is consistent
                if current_x == x_pos:

                    # if the y position is the current position + 1
                    if y_pos == current_y + 1:

                        # if the space is empty
                        if gameboard[x_pos][y_pos] == '0':
                            return True

                    # if the y position is the current position - 1
                    elif y_pos == current_y - 1:

                        # if the space is empty
                        if gameboard[x_pos][y_pos] == '0':
                            return True

                    # if the move is not an increment of 1, return false
                    else:
                        return False

                # If the y value is consistent
                elif current_y == y_pos:

                    # if the x position is the current position + 1
                    if x_pos == current_x + 1:

                        # if the space is empty
                        if gameboard[x_pos][y_pos] == '0':
                            return True

                    # if the x position is the current position - 1
                    elif x_pos == current_x - 1:

                        # if the space is empty
                        if gameboard[x_pos][y_pos] == '0':
                            return True

                    # if the move is not an increment of 1, return false
                    else:
                        return False

        # if the general is black
        elif piece_color == 'black':

            # if the row position is outside the castle, return false
            if x_pos < 0 or x_pos > 2:
                return False

            # if the column position is outside the castle, return false
            elif y_pos < 3 or y_pos > 5:
                return False

            else:

                # if x value is consistent
                if current_x == x_pos:
                    print('y is changing')

                    # if the y position is the current position + 1
                    if y_pos == current_y + 1:

                        # if the space is empty
                        if gameboard[x_pos][y_pos] == '0':
                            return True

                    # if the y position is the current position - 1
                    elif y_pos == current_y - 1:

                        # if the space is empty
                        if gameboard[x_pos][y_pos] == '0':
                            return True

                    # if the move is not an increment of 1, return false
                    else:
                        return False

                # If the y value is consistent
                elif current_y == y_pos:
                    print('x is changing')

                    # if the x position is the current position + 1
                    if x_pos == current_x + 1:

                        # if the space is empty
                        if gameboard[x_pos][y_pos] == '0':
                            return True

                    # if the x position is the current position - 1
                    elif x_pos == current_x - 1:

                        # if the space is empty
                        if gameboard[x_pos][y_pos] == '0':
                            return True

                    # if the move is not an increment of 1, return false
                    else:
                        return False
        

class Advisor(Piece):
    """"""

    def __init__(self, x, y, color):
        super().__init__(x, y, color)

    def move(self, x_pos, y_pos, gameboard):
        pass

    def check_move(self, x_pos, y_pos, gameboard):
        pass


class Elephant(Piece):
    """"""

    def __init__(self, x, y, color):
        super().__init__(x, y, color)

    def move(self, x_pos, y_pos, gameboard):
        pass

    def check_move(self, x_pos, y_pos, gameboard):
        pass



class Horse(Piece):
    """"""

    def __init__(self, x, y, color):
        super().__init__(x, y, color)

    def move(self, x_pos, y_pos, gameboard):
        pass

    def check_move(self, x_pos, y_pos, gameboard):
        print("LOL")



class Chariot(Piece):
    """"""

    def __init__(self, x, y, color):
        super().__init__(x, y, color)

    def move(self, x_pos, y_pos, gameboard):
        pass

    def check_move(self, x_pos, y_pos, gameboard):

        print(self.get_x_position())
        print(self.get_y_position())

        if x_pos == self.get_x_position():
            print("x same")

        if y_pos == self.get_y_position():
            print("y same")

        print("MOVIN")


class Cannon(Piece):
    """"""

    def __init__(self, x, y, color):
        super().__init__(x, y, color)

    def move(self, x_pos, y_pos, gameboard):
        pass

    def check_move(self, x_pos, y_pos, gameboard):
        pass



class Soldier(Piece):
    """"""

    def __init__(self, x, y, color):
        super().__init__(x, y, color)

    def move(self, x_pos, y_pos, gameboard):
        pass

    def check_move(self, x_pos, y_pos, gameboard):
        pass


if __name__ == '__main__':

    board = Board()
    board.print_board()
    game = XiangqiGame()
    move_result = game.make_move('e10', 'e9')

    """
    black_in_check = game.is_in_check('black')
    game.make_move('e7', 'e6')
    state = game.get_game_state()
    """
