class Board:

    def __init__(self):
        """
        init a tic-tac-toe board represente by a list of 3 lists that contains 3 characters
        """
        self.board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]

    def get_case(self, case):
        """
        Get the case value on the board
        :param case: tuple x, y of the center
        :return: the value of the case (' ', 'X', 'O')
        """
        if case == (140, 140):
            return self.board[0][0]
        elif case == (340, 140):
            return self.board[0][1]
        elif case == (540, 140):
            return self.board[0][2]

        elif case == (140, 340):
            return self.board[1][0]
        elif case == (340, 340):
            return self.board[1][1]
        elif case == (540, 340):
            return self.board[1][2]

        elif case == (140, 540):
            return self.board[2][0]
        elif case == (340, 540):
            return self.board[2][1]
        elif case == (540, 540):
            return self.board[2][2]
        
        else:
            raise ValueError("This case (center) does not exist")

    def set_case(self, case, value):
        """
        Change the case on the board
        :param case:
        :param value: X or O
        """
        if case == (140, 140):
            self.board[0][0] = value
        elif case == (340, 140):
            self.board[0][1] = value
        elif case == (540, 140):
            self.board[0][2] = value

        elif case == (140, 340):
            self.board[1][0] = value
        elif case == (340, 340):
            self.board[1][1] = value
        elif case == (540, 340):
            self.board[1][2] = value

        elif case == (140, 540):
            self.board[2][0] = value
        elif case == (340, 540):
            self.board[2][1] = value
        elif case == (540, 540):
            self.board[2][2] = value

        else:
            raise ValueError("This case (center) does not exist")

    def check(self, player):
        """
        check if a player win
        :param player: string 'X' or 'O'
        :return: bool
        """
        # ROW
        for l in self.board:
            if l == [player, player, player]:
                return True

        # COLUMN
        column_A = ((0, 0), (1, 0), (2, 0))
        column_B = ((0, 1), (1, 1), (2, 1))
        column_C = ((0, 2), (1, 2), (2, 2))
        list_column = [column_A, column_B, column_C]
        for column in list_column:
            if self.board[column[0][0]][column[0][1]] == self.board[column[1][0]][column[1][1]] == self.board[column[2][0]][column[2][1]] == player:
                return True

        # DIAGONAL
        diagonal_1 = ((0, 0), (1, 1), (2, 2))
        diagonal_2 = ((0, 2), (1,1), (2, 0))
        list_diagonal = [diagonal_1, diagonal_2]
        for diagonall in list_diagonal:
            if self.board[diagonall[0][0]][diagonall[0][1]] == self.board[diagonall[1][0]][diagonall[1][1]] == self.board[diagonall[2][0]][diagonall[2][1]] == player:
                return True
        
        return False

    def check_draw(self):
        """
        Check if the board is full without winner 
        :return: bool
        """
        if not self.check('X') or not self.check('O'):
            for l in self.board:
                for c in l:
                    if c == ' ':
                        return False
        return True

    def __repr__(self):
        """
        Show the board with print()
        """
        msg = ""
        for l in self.board:
            for c in l:
                msg += ' ' + c + ' |'
            msg = msg[0:-1] + '\n'
            msg += '---+---+---\n'
        msg = msg[0:-12]    

        return msg

if __name__ == '__main__':
    b = Board()
    print(b)