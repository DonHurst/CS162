# Author: Don Hurst
# Date: 02/22/2020
# Description:


class Board:
    """The Board class """

    def __init__(self):
        """"""

        # Variables for number of rows / columns
        self.__rows = 10
        self.__columns = 9

        # Create empty game board
        self.__gameBoard = [[0] * self.__columns] * self.__rows

        # Initialize Piece Placement
        self.__gameBoard[][] =

    def print_board(self):
        """The print board function"""

        row_counter = 1
        for row in self.__gameBoard:

            print(row_counter, row)
            row_counter += 1


class XiangqiGame:

    def __init__(self):
        self.__gameBoard = Board()


    def get_game_state(self):
        pass

    def is_in_check(self, color):
        pass

    def make_move(self, pos_from, pos_to):
        pass


class Piece:
    """"""

    def __init__(self, x, y):
        self.x_position = x
        self.y_position = y


class General(Piece):
    """"""

    def __init__(self, x, y):
        super().__init__(x, y)
        self.__symbol = 'G'


class Advisor(Piece):
    """"""

    def __init__(self, x, y):
        super().__init__(x, y)
        self.__symbol = 'A'


class Elephant(Piece):
    """"""

    def __init__(self, x, y):
        super().__init__(x, y)
        self.__symbol = 'E'


class Horse(Piece):
    """"""

    def __init__(self, x, y):
        super().__init__(x, y)
        self.__symbol = 'H'


class Chariot(Piece):
    """"""

    def __init__(self, x, y):
        super().__init__(x, y)
        self.__symbol = 'CH'


class Cannon(Piece):
    """"""

    def __init__(self, x, y):
        super().__init__(x, y)
        self.__symbol = 'CA'


class Soldier(Piece):
    """"""

    def __init__(self, x, y):
        super().__init__(x, y)
        self.__symbol = 'S'


if __name__ == '__main__':

    board = Board()
    board.print_board()
