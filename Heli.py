import pygame, sys

pygame.init()
pygame.mixer.init()
aken = pygame.display.set_mode([640, 480])

def lask():
    
    heli_laskmine = pygame.mixer.Sound("lask.wav")
    heli_laskmine.play()
    
def success():
        
    pygame.mixer.music.load("success.mp3")
    pygame.mixer.music.play()
     
def gameover():
        
    pygame.mixer.music.load("GameOVER.mp3")
    pygame.mixer.music.play()
     
def taustamuusika(self):
        
    pygame.mixer.music.load("taustamuusika.mp3")
    pygame.mixer.music.play(self)

while True:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_SPACE:
                taustamuusika(-1)
            

    