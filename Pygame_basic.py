import pygame

sw=640
sh=480

pygame.init()

aken = pygame.display.set_mode([sw,sh])

class Person:
    def __init__(self,x,y,colour):
        self.x=x
        self.y=y
        self.colour=colour
        self.vx=0
        self.vy=0
        self.points_bol=[False,False,False,
                         False,False,False,
                         False,False,False]
        self.move_bol=[False,False,False,False,False]
        self.jump1=False
        self.jump2=False
        self.jump_bol=True
        self.var=0
    
    def draw(self):
        pygame.draw.rect(aken,[255,0,0],[ self.x-20, self.y-20, 40, 40],0)
        
    def update(self,walls):
        self.points_bol=[False,False,False,
                         False,False,False,
                         False,False,False]
        self.jump1=False
        for s in walls:
            if self.x in range(s.x, s.x+s.w) and self.y + 20 in range(s.y,s.y+s.h):
                self.points_bol[7]=True
                self.y =s.y-20
                self.vy = 0
                self.jump1=True
                self.jump2=True
            elif self.x+20 in range(s.x, s.x+s.w) and self.y in range(s.y,s.y+s.h):
                self.points_bol[5]=True
                self.x =s.x-20
                self.jump1=True
                self.jump2=True
            elif self.x-20 in range(s.x, s.x+s.w) and self.y in range(s.y,s.y+s.h):
                self.points_bol[3]=True
                self.x =s.x+s.w+19
                self.jump1=True
                self.jump2=True
            elif self.x in range(s.x, s.x+s.w) and self.y-20 in range(s.y,s.y+s.h):
                self.points_bol[1]=True
                self.y =s.y+s.h+20
            elif self.x+20 in range(s.x, s.x+s.w) and self.y+20 in range(s.y,s.y+s.h):
                self.points_bol[8]=True
            elif self.x-20 in range(s.x, s.x+s.w) and self.y+20 in range(s.y,s.y+s.h):
                self.points_bol[6]=True
            elif self.x+20 in range(s.x, s.x+s.w) and self.y-20 in range(s.y,s.y+s.h):
                self.points_bol[2]=True
            elif self.x-20 in range(s.x, s.x+s.w) and self.y-20 in range(s.y,s.y+s.h):
                self.points_bol[0]=True
                
    def move(self):
        if self.points_bol[7] == True:
            self.vy = 0
        elif self.points_bol[7] == False:
            self.vy +=1
            
        if (self.move_bol[3]==False and self.move_bol[1]==False) and (self.points_bol[3]==True or self.points_bol[5]==True):
            self.vy =0
        elif (self.points_bol[3]==True or self.points_bol[5]==True) and self.move_bol[3]==True:
            self.vy= 5
        elif (self.points_bol[3]==True or self.points_bol[5]==True) and self.move_bol[1]==True:
            self.vy=-5
            
        if self.points_bol[3]==True and self.move_bol[4]==True and self.jump_bol==True:
            self.vy=-10
            self.vx= 5
            self.jump1 =False
            self.jump_bol=False
        elif self.points_bol[5]==True and self.move_bol[4]==True and self.jump_bol==True:
            self.vy=-10
            self.vx=-5
            self.jump1 =False
            self.jump_bol=False
            
        if self.move_bol[0]==True and self.move_bol[2]==True:
            self.vx =0
        elif self.move_bol[0]==True and self.points_bol[3] != True:
            self.vx=-5
        elif self.move_bol[2]==True and self.points_bol[5] != True:
            self.vx= 5
            
        if (self.move_bol[1]==True or self.move_bol[4]==True) and self.jump1==True and not (self.points_bol[3]==True or self.points_bol[5]==True) and self.jump_bol==True:
            self.vy =-10
            self.jump1=False
            self.jump_bol=False
        elif (self.move_bol[1]==True or self.move_bol[4]==True) and self.jump2==True and not (self.points_bol[3]==True or self.points_bol[5]==True) and self.jump_bol==True:
            self.vy =-10
            self.jump2=False
            self.jump_bol=False

        if self.move_bol[0]==False and self.move_bol[2]==False and self.points_bol[7]==True:
            self.vx= int(self.vx * 0.75)
        if self.move_bol[0]==False and self.move_bol[2]==False and self.points_bol[7]==False:
            if self.vx >0:
                self.vx=int(self.vx * 0.99)
            if self.vx <0:
                self.vx=int(self.vx * 0.99)
                
        if self.move_bol[1]==True:
            self.var=1
        elif self.move_bol[4]==True:
            self.var=2
            
        if self.var!=0:
            if self.jump_bol==False and self.move_bol[1]==False and self.var==1:
                self.jump_bol=True
                self.var=0
            if self.jump_bol==False and self.move_bol[4]==False and self.var==2:
                self.jump_bol=True
                self.var=0
            
        self.x+=self.vx
        self.y+=self.vy
        
class Wall:
    def __init__(self,x,y,w,h):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
    
    def draw(self):
        pygame.draw.rect(aken,[0,0,0], [self.x, self.y, self.w, self.h],0)
        
class WinArea:
    def __init__(self,x,y,w,h):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        
    def draw(self):
        pygame.draw.rect(aken,(71,209,255),[self.x, self.y, self.w, self.h],0)
        
    def win(self,player):
        if player.x in range(self.x,self.x+self.w) and player.y in range(self.y,self.y+self.h):
             return False
        else: return True
        
class LoseArea:
    def __init__(self,x,y,w,h):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        
    def draw(self):
        pygame.draw.rect(aken,(100,0,0),[self.x, self.y, self.w, self.h],0)
        
    def lose(self,player):
        if player.x in range(self.x,self.x+self.w) and player.y in range(self.y,self.y+self.h):
             player.__init__(80,400,(225,0,0))
        
player=Person(80,400,(225,0,0))
people=[player]

wall1 =Wall(0,450,330,40)
wall2 =Wall(160,400,80,200)
wall3 =Wall(200,250,150,50)
wall4 =Wall(550,250,70,50)
wall5 =Wall(450,0,40,150)
walls =[wall1,wall2,wall3,wall4,wall5]

win = WinArea(590,0,50,120)
lose =LoseArea(330,400,400,100)
areas =[win,lose]

töötab=True
while töötab:
    for e in pygame.event.get():
        töötab= win.win(player)
        if e.type == pygame.QUIT:
            töötab = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_w:
                player.move_bol[1]=True
            if e.key == pygame.K_a:
                player.move_bol[0]=True
            if e.key == pygame.K_d:
                player.move_bol[2]=True
            if e.key == pygame.K_s:
                player.move_bol[3]=True
            if e.key == pygame.K_SPACE:
                player.move_bol[4]=True
        elif e.type == pygame.KEYUP:
            if e.key == pygame.K_w:
                player.move_bol[1]=False
            if e.key == pygame.K_a:
                player.move_bol[0]=False
            if e.key == pygame.K_d:
                player.move_bol[2]=False
            if e.key == pygame.K_s:
                player.move_bol[3]=False
            if e.key == pygame.K_SPACE:
                player.move_bol[4]=False
    
    aken.fill([255,255,255])
    
    for a in areas:
        a.draw()
    for p in people:
        p.update(walls)
        p.move()
        p.draw()
    if player.x<0 or player.x>sw or player.y <0 or player.y> sh:
        player.__init__(80,400,(225,0,0))
        
    for s in walls:
        s.draw()
    lose.lose(player)
    pygame.display.flip()
    pygame.time.delay(17)
pygame.quit()