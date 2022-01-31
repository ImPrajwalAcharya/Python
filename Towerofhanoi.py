import pygame
class stack:
    def __init__(self):
        self.top=-1
        self.number=[0,0,0]
    def push(self,number):
        if self.top<3:
            self.top+=1
            self.number[self.top]=number
    def pop (self):
        if self.top!=-1:
            temp=self.number[self.top]
            self.number[self.top]=0
            self.top-=1
            return temp
    def see(self):
        saw=[]
        temp=2
        while temp>=0:
            saw.append(self.number[temp])
            temp-=1
        return saw
    def seetop(self):
        if self.top==-1:
            return 4
        else:
            return self.number[self.top]
width=700
height=500
getx=[]
pygame.init()
color=['red','blue','white','green']
screen=pygame.display.set_mode((width,height))
rod_image='rod.png'
rod=pygame.image.load(rod_image)
rods=pygame.transform.scale(rod, (100,200))
display='Welcome to the tower of hanoi'
font = pygame.font.Font('freesansbold.ttf', 18)
text = font.render(display, True,'green','blue')
d=[stack(),stack(),stack()]
d[0].push(3)
d[0].push(2)
d[0].push(1)
posx=[90,98,106]
posy=[480,460,440]
size=80
while 1:
    screen.fill(0)
    screen.blit(rods,[100,300])
    screen.blit(rods,[300,300])
    screen.blit(rods,[500,300])
    textRect = text.get_rect()
    textRect.center = (350, 100)
    screen.blit(text, textRect)
    for i in range(3):
        if d[i].see()==[1,2,3]:
            pygame.draw.rect(screen, color[0], pygame.Rect(posx[0]+200*i,posy[0], size+40, 15))
            pygame.draw.rect(screen, color[1], pygame.Rect(posx[1]+200*i,posy[1], size+20, 15))
            pygame.draw.rect(screen, color[2], pygame.Rect(posx[2]+200*i,posy[2], size, 15))
        elif d[i].see()==[0,1,2]:
            pygame.draw.rect(screen, color[1], pygame.Rect(posx[1]+200*i,posy[0], size+20, 15))
            pygame.draw.rect(screen, color[2], pygame.Rect(posx[2]+200*i,posy[1], size, 15))
        elif d[i].see()==[0,1,3]:
            pygame.draw.rect(screen, color[0], pygame.Rect(posx[0]+200*i,posy[0], size+40, 15))
            pygame.draw.rect(screen, color[2], pygame.Rect(posx[2]+200*i,posy[1], size, 15))
        elif d[i].see()==[0,2,3]:
            pygame.draw.rect(screen, color[0], pygame.Rect(posx[0]+200*i,posy[0], size+40, 15))
            pygame.draw.rect(screen, color[1], pygame.Rect(posx[1]+200*i,posy[1], size+20, 15))
        elif d[i].see()==[0,0,1]:
            pygame.draw.rect(screen, color[2], pygame.Rect(posx[2]+200*i,posy[0], size, 15))
        elif d[i].see()==[0,0,2]:
            pygame.draw.rect(screen, color[1], pygame.Rect(posx[1]+200*i,posy[0], size+20, 15))
        elif d[i].see()==[0,0,3]:
            pygame.draw.rect(screen, color[0], pygame.Rect(posx[0]+200*i,posy[0], size+40, 15))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit() 
            exit(0)
        if event.type==pygame.MOUSEBUTTONDOWN:
            x,y=pygame.mouse.get_pos()
            getx.append(x)
            k=getx.index(x)
            if k%2==1:
                if x<200 and x>0:
                    if getx[k-1]>200 and getx[k-1]<400:
                        if d[0].seetop()>d[1].seetop():
                            d[0].push(d[1].pop())
                    elif getx[k-1]>400 and getx[k-1]<600:
                        if d[0].seetop()>d[2].seetop():
                            d[0].push(d[2].pop())
                    else:
                        getx.clear()
                elif x>200 and x<400:
                    if getx[k-1]<200 and getx[k-1]>0:
                        if d[1].seetop()>d[0].seetop():
                            d[1].push(d[0].pop())
                    elif getx[k-1]>400 and getx[k-1]<600:
                        if d[1].seetop()>d[2].seetop():
                            d[1].push(d[2].pop())
                    else:
                        getx.clear()
                elif x>400 and x<600:
                    if getx[k-1]>200 and getx[k-1]<400:
                        if d[2].seetop()>d[1].seetop():
                            d[2].push(d[1].pop())
                    elif getx[k-1]>0 and getx[k-1]<200:
                        if d[2].seetop()>d[0].seetop():
                            d[2].push(d[0].pop())
                    else:
                        getx.clear()
    if d[1].see()==[1,2,3] or d[2].see()==[1,2,3]:
        text = font.render("Congo You completed the game", True,'green','blue')
        screen.blit(text, textRect)