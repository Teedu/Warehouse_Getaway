import pygame, sys

pygame.init()
pygame.mixer.init() #laadime mixeri
aken = pygame.display.set_mode([640, 480]) #katsetuseks teeme ekraani
    
def success(): #võidu helifaili funktsioon
        
    pygame.mixer.music.load("success.mp3")#laeme sisse
    pygame.mixer.music.play()#kanname ette
     
def gameover(): #mängu läbikukkumise helifaili funktsioon
        
    pygame.mixer.music.load("GameOVER.mp3")
    pygame.mixer.music.play()
     
def taustamuusika(self): #taustamuusika helifaili funktsioon
        
    pygame.mixer.music.load("taustamuusika.mp3")
    pygame.mixer.music.play(self)

##while True:
##    for i in pygame.event.get():
##        if i.type==pygame.QUIT:
##            pygame.quit()
##            sys.exit()
##        if i.type == pygame.KEYDOWN:
##            if i.key == pygame.K_SPACE:
##                taustamuusika(-1)
##            

    