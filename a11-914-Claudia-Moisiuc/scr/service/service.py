import math
import random


class Service:
    def __init__(self, repository):
        self.__repository = repository

    @property
    def board(self):
        """the function returns the board"""
        return self.__repository.board

    def drop_piece(self, row, col, piece):
        """the function drops a piece in the place that is set to"""
        self.board[row][col] = piece

    def simulate_drop_piece(self, board, row, col, piece):
        """the function simulates the dropping of a piece in order to find the best case in which it can drop"""
        board[row][col] = piece
        return board

    def valid_location(self, col):
        """the function sees if you can drop a piece on that column"""
        return self.board[5][col] == 0

    def get_next_row(self, col):
        """the function finds the next available row on that column"""
        for r in range(0, 6):
            if self.board[r][col] == 0:
                return r

    def win(self, piece):
        """the function calculates if the player have won"""
        #Check horizontal win
        for c in range(0, 4):
            for r in range(0, 6):
                 if self.board[r][c] == piece and self.board[r][c+1] == piece and self.board[r][c+2] == piece and self.board[r][c+3] == piece:
                     return True

        #Check vertical win
        for c in range(0, 7):
            for r in range(0, 3):
                if self.board[r][c] == piece and self.board[r + 1][c] == piece and self.board[r + 2][c] == piece and self.board[r + 3][c] == piece:
                    return True

        #Check diagonal win
        for c in range(0, 4):
            for r in range(0, 3):
                 if self.board[r][c] == piece and self.board[r+1][c+1] == piece and self.board[r+2][c+2] == piece and self.board[r+3][c+3] == piece:
                     return True

        for c in range(0, 4):
            for r in range(0, 6):
                 if self.board[r][c] == piece and self.board[r-1][c+1] == piece and self.board[r-2][c+2] == piece and self.board[r-3][c+3] == piece:
                     return True

    def is_terminal_mode(self):
        return self.win(1) or self.win(2) or len(self.get_valid_location()) == 0

    def minimax(self, board, depth, maximazingPlayer):
        valid_locations = self.get_valid_location()
        is_terminal = self.is_terminal_mode()
        if depth == 0 or is_terminal:
            if is_terminal:
                if self.win(1):
                    return (None, 10000000)
                elif self.win(2):
                    return (None, -10000000)
                else:
                    #Game is over
                    return (None, 0)
            else:
                return (None, self.score_position(self.board, 2))

        if maximazingPlayer:
            value = -math.inf
            column = random.choice(valid_locations)
            for col in valid_locations:
                row = self.get_next_row(col)
                b_copy = board.copy()
                self.simulate_drop_piece(b_copy, row, col, 2)
                new_score = self.minimax(b_copy, depth - 1, False)[1]
                if new_score > value:
                    value = new_score
                    column = col
            return column, new_score

        else: # Minimizing
            value = math.inf
            column = random.choice(valid_locations)
            for col in valid_locations:
                row = self.get_next_row(col)
                b_copy = board.copy()
                self.simulate_drop_piece(b_copy, row, col, 1)
                new_score = self.minimax(b_copy, depth - 1, True)[1]
                if new_score < value:
                    value = new_score
                    column = col
            return column, new_score


    def score_position(self, board, piece):
        """the function calculates which move is the best for tha computer adding points to that move"""
        score = 0
        # Score center column
        center_array = [int(i) for i in list(board[:,7//2])]
        center_count = center_array.count(piece)
        score += center_count * 3

        # Score Horizontal
        for r in range(0, 6):
            row_array = [int(i) for i in list(board[r,:])]
            for c in range(0, 4):
                window = row_array[c:c+4]
                score += self.evaluate_window(window, piece)

        #Score Vertical
        for c in range(0, 7):
            col_array = [int(i) for i in list(board[:, c])]
            for r in range(0, 3):
                window = col_array[r:r + 4]
                score += self.evaluate_window(window, piece)

        #Score positive diagonal
        for r in range(0, 3):
            for c in range(0, 4):
                window = [self.board[r+i][c+i] for i in range(0, 4)]
                score += self.evaluate_window(window, piece)

        #Score negative diagonal
        for r in range(0, 3):
            for c in range(0, 4):
                window = [self.board[r+3-i][c+i] for i in range(0, 4)]
                score += self.evaluate_window(window, piece)

        return score

    def evaluate_window(self, window, piece):
        score = 0
        opp_piece = 1
        if piece == 1:
            opp_piece = 2

        if window.count(piece) == 4:
            score += 100
        elif window.count(piece) == 3 and window.count(0) == 1:
            score += 10
        elif window.count(piece) == 2 and window.count(0) == 2:
            score += 5

        if window.count(opp_piece) == 3 and window.count(0) == 1:
            score -= 80

        return score

    def get_valid_location(self):
        """the function makes a list with all the valid columns"""
        valid = []
        for col in range (0, 7):
            if self.valid_location(col):
                valid.append(col)
        return valid

    def pick_best_move(self, piece):
        valid = self.get_valid_location()
        best_score = -10000
        best_col = random.choice(valid)
        for col in valid:
            row = self.get_next_row(col)
            temp_board = self.board.copy()
            temp_board = self.simulate_drop_piece(temp_board, row, col, piece)
            score = self.score_position(temp_board, piece)
            if score > best_score:
                best_score = score
                best_col = col

        return best_col


