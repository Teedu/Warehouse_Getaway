import pygame

class Ruut:
    def __init__(self): # alustab ekraani keskel
        self.x =320
        self.y= 240
        
    def draw(self): # joonistab tegelase
        pygame.draw.rect(aken,[255,0,0],[ self.x-20, self.y-20, 40, 40],0)
        
    def tp(self): # peatab aknast välja mineku
        if self.x <0:
            self.x = 0
        if self.x >640:
            self.x = 640
        if self.y <0:
            self.y = 0
        if self.y >240:
            self.y = 240

    def update(self,vx,vy): # liikutab tegelast
        self.x += vx
        self.y += vy

pygame.init()

aken = pygame.display.set_mode([640,480]) # teeb akna

tüüp = Ruut() # teeb tegelase
VX=0 # x telje kiirus
VY=0 # y telje kiirus
XL=2 # kui kiiresti liigub

töötab=True

while töötab:
    for e in pygame.event.get():
        if e.type == pygame.QUIT: # lülitub välja korralikult kui kinni pannakse
            töötab = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP:
                VY += -XL 
            if e.key == pygame.K_DOWN:
                VY += XL
            if e.key == pygame.K_LEFT:
                VX += -XL
            if e.key == pygame.K_RIGHT:
                VX += XL
        elif e.type == pygame.KEYUP:
            if e.key == pygame.K_UP:
                VY -= -XL 
            if e.key == pygame.K_DOWN:
                VY -= XL
            if e.key == pygame.K_LEFT:
                VX -= -XL
            if e.key == pygame.K_RIGHT:
                VX -= XL
        
    tüüp.update(VX,VY)
    aken.fill([255,255,255])
    tüüp.draw()
    pygame.display.flip()
    pygame.time.delay(17)

pygame.quit()