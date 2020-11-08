import pygame
from sys import exit
from os import system
import board
from constances import *

from time import sleep

def draw_o(position):
    """
    Draw O in the board
    :param position: list with positions of a center case
    """
    pygame.draw.circle(screen, BLUE, position, radius, circle_width)

def draw_x(position):
    """
    Draw X in the board
    :param position: list with positions of a center case
    """
    pygame.draw.line(screen, RED, (position[0]-60, position[1]-60), (position[0]+60, position[1]+60), cross_width)
    pygame.draw.line(screen, RED, (position[0]+60, position[1]-60), (position[0]-60, position[1]+60), cross_width)


if __name__ == '__main__':

    system('cls')

    # COLORS
    BLACK = pygame.Color(0, 0, 0)
    BLUE = pygame.Color(0, 0, 255)
    RED = pygame.Color(255, 0, 0)

    # BOARD + PLAYER
    board = board.Board()
    player = True
    
    pygame.init()        

    # SCREEN
    screen = pygame.display.set_mode(screen_size)
    screen.fill(pygame.Color(255, 255, 255)) # bg white
    pygame.display.set_caption("Tic-Tac-Toe")

    # DRAW BOARD
    pygame.draw.line(screen, BLACK, line_v1[0], line_v1[1], line_width)
    pygame.draw.line(screen, BLACK, line_v2[0], line_v2[1], line_width)
    pygame.draw.line(screen, BLACK, line_h1[0], line_h1[1], line_width)
    pygame.draw.line(screen, BLACK, line_h2[0], line_h2[1], line_width)

    # CASES RECT (hitboxes)
    cases_rect = {
        '1A': pygame.Rect((40, 40), (cases_width, cases_width)),
        '1B': pygame.Rect((240, 40), (cases_width, cases_width)),
        '1C': pygame.Rect((440, 40), (cases_width, cases_width)),

        '2A': pygame.Rect((40, 240), (cases_width, cases_width)),
        '2B': pygame.Rect((240, 240), (cases_width, cases_width)),
        '2C': pygame.Rect((440, 240), (cases_width, cases_width)),

        '3A': pygame.Rect((40, 440), (cases_width, cases_width)),
        '3B': pygame.Rect((240, 440), (cases_width, cases_width)),
        '3C': pygame.Rect((440, 440), (cases_width, cases_width)),
    }

    pygame.display.update()

    GAME = True
    RUNNING = True
    while RUNNING:

        for event in pygame.event.get():

            # QUIT
            if event.type == pygame.QUIT:
                print("[WINDOW CLOSED]")
                GAME = False
                RUNNING = False
                pygame.quit()
                exit()

            # CLICK
            if event.type == pygame.MOUSEBUTTONDOWN and GAME:
                if event.button == 1:  # left click

                    for key in cases_rect:

                        # if click on a case and this case is empty
                        if cases_rect[key].collidepoint(event.pos) and board.get_case(cases_center[key]) == ' ':
                           
                            if player:  # player 0

                                # draw + set board
                                board.set_case(cases_center[key], 'X')
                                draw_x(cases_center[key])

                                # check win or draw
                                win_game = board.check('X')
                                draw_game = board.check_draw()

                                # print cmd
                                print(f">>>\n{board}X win={win_game}, draw={draw_game}\n")

                                if win_game:
                                    # display "X win"
                                    pygame.font.init()
                                    win_font = pygame.font.SysFont(win_text_font, win_text_size)
                                    win_text = win_font.render("X win", True, BLACK)
                                    screen.blit(win_text, win_text_pos)

                                    # stop the GAME
                                    print('[GAME OVER]')
                                    GAME = False


                            else:  # player 1

                                # draw + set board
                                board.set_case(cases_center[key], 'O')
                                draw_o(cases_center[key])

                                # check win or draw
                                win_game = board.check('O')
                                draw_game = board.check_draw()

                                # print cmd
                                print(f">>>\n{board}O win={win_game}, draw={draw_game}\n")

                                if win_game:

                                    # display "X win"
                                    pygame.font.init()
                                    win_font = pygame.font.SysFont(win_text_font, win_text_size)
                                    win_text = win_font.render("O win", True, BLACK)
                                    screen.blit(win_text, win_text_pos)

                                    # stop the GAME
                                    print('[GAME OVER]')
                                    GAME = False


                            # if no one win
                            if board.check_draw() and GAME:

                                # display "draw"
                                pygame.font.init()
                                win_font = pygame.font.SysFont(win_text_font, win_text_size)
                                win_text = win_font.render("draw", True, BLACK)
                                screen.blit(win_text, (win_text_pos[0]+10, win_text_pos[1]))
                                
                                # stop the GAME
                                print('[GAME OVER]')
                                GAME = False


                            # change the player
                            player = not player

                            # refresh screen
                            pygame.display.update()
