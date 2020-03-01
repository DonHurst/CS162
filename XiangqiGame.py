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
        self.__gameBoard[2][1] = Cannon(2, 1,'black')
        self.__gameBoard[2][7] = Cannon(2, 7,'black')
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
        self.__gameBoard[9][4] = General(0, 9, 'red')

    def get_piece(self, x, y):
        return self.__gameBoard[x][y]

    def print_board(self):
        """The print board function"""

        row_counter = 1
        for row in self.__gameBoard:

            print(row)
            row_counter += 1


class XiangqiGame:


    def __init__(self):
        """Init function for the game initializes the game board and a list to hold the corresponding letter values
        the user may enter to make a move. Initializes the current turn to red"""
        self.__gameBoard = Board()
        self.__letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
        self.__current_turn = 'red'

    def get_turn(self):
        return self.__current_turn

    def get_game_state(self):
        pass

    def is_in_check(self, color):
        pass

    def make_move(self, pos_from, pos_to):
        """
        # If entered move isn't valid
        if len(pos_from) != 2:
            return False

        # If entered move isn't valid
        if len(pos_to) != 2:
            return False

        # If from position move isn't valid digits
        if pos_from[0] not in self.__letters or pos_from[1] < 0 or pos_from[1] > 9:
            return False
        """

        # set the from position to the row value indicated and the index value for column
        from_row_pos = int(pos_from[1]) - 1
        from_col_pos = int(self.__letters.index(pos_from[0]))

        # create variable for the piece to be moved
        moving_piece = self.__gameBoard.get_piece(from_row_pos, from_col_pos)
        print(moving_piece)
        if moving_piece == '0':
            return False

        # if the piece to be moved is not the current turn's color, return false
        if moving_piece.get_color() != self.__current_turn:
            print("hello")

        # set the end location to the row value indicated and the index value for column
        to_row_pos = int(pos_to[1]) - 1
        to_col_pos = int(self.__letters.index(pos_to[0]))
        moved_to_space = self.__gameBoard.get_piece(to_row_pos, to_col_pos)

        # call function to move the piece passing in the moved-to location
        moving_piece.move(to_row_pos, to_col_pos, moved_to_space)


class Piece:
    """"""

    def __init__(self, x, y, color):
        self.__x_position = x
        self.__y_position = y
        self.__color = color

    def move(self, x_pos, y_pos, target_position):
        pass

    def check_move(self, x_pos, y_pos, target_position):
        pass

    def get_color(self):
        return self.__color


class General(Piece):
    """"""

    def __init__(self, x, y, color):
        super(General, self).__init__(x, y, color)

    def move(self, x_pos, y_pos, target_position):

        valid_move = self.check_move(x_pos, y_pos, target_position)

        if valid_move is True:
            pass
        else:
            return False
        """
        if x_pos == self.x and (y_pos == self.y - 1 or y_pos == self.y + 1):
            if target_space == '0':
                valid_move == True
        """



        if valid_move is False:
            return False

    def check_move(self, x_pos, y_pos, target_position):

        # if targeted position is empty
        if target_position == '0':

            # If the x position is + or - 1 and the y position is constant
            if (self.__x_position + 1 == x_pos or self.__x_position - 1 == x_pos) and self.__y_position == y_pos:
                return True

            # If the y position is + or - 1 and the x position is consistent
            elif (self.__y_position - 1 == y_pos or self.__y_position + 1 == y_pos) and self.__x_position == x_pos:
                return True

            # If neither of the above are true, return false
            else:
                return False

        else:
            return False

    def get_color(self):
        return self.__color

class Advisor(Piece):
    """"""

    def __init__(self, x, y, color):
        super().__init__(x, y, color)

    def move(self, x_pos, y_pos, target_position):
        pass



class Elephant(Piece):
    """"""

    def __init__(self, x, y, color):
        super().__init__(x, y, color)

    def move(self, x_pos, y_pos, target_position):
        pass



class Horse(Piece):
    """"""

    def __init__(self, x, y, color):
        super().__init__(x, y, color)

    def move(self, x_pos, y_pos, target_position):
        pass



class Chariot(Piece):
    """"""

    def __init__(self, x, y, color):
        super().__init__(x, y, color)

    def move(self, x_pos, y_pos, target_position):
        pass



class Cannon(Piece):
    """"""

    def __init__(self, x, y, color):
        super().__init__(x, y, color)

    def move(self, x_pos, y_pos, target_position):
        pass



class Soldier(Piece):
    """"""

    def __init__(self, x, y, color):
        super().__init__(x, y, color)

    def move(self, x_pos, y_pos, target_position):
        pass


if __name__ == '__main__':

    board = Board()
    board.print_board()
    game = XiangqiGame()
    move_result = game.make_move('a1', 'e3')
    """
    black_in_check = game.is_in_check('black')
    game.make_move('e7', 'e6')
    state = game.get_game_state()
    """
