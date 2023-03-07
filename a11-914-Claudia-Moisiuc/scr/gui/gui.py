import math
import sys
import random

import pygame


class GUI:
    def __init__(self, repository, service):
        self.__repository = repository
        self.__service = service
        self.__squaresize = 100
        self.__width = 700
        self.__height = 700
        self.__screen = pygame.display.set_mode((self.__width, self.__height))

    def valid_game(self):
        """ the program creates the gui and makes the moves of the computer."""
        red = (255, 0, 0)
        yellow = (255, 255, 0)
        black = (0,0,0)
        radius = int(self.__squaresize // 2 - 5)
        game_over = False
        turn = random.randint(0, 1)
        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.MOUSEMOTION:
                    pygame.draw.rect(self.__screen, black, (0, 0, self.__width, self.__squaresize))
                    posx = event.pos[0]
                    if turn == 0:
                        pygame.draw.circle(self.__screen, red, (posx, self.__squaresize//2), radius)

                pygame.display.update()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    #print("")
                    if turn == 0:
                        posx = event.pos[0]
                        col = int(math.floor(posx / self.__squaresize))
                        if self.__service.valid_location(col):
                            row = self.__service.get_next_row(col)
                            self.__service.drop_piece(row, col, 1)

                            if self.__service.win(1):
                                print('PLAYER 1 WINS!!')
                                game_over = True

                            turn = turn + 1
                            turn = turn % 2

                            self.print_board()

            if turn == 1 and not game_over:

                col = self.__service.pick_best_move(2)
                #col, minimax_score = self.__service.minimax(self.__service.board, 3, True)

                if self.__service.valid_location(col):
                    pygame.time.wait(500)
                    row = self.__service.get_next_row(col)
                    self.__service.drop_piece(row, col, 2)
                    if self.__service.win(2):
                        print('PLAYER 2 WINS!!')
                        game_over = True

                    turn = turn + 1
                    turn = turn % 2

                    self.print_board()

            if game_over:
                pygame.time.wait(3000)

    def print_board(self):
        """ the function prints the board using gui"""
        blue = (0, 0, 255)
        black = (0, 0, 0)
        red = (255, 0, 0)
        yellow = (255, 255, 0)
        radius = int( self.__squaresize//2 - 5)
        for c in range(0, 7):
            for r in range(0, 6):
                pygame.draw.rect(self.__screen, blue, (c * self.__squaresize, r * self.__squaresize+ self.__squaresize,  self.__squaresize,  self.__squaresize))
                pygame.draw.circle(self.__screen, black, (c * self.__squaresize + self.__squaresize // 2, r * self.__squaresize + self.__squaresize + self.__squaresize // 2), radius)

        for c in range(0, 7):
            for r in range(0, 6):
                if self.__service.board[r][c]==1:
                    pygame.draw.circle(self.__screen, red, (c * self.__squaresize + self.__squaresize // 2, self.__height - (r * self.__squaresize + self.__squaresize // 2)), radius)
                elif self.__service.board[r][c]==2:
                    pygame.draw.circle(self.__screen, yellow, (c * self.__squaresize + self.__squaresize // 2, self.__height - (r * self.__squaresize + self.__squaresize // 2)), radius)
        pygame.display.update()

    def make_board(self):
        """ the function calls the move maker and the function that creates the board """
        pygame.init()
        size = (self.__width, self.__height)
        self.print_board()
        pygame.display.update()
        self.valid_game()
        pygame.display.update()

#pygame.init()
#screen = pygame.display.set_mode((800, 600))