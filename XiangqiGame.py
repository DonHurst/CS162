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

    def print_board(self):
        """The print board function"""

        row_counter = 1
        for row in self.__gameBoard:

            print(row)
            row_counter += 1


class XiangqiGame:

    def __init__(self):
        self.__gameBoard = Board()
        self.__letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

    def get_game_state(self):
        pass

    def is_in_check(self, color):
        pass

    def make_move(self, pos_from, pos_to):

        # If entered move isn't valid
        if len(pos_from) != 2:
            return False

        # If entered move isn't valid
        if len(pos_to) != 2:
            return False

        # If from position move isn't valid digits
        if pos_from[0] not in self.__letters or pos_from[1] > 9:
            return False

        else:
            row_pos = pos_from[1]
            col_pos = self.__letters[pos_from[0]]
            self.__gameboard[row_pos][col_pos].move()

class Piece:
    """"""

    def __init__(self, x, y, color):
        self.__x_position = x
        self.__y_position = y
        self.__color = color





class General(Piece):
    """"""

    def __init__(self, x, y, color):
        super(General, self).__init__(x, y, color)
        self.__symbol = 'G'

    #def move(self, x_pos, y_pos):

        




class Advisor(Piece):
    """"""

    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.__symbol = 'A'

    def move(self, x_pos, y_pos):

        current_x = self.__x_position
        current_y = self.__y_position
        valid_move = False


        if self.__color == 'red':


        elif self.__color == 'black':

        if current_x

        if valid_move is True:


        else:
            return

class Elephant(Piece):
    """"""

    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.__symbol = 'E'


class Horse(Piece):
    """"""

    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.__symbol = 'H'


class Chariot(Piece):
    """"""

    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.__symbol = 'CH'


class Cannon(Piece):
    """"""

    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.__symbol = 'CA'


class Soldier(Piece):
    """"""

    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.__symbol = 'S'


if __name__ == '__main__':

    board = Board()
    board.print_board()
    """
    game = XiangqiGame()
    move_result = game.make_move('c1', 'e3')
    black_in_check = game.is_in_check('black')
    game.make_move('e7', 'e6')
    state = game.get_game_state()
    """
