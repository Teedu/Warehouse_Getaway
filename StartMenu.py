import pygame
from Heli import taustamuusika

pygame.init()
window = pygame.display.set_mode([640, 480])
red = [255,0,0]
taust = pygame.image.load("menüütaust.png")

def menüü():
    
    taustamuusika(-1)
    
    menu = True 
    while menu:
        for i in pygame.event.get():
            if i.type==pygame.QUIT:
                pygame.quit()
                sys.exit()

        window.fill([255,255,255])
        window.blit(taust,(0,0))
        pygame.draw.rect(window, red, (270, 200, 100, 40), 2)
        pygame.draw.rect(window, red, (270, 250, 100, 40), 2)
        pygame.draw.rect(window, red, (270, 300, 100, 40), 2)
        
        hiir = pygame.mouse.get_pos()
        klik = pygame.mouse.get_pressed()
        
        if 270+100 > hiir[0] > 270 and 200+40 > hiir[1] > 200:
            pygame.draw.rect(window, red, (270, 200, 100, 40), 0)
            if klik[0] == 1:
                menu = False
                
        elif 270+100 > hiir[0] > 270 and 250+40 > hiir[1] > 200:
            pygame.draw.rect(window, red, (270, 250, 100, 40), 0)
            if klik[0] == 1:
                menu2 = True
                while menu2:
                    for i in pygame.event.get():
                        if i.type==pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        if i.type == pygame.MOUSEBUTTONDOWN:
                            menu2 = False
                    window.fill([255,255,255])
                    klahvid = pygame.image.load("wasd.png")
                    window.blit(klahvid, (0, 0))
                    pygame.display.update()
                
                            
        elif 270+100 > hiir[0] > 270 and 300+40 > hiir[1] > 200:
            pygame.draw.rect(window, red, (270, 300, 100, 40), 0)
            if klik[0] == 1:
                pygame.quit()
        
        window.blit(pygame.font.Font(None, 70).render("Mad Mayhem", 1,[0,0,0]), (170, 120))
        window.blit(pygame.font.Font(None, 30).render("Start", 1,[0,0,0]), (295, 210))
        window.blit(pygame.font.Font(None, 30).render("Controls", 1,[0,0,0]), (277, 262))
        window.blit(pygame.font.Font(None, 30).render("Quit", 1,[0,0,0]), (297, 312))
        
        pygame.display.update()

menüü()
     

    