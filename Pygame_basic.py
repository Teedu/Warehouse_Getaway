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
        if self.x <20:
            self.x = 20
        if self.x >620:
            self.x = 620
        if self.y >460:
            self.y = 460

    def update(self,vx,vy):
        self.x += vx # liikumine
        self.y += vy
        if jump != False: # hüppamine põrandal tööab
            VY=0
        

pygame.init()

aken = pygame.display.set_mode([sx,sy])

tüüp = Ruut()
VX=0
VY=0
XL=5


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
    VY += 1
    tüüp.update(VX,VY)
    tüüp.tp()
    aken.fill([255,255,255])
    tüüp.draw()
    pygame.display.flip()
    pygame.time.delay(17)
    
pygame.quit()


