# GUI.py
import pygame
from solver import solve, valid
import time
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

class Grid:
    board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

    def __init__(self, rows, cols, width, height):
        self.rows = rows
        self.cols = cols
        self.cubes = [[Cube(self.board[i][j], i, j, width, height) for j in range(cols)] for i in range(rows)]
        self.width = width
        self.height = height
        self.model = None
        self.selected = None

    def update_model(self):
        self.model = [[self.cubes[i][j].value for j in range(self.cols)] for i in range(self.rows)]

    def place(self, val):
        row, col = self.selected
        if self.cubes[row][col].value == 0:
            self.cubes[row][col].set(val)
            self.update_model()

            if valid(self.model, val, (row,col)) and solve(self.model):
                self.cubes[row][col].success = True
                return True
            else:
                self.cubes[row][col].set_red(val)
                self.cubes[row][col].set_temp(0)
                self.update_model()
                return False

    def sketch(self, val):
        row, col = self.selected
        self.cubes[row][col].set_temp(val)



    def draw(self, win):
        # Draw Grid Lines
        gap = self.width / 9
        for i in range(self.rows+1):
            if i % 3 == 0 and i != 0:
                thick = 4
            else:
                thick = 1
            pygame.draw.line(win, black, (0, i*gap), (self.width, i*gap), thick)
            pygame.draw.line(win, black, (i * gap, 0), (i * gap, self.height), thick)

        # Draw Cubes
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].draw(win)

    def select(self, row, col):
        # Reset all other
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].selected = False

        self.cubes[row][col].selected = True
        self.selected = (row, col)

    def clear(self):
        if self.selected == None:
            return
        row, col = self.selected
        if self.cubes[row][col].value == 0 or self.cubes[row][col].isRed:
            self.cubes[row][col].set_temp(0)
            self.cubes[row][col].set(0)
            self.cubes[row][col].isRed = False

    def click(self, pos):

        if pos[0] < self.width and pos[1] < self.height:
            gap = self.width / 9
            x = pos[0] // gap
            y = pos[1] // gap
            return (int(y),int(x))
        else:
            return None

    def is_finished(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.cubes[i][j].value == 0:
                    return False
        return True


class Cube:
    rows = 9
    cols = 9

    def __init__(self, value, row, col, width ,height):
        self.value = value
        self.temp = 0
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.selected = False
        self.isRed = False
        self.success = False
        if self.value != 0:
            self.success = True

    def draw(self, win):
        fnt = pygame.font.SysFont("comicsans", 40)

        gap = self.width / 9
        x = self.col * gap
        y = self.row * gap


        if self.temp != 0 and self.value == 0:
            text = fnt.render(str(self.temp), 1, (128,128,128))
            win.blit(text, (x+5, y+5))
        elif not(self.value == 0):
            if self.isRed:
                text = fnt.render(str(self.value), 1, red)
                win.blit(text, (x + (gap/2 - text.get_width()/2), y + (gap/2 - text.get_height()/2)))
            else:
                text = fnt.render(str(self.value), 1, black)
                win.blit(text, (x + (gap/2 - text.get_width()/2), y + (gap/2 - text.get_height()/2)))

        if self.selected:
            if self.success:
                pygame.draw.rect(win, light_green, (x,y, gap ,gap), 3)
                return
            pygame.draw.rect(win, red, (x,y, gap ,gap), 3)

    def set(self, val):
        self.value = val

    def set_red(self, val):
        self.value = val
        self.isRed=True

    def set_temp(self, val):
        self.temp = val


def redraw_window(win, board, time, strikes):
    win.fill((255,255,255))
    # Draw time
    fnt = pygame.font.SysFont("comicsans", 40)
    text = fnt.render("Time: " + format_time(time), 1, (0,0,0))
    win.blit(text, (540 - 160, 560))
    # Draw Strikes
    text = fnt.render("X " * strikes, 1, (255, 0, 0))
    win.blit(text, (20, 560))
    # Draw grid and board
    board.draw(win)


def format_time(secs):
    sec = secs%60
    minute = secs//60
    hour = minute//60

    mat = " " + str(minute) + ":" + str(sec)
    return mat


def main(win):

    pygame.display.set_caption("Sudoku")
    board = Grid(9, 9, 540, 540)
    key = None
    run = True
    start = time.time()
    strikes = 0
    while run:

        play_time = round(time.time() - start)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_9:
                    key = 9
                if event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE :
                    board.clear()
                    key = None
                if board.selected != None:
                    if event.key == pygame.K_RETURN:
                        i, j = board.selected
                        if board.cubes[i][j].temp != 0:
                            if board.place(board.cubes[i][j].temp):
                                print("Success")
                            else:
                                print("Wrong")
                                strikes += 1
                            key = None

                            if board.is_finished():
                                print("Game over")
                                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clicked = board.click(pos)
                if clicked:
                    board.select(clicked[0], clicked[1])
                    key = None

        if board.selected and key != None:
            board.sketch(key)

        redraw_window(win, board, play_time, strikes)
        pygame.display.update()


def message_to_screen(msg,color,size,x,y,win):
    font = pygame.font.SysFont(None, size)
    screen_text = font.render(msg, True, color)
    win.blit(screen_text,[x,y])

def text_to_button(text,color,x,y,w,h):
    font = pygame.font.SysFont(None, 25)
    text = font.render(text, True, color)
    win.blit(text,[x+(w/2-text.get_width()/2),y+(h/2-text.get_height()/2)])





def gameIntro():
    intro = True
    while intro:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                intro =False
            elif event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] in range(230,331) and pygame.mouse.get_pos()[1] in range(300,341):
                pygame.draw.rect(win,light_green,(230,300,100,40))
                text_to_button("PLAY",black,230,300,100,40)
                pygame.display.update()


                main(win)

        win.fill(white)
        message_to_screen("Sudoku", black, 80, 180, 230, win)

        pygame.draw.rect(win,green,(230,300,100,40))
        text_to_button("PLAY",black,230,300,100,40)

        pygame.display.update()



gameIntro()

pygame.quit()
