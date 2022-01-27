
import pygame
from pygame.locals import *
from random import*

pygame.init()
width, height = 700, 700
screen=pygame.display.set_mode((width, height))
keys = [False, False]
playerpos=[100,500]


player = pygame.image.load("dude.png")
stone=pygame.image.load("stone.png")
position=0
randmizer=randint(50,width-50)
score=0;
miss=0;
display='Ony 10 Miss Allowed press enter to play'

font = pygame.font.Font('freesansbold.ttf', 18)
while 1:
    screen.fill(0)
    text = font.render(display, True,'green','blue')
    textRect = text.get_rect()
    textRect.center = (300, 100)
    screen.blit(text, textRect)
    display='Catched: '+str(score)+' Missed: '+str(miss)
    screen.blit(player, playerpos)
    screen.blit(stone, [randmizer,position])
    
    if position>=height:
        randmizer=randint(50,width-50)
        position=0
        miss+=1
    else:
        position+=1
    if miss>10:
        display='Game over You scored :'+str(score)+' Press x to exit'
        keys=[False,False]
        position=0
        pressed=pygame.key.get_pressed()
        if pressed[K_x]:
            exit()
    if playerpos[0]<randmizer and playerpos[0]+40>randmizer and playerpos[1]<position and playerpos[1]+40>position :
        score=score+1
        randmizer=randint(50,width-50)
        position=0

    elif playerpos[0]>randmizer and playerpos[0]<randmizer+40 and playerpos[1]>position and playerpos[1]<position+40 :
        score=score+1
        randmizer=randint(50,width-50)
        position=0
    if playerpos[0]<0:
        playerpos[0]=width
    elif playerpos[0]>width:
        playerpos[0]=0
    if playerpos[1]<0:
        playerpos[1]=height
    elif playerpos[1]>height:
        playerpos[1]=0

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit() 
            exit(0) 
        if event.type == pygame.KEYDOWN:
            if event.key==K_d:
                keys[0]=True
            elif event.key==K_a:
                keys[1]=True
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_d:
                keys[0]=False
            elif event.key==pygame.K_a:
                keys[1]=False
        # 9 - Move player
    if keys[0]:
        playerpos[0]+=1
    elif keys[1]:
        playerpos[0]-=1



