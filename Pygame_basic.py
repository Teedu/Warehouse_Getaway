import pygame

sx= 640 # akna suurus x
sy = 480 # akna suurus y

class Ruut:
    def __init__(self): # alustab ekraani keskel
        self.x =sx/2
        self.y= sy/2
        
    def draw(self): 
        pygame.draw.rect(aken,[255,0,0],[ self.x-20, self.y-20, 40, 40],0)
        
    def tp(self):
        if self.x < 20: # ei lase tegelast akna äärtest välja
            self.x = 20
        if self.x > sx-20:
            self.x = sx-20
        if self.y > sy-20:
            self.y = sy-20
        
        for s in seinad:
            if self.punktid[7][0] in range(s.x,(s.x+s.w)) and self.punktid[7][1] in range(s.y,(s.y+s.h)):
                self.y = s.y-20
                self.vy = 0
            elif self.punktid[5][0] in range(s.x,(s.x+s.w)) and self.punktid[5][1] in range(s.y,(s.y+s.h)):
                self.x = s.x-20
            elif self.punktid[3][0] in range(s.x,(s.x+s.w)) and self.punktid[3][1] in range(s.y,(s.y+s.h)):
                self.x = s.x+s.w+20
            elif self.punktid[1][0] in range(s.x,(s.x+s.w)) and self.punktid[1][1] in range(s.y,(s.y+s.h)):
                self.y = s.y+s.h+20
                self.vy = 0


    def update(self,vx,vy):
        self.vx = vx
        self.vy = vy
        self.x += self.vx # liikumine
        self.y += self.vy
        if jump != False: # hüppamine põrandal tööab
            VY=0
        self.punktid = [[self.x-20, self.y-20],[self.x, self.y-20],[self.x+20, self.y-20],
                        [self.x-20, self.y],   [self.x, self.y],   [self.x+20, self.y],
                        [self.x-20, self.y+20],[self.x, self.y+20],[self.x+20, self.y+20]]
            
class Sein:
    def __init__(self, x, y, w, h):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        
    def draw(self):
        pygame.draw.rect(aken,[0,0,0],[ self.x, self.y, self.w, self.h],0)
        
pygame.init()

aken = pygame.display.set_mode([sx,sy])

tüüp = Ruut()
VX=0
VY=0
XL=5

sein =Sein(400,150,110,200)
seinad = [sein]

jump=False


töötab=True

while töötab:
    if tüüp.y == 460:
        jump=True
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            töötab = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP:
                jump = False
                VY = -15
            if e.key == pygame.K_LEFT:
                VX += -XL
            if e.key == pygame.K_RIGHT:
                VX += XL
        elif e.type == pygame.KEYUP:
            if e.key == pygame.K_LEFT:
                VX -= -XL
            if e.key == pygame.K_RIGHT:
                VX -= XL
    VY += 1 # gravitatsioon
    tüüp.update(VX,VY)
    tüüp.tp()
    aken.fill([255,255,255])
    sein.draw()
    tüüp.draw()
    pygame.display.flip()
    pygame.time.delay(17)
pygame.quit()


