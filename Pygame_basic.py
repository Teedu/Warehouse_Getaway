import pygame

class Ruut:
    def __init__(self):
        self.x =320
        self.y= 240
        
    def draw(self):
        pygame.draw.rect(aken,[255,0,0],[ self.x-20, self.y-20, 40, 40],0)
        
    def tp(self):
        if self.x <0:
            self.x = 640
        if self.x >640:
            self.x = 0
        if self.y <0:
            self.y = 240
        if self.y >240:
            self.y = 0

    def update(self,vx,vy):
        self.x += vx
        self.y += vy

pygame.init()

aken = pygame.display.set_mode([640,480])

tüüp = Ruut()
VX=0
VY=0
XL=2

töötab=True

while töötab:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
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