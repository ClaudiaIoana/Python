import random


class Service:
    def __init__(self, repository):
        self.__repository = repository

    @property
    def game_board(self):
        return self.__repository.game_board

    @property
    def board(self):
        return self.__repository.board

    def valid_place_asteroid(self, asteroid_row, asteroid_col):
        if asteroid_row == 0:
            index_first_row = asteroid_row
            index_last_row = asteroid_row+1

        elif asteroid_row == 6:
            index_first_row = asteroid_row-1
            index_last_row = asteroid_row

        else:
            index_first_row = asteroid_row -1
            index_last_row = asteroid_row + 1

        if asteroid_col == 1:
            index_first_col = asteroid_col
            index_last_col = asteroid_col + 1

        elif asteroid_col == 7:
            index_first_col = asteroid_col -1
            index_last_col = asteroid_col

        else:
            index_first_col = asteroid_col - 1
            index_last_col = asteroid_col +1


        for i in range (index_first_row,  index_last_row+1):
            for j in range (index_first_col, index_last_col+1):
                if self.game_board[i][j] != ' ':
                    return False
        return True

    def asteroid_place(self):
        ok = False
        while ok == False:
            asteroid_row = random.randint(0, 6)
            asteroid_col = random.randint(1, 7)
            ok = self.valid_place_asteroid(asteroid_row, asteroid_col)

        self.board[asteroid_row][asteroid_col] = '*'
        self.game_board[asteroid_row][asteroid_col] = '*'

    def asteroids(self):
        for i in range(0, 8):
            self.asteroid_place()

    def valid_place_alien(self, alien_row, alien_col):
        #if (alien_row != 0 and alien_row != 6) or (alien_col != 0 and alien_col != 6):
            #return False

        if self.board[alien_row][alien_col] != ' ':
            return False

        if alien_row - 3 > -3 and alien_row - 3 < 3:
            return False

        if alien_col - 3 > -3 and alien_row - 3 < 3:
            return False

        return True

    def place_alien(self):
        alien_row = random.randint(0, 6)
        alien_col = random.randint(1, 7)
        ok = False
        while ok == False:
            ok = self.valid_place_alien(alien_row, alien_col)
            if ok == False:
                alien_row = random.randint(0, 6)
                alien_col = random.randint(1, 7)

        self.game_board[alien_row][alien_col] = 'X'

    def alien(self):
        for i in range(0, 2):
            self.place_alien()

    def fire_valid(self, coordonate_row, coordonate_col):
        '''
        the function sees if the place has already been hit or if the place contains an asteroid
        :param coordonate_row: the coodonate of the row on which it will fire
        :param coordonate_col: the coodonate of the column on which it will fire
        :return: False if we hit an asteroid or an already hit place
        '''
        if self.game_board[coordonate_row][coordonate_col] == '*' or self.game_board[coordonate_row][coordonate_col] == '-':
            return False
        else:
            return True

    def fire(self, row, col):
        '''
        the function puts - in both the diplayed bord as well as on the hit bord if we hit an alien
        :param row: the row of the hit
        :param col: the column of the hit
        :return: hit if we hit an alien and not hit otherwise
        '''
        if self.game_board[row][col] == 'X':
            self.game_board[row][col] = '-'
            self.board[row][col] = '-'
            return 'hit'
        return 'not hit'


#