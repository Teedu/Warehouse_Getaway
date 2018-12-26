import pygame, sys

pygame.init()
pygame.mixer.init()
aken = pygame.display.set_mode([640, 480])

def lask():
    
    heli_laskmine = pygame.mixer.Sound("lask.wav")
    heli_laskmine.play()
    
def kõndimine(self):
        
    heli_kõndimine = pygame.mixer.Sound("")
    heli_kõndimine.play() 
     
def gameover(self):
        
    heli_gameover = pygame.mixer.Sound("")
    heli_gameover.play() 
     
def taustamuusika(self):
        
    pygame.mixer.music.load("")
    pygame.mixer.music.play()

while True:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

    lask()