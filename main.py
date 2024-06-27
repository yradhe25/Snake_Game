import pygame
from pygame.locals import *
import time
import random

pygame.init()
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
black=(0,0,0)

win_width=600
win_height=500
window=pygame.display.set_mode((win_width,win_height))
pygame.display.set_caption("Snake Game")

snake=10
font=pygame.font.SysFont("twcencondensedextra",20)

def draw_snake(snake,snake_list):
    for block in snake_list:
        pygame.draw.rect(window,green,(block[0],block[1],snake,snake))

def show_score(score):
    number=font.render(f"Score : {score}",True,red)
    window.blit(number,[10,10])

def start_game():
    clock=pygame.time.Clock()
    fps=10
    counter=0
    
    gameOver=False
    gameClose=False

    cx=win_width/2
    cy=win_height/2

    x_change=0
    y_change=0

    snake_length=1
    snake_list=[]

    foodX=round(random.randrange(0,win_width-snake)/10.0)*10.0
    foodY=round(random.randrange(0,win_height-snake)/10.0)*10.0

    while not gameOver:
        while gameClose==True:
            for event in pygame.event.get():
                if event.type==QUIT:
                    gameOver=True
                    gameClose=False
                elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        gameOver=True
                        gameClose=False
                    elif event.key==pygame.K_p:
                        start_game()

            window.fill(black)
            m=font.render("Game over Press q to quit or p to play again",True,red)
            w=font.render(f"Your score : {snake_length-1}",True,red)
            window.blit(m,[130,180])
            window.blit(w,[220,210])
            pygame.display.update()
    
        for event in pygame.event.get():
            if event.type==QUIT:
                gameOver=True
            elif event.type==pygame.KEYDOWN:
                 if event.key==pygame.K_LEFT:
                    x_change=-snake
                    y_change=0
                 elif event.key==pygame.K_RIGHT:
                    x_change=+snake
                    y_change=0
                 elif event.key==pygame.K_UP:
                     x_change=0
                     y_change=-snake
                 elif event.key==pygame.K_DOWN:
                     x_change=0
                     y_change=+snake

        for block in snake_list[:-1]:
            if block==(cx,cy):
                gameClose=True
                break

        if cx<0 or cx>=win_width or cy<0 or cy>=win_height:
            gameClose=True

        cx+=x_change
        cy+=y_change
        window.fill(black)
        pygame.draw.rect(window,red,(foodX,foodY,snake,snake))
        snake_list.append((cx,cy))
        if len(snake_list)>snake_length:
            del snake_list[0]

        draw_snake(snake,snake_list)
        show_score(snake_length-1)

        pygame.display.update()

        if cx==foodX and cy==foodY:
            foodX=round(random.randrange(0,win_width-snake)/10.0)*10.0
            foodY=round(random.randrange(0,win_height-snake)/10.0)*10.0
            snake_length=snake_length+1
            counter+=1
            if counter%5==0:
                fps+=4

        clock.tick(fps)

    pygame.quit()
    quit()

start_game()