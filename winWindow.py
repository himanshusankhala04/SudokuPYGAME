import pygame
from methods import format_time,message_to_screen,text_to_button
pygame.font.init()
pygame.init()

win = pygame.display.set_mode((540,600))
pygame.display.set_caption('Sudoku')
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
yellow = (200,200,0)
green = (34,177,76)
light_green = (0,255,0)
blue = (0,0,255)


def winScreen(win):
    run = True
    while run:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()

        win.fill(white)
        message_to_screen("You Won!", green, 60, 180, 100, win)
        message_to_screen("Congratulations!", black, 50, 125, 230, win)

        pygame.display.update()
