import pygame
from statsWindow import statsScreen
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


def loseScreen(win,db):
    print("Hereim")
    run = True
    while run:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] in range(120,261) and pygame.mouse.get_pos()[1] in range(350,391):
                pygame.draw.rect(win,green,(120,350,140,40))
                pygame.display.update()
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] in range(280,421) and pygame.mouse.get_pos()[1] in range(350,391):
                pygame.draw.rect(win,red,(280,350,140,40))
                pygame.display.update()
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] in range(220,321) and pygame.mouse.get_pos()[1] in range(410,451):
                pygame.draw.rect(win,yellow,(220,410,100,40))
                pygame.display.update()
                statsScreen(win,db)


        win.fill(white)
        message_to_screen("You Lost!", red, 60, 180, 100, win)

        pygame.draw.rect(win,green,(120,350,140,40))
        text_to_button("PLAY AGAIN",black,120,350,140,40,win)

        pygame.draw.rect(win,red,(280,350,120,40))
        text_to_button("QUIT",black,280,350,120,40,win)

        pygame.draw.rect(win,yellow,(220,410,100,40))
        text_to_button("STATS",black,220,410,100,40,win)
        pygame.display.update()
