import pygame
pygame.font.init()
pygame.init()



def format_time(secs):
    sec = secs%60
    minute = secs//60
    hour = minute//60

    mat = " " + str(minute) + ":" + str(sec)
    return mat

def message_to_screen(msg,color,size,x,y,win):
    font = pygame.font.SysFont(None, size)
    screen_text = font.render(msg, True, color)
    win.blit(screen_text,[x,y])

def text_to_button(text,color,x,y,w,h,win):
    font = pygame.font.SysFont(None, 25)
    text = font.render(text, True, color)
    win.blit(text,[x+(w/2-text.get_width()/2),y+(h/2-text.get_height()/2)])
