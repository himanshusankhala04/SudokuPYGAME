import pygame
from database import DataBase
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



def statsScreen(win,db):
    gameData = db.get_data()
    run = True
    while run:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] in range(230,331) and pygame.mouse.get_pos()[1] in range(360,401):
                pygame.draw.rect(win,blue,(230,360,100,40))
                pygame.display.update()
                db.reset()
                gameData = db.get_data()
            elif event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] in range(10,71) and pygame.mouse.get_pos()[1] in range(10,31):
                pygame.draw.rect(win,black,(10, 10,60,20))
                pygame.display.update()
                db.save()
                run = False


        win.fill(white)
        time = format_time(gameData[3])
        message_to_screen(f"Game Satrted     {gameData[0]}", black, 40, 150, 150, win)
        message_to_screen(f"Game Won          {gameData[1]}", black, 40, 150, 200, win)
        message_to_screen(f"Game Lose         {gameData[2]}", black, 40, 150, 250, win)
        message_to_screen(f"Best Time          {time}", black, 40, 150, 300, win)

        pygame.draw.rect(win,black,(10, 10,60,20))
        text_to_button("Back",white,10, 10,60,20,win)
        pygame.draw.rect(win,blue,(230,360,100,40))
        text_to_button("RESET",white,230,360,100,40,win)

        pygame.display.update()
