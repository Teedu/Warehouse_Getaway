import pygame, Heli, time

sw=640
sh=480

map = [[[('player',80,400,(225,0,0)),('wall',0,0,20,480),('wall',0,0,640,20),('wall',0,460,640,20),('wall',620,140,20,400),('wall',480,140,200,50),('wall',480,280,280,60),('wall',300,0,80,200),('wall',200,300,80,300),('wall',346,391,70,100),('lose area',280,404,350,100)],
        [('wall',0,0,640,20),('wall',0,140,20,400),('wall',0,140,150,50),('wall',620,0,20,100),('wall',520,150,100,50),('wall',620,150,20,500),('wall',0,460,280,20),('wall',340,460,300,20),('wall',400,300,240,50),('lose area',0,400,280,60),('lose area',340,400,280,60)],
        [('wall',0,0,20,100),('wall',0,0,640,20),('wall',620,0,20,400),('wall',0,460,680,20),('wall',0,150,20,330),('wall',20,240,80,220),('wall',100,320,80,140),('wall',180,400,80,60)]],
       [[('wall',0,0,400,20),('wall',0,0,20,480),('wall',0,460,640,20)],[]]
       ]

x=0
y=0

pygame.init()

window = pygame.display.set_mode([sw,sh])
taust = pygame.image.load("forest.png") ####################################### tausta laadimine
sein = pygame.image.load("sein.jpg")    ####################################### seina laadimine

class Person:
    def __init__(self,x,y,colour,drone=False,route=None):
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
        self.drone=drone
        self.route=route
        self.route_var=0
        if self.drone==True:
            self.set_goal()

    def draw(self):
        pygame.draw.rect(window,self.colour,[ self.x-20, self.y-20, 40, 40],0)

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
##        if self.move_bol[0]==False and self.move_bol[2]==False and self.points_bol[7]==False:
##            if self.vx >0:
##                self.vx=int(self.vx * 0.99)
##            if self.vx <0:
##                self.vx=int(self.vx * 0.99)

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

    def set_goal(self):
        try:self.goal =self.route[self.route_var]
        except IndexError:
            self.route_var=0
            self.set_goal()
        if self.goal[2] != None:
            self.t1 = time.time() + self.goal[2]

    def go(self):
        if self.goal[0] != None and self.goal[1] != None:
            if self.goal[0] < self.x:
                self.move_bol[0] = True
                self.move_bol[2] = False
            if self.goal[0] > self.x:
                self.move_bol[0] = False
                self.move_bol[2] = True
            if self.goal[0] == self.x:
                self.move_bol[0] = False
                self.move_bol[2] = False
            if self.goal[1] < self.y:
                self.move_bol[1] = True
                self.move_bol[3] = False
            if self.goal[1] > self.y:
                self.move_bol[1] = False
                self.move_bol[3] = True
            if self.goal[y] == self.y:
                self.move_bol[1] = False
                self.move_bol[3] = False
            if self.goal[0]==self.x and self.goal[1]==self.y:
                self.route_var+=1
                self.set_goal()
        elif self.goal[2] != None:
            if self.t1 < time.time():
                self.route_var+=1
                self.set_goal()

class Wall:
    def __init__(self,x,y,w,h):
        self.x=x
        self.y=y
        self.w=w
        self.h=h

    def draw(self):
        pygame.draw.rect(window,[0,0,0], [self.x, self.y, self.w, self.h],0)
        window.blit(sein, (self.x, self.y))                                     ###################################### seina lisamine

class WinArea:
    def __init__(self,x,y,w,h):
        self.x=x
        self.y=y
        self.w=w
        self.h=h

    def draw(self):
        pygame.draw.rect(window,(71,209,255),[self.x, self.y, self.w, self.h],0)

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
        pygame.draw.rect(window,(100,0,0),[self.x, self.y, self.w, self.h],0)

    def lose(self,player):
        if player.x in range(self.x,self.x+self.w) and player.y in range(self.y,self.y+self.h):
            player.__init__(80,400,(225,0,0))
            global x
            x=0
            global y
            y=0
            Heli.gameover()
            time.sleep(0.5)
            Heli.taustamuusika()

def set_room(name):
    ls=[]
    if name == 'walls':
        for i in map[y][x]:
            if i[0] == 'wall':
                ls.append(Wall(i[1],i[2],i[3],i[4]))
        return ls
    elif name == 'player':
        for i in map[y][x]:
            if i[0] == 'player':
                return Person(i[1],i[2],i[3])
    elif name == 'areas':
        for i in map[y][x]:
            if i[0] == 'lose area':
                ls.append(LoseArea(i[1],i[2],i[3],i[4]))
            if i[0] == 'win area':
                ls.append(WinArea(i[1],i[2],i[3],i[4]))
        return ls
    elif name == 'drones':
        for i in map[y][x]:
            if i[0] == 'drone':
                ls.append(person(i[1],i[2],i[3],True,i[4]))
        return ls

player=set_room('player')
people=set_room('drones')
people.append(player)

walls =set_room('walls')

areas =set_room('areas')

Heli.taustamuusika(-1)

on=True
while on:
    for e in pygame.event.get():
        try:on= win.win(player)
        except NameError:on=True
        if e.type == pygame.QUIT:
            on = False
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
            if e.key == pygame.K_r:
                x=0
                y=0
                walls =set_room('walls')
                areas =set_room('areas')
                people=set_room('drones')
                people.append(player)
                player.__init__(80,400,(225,0,0))
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

    window.fill([255,255,255])
    window.blit(taust, (0, 0))  ###################################### tausta kuvamine

    for a in areas:
        a.draw()
    for p in people:
        if p.drone==True:
            p.go
        p.move()
        p.update(walls)
        p.draw()

    if player.x < 0:
        x-=1
        player.x = sw
        walls =set_room('walls')
        areas =set_room('areas')
        people=set_room('drones')
        people.append(player)
    elif player.x>sw:
        x+=1
        player.x=0
        walls =set_room('walls')
        areas =set_room('areas')
        people=set_room('drones')
        people.append(player)
    if player.y<0:
        y-=1
        player.y=sh
        walls =set_room('walls')
        areas =set_room('areas')
        people=set_room('drones')
        people.append(player)
    elif player.y>sh:
        y+=1
        player.y=0
        walls =set_room('walls')
        areas =set_room('areas')
        people=set_room('drones')
        people.append(player)

    for s in walls:
        s.draw()
    try:
        for i in areas:
            i.lose(player)
    except NameError:pass

    pygame.display.flip()
    print(pygame.mouse.get_pos())
    pygame.time.delay(17)
pygame.quit()
