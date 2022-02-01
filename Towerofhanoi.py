import pygame
n=5
moves=0
width=700
height=500
getx=[]
pygame.init()
color=['red','blue','white','green','yellow','white']
screen=pygame.display.set_mode((width,height))
rod_image='rod.png'
rod=pygame.image.load(rod_image)
rods=pygame.transform.scale(rod, (100,200))
display='Welcome to the tower of hanoi'
font = pygame.font.Font('freesansbold.ttf', 18)
text = font.render(display, True,'green','blue')
class stack:
    def __init__(self):
        self.top=-1
        self.number=[]
        temp=n
        while temp!=0:
            temp-=1
            self.number.append(0)
    def push(self,number):
        if self.top<n:
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
        temp=0
        while temp<n:
            saw.append(self.number[temp])
            temp+=1
        return saw
    def seetop(self):
        if self.top==-1:
            return n+1
        else:
            return self.number[self.top]
    def combo(self,num,pos):
        
        if num !=0:
            state=pygame.draw.rect(screen, color[num-1], pygame.Rect(posx[num-1]+200*i,posy[pos], size+20*num, 15))
            return state
def load(number):
    while number!=0:
        d[0].push(number)
        number-=1
d=[stack(),stack(),stack()]
load(n)
initial=d[0].see()
posx=[122,114,106,98,90]
posy=[480,460,440,420,400]
size=80
while 1:
    screen.fill(0)
    screen.blit(rods,[100,300])
    screen.blit(rods,[300,300])
    screen.blit(rods,[500,300])
    textRect = text.get_rect()
    textRect.center = (350, 100)
    text = font.render(display, True,'green','blue')
    screen.blit(text, textRect)
    for i in range(3):
        pos=0
        for j in d[i].see():
            if j!=0:
                d[i].combo(j,pos)
                pos+=1
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
                            moves+=1
                    elif getx[k-1]>400 and getx[k-1]<600:
                        if d[0].seetop()>d[2].seetop():
                            d[0].push(d[2].pop())
                            moves+=1
                    else:
                        getx.clear()
                elif x>200 and x<400:
                    if getx[k-1]<200 and getx[k-1]>0:
                        if d[1].seetop()>d[0].seetop():
                            d[1].push(d[0].pop())
                            moves+=1
                    elif getx[k-1]>400 and getx[k-1]<600:
                        if d[1].seetop()>d[2].seetop():
                            d[1].push(d[2].pop())
                            moves+=1
                    else:
                        getx.clear()
                elif x>400 and x<600:
                    if getx[k-1]>200 and getx[k-1]<400:
                        if d[2].seetop()>d[1].seetop():
                            d[2].push(d[1].pop())
                            moves+=1
                    elif getx[k-1]>0 and getx[k-1]<200:
                        if d[2].seetop()>d[0].seetop():
                            d[2].push(d[0].pop())
                            moves+=1
                    else:
                        getx.clear()
        
    if d[1].see()==initial or d[2].see()==initial:
        if moves==2**n-1:
            display="Game completed with least moves "+str(moves)
        else:
            display="Game completed with "+str(moves)+" moves"
    else:
        display='moves = '+str(moves)+' Least Moves Possible = '+str(2**n-1)