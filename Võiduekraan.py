import pygame, time
from Heli import success

pygame.init()
window = pygame.display.set_mode([640, 480])
red = [255,0,0]
taust = pygame.image.load("menüütaust.png")

def võiduekraan(koguaeg):
    
    success()
    
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
        
        
        hiir = pygame.mouse.get_pos()
        klik = pygame.mouse.get_pressed()
        
        if 270+100 > hiir[0] > 270 and 200+40 > hiir[1] > 200:
            pygame.draw.rect(window, red, (270, 200, 100, 40), 0)
            if klik[0] == 1:
                menu = False
        elif 270+100 > hiir[0] > 270 and 250+40 > hiir[1] > 250:
            pygame.draw.rect(window, red, (270, 250, 100, 40), 0)
            if klik[0] == 1:
                pygame.quit()
                 
        window.blit(pygame.font.Font(None, 70).render("You won!", 1,[0,0,0]), (210, 120))
        window.blit(pygame.font.Font(None, 30).render("Retry", 1,[0,0,0]), (295, 211))
        window.blit(pygame.font.Font(None, 30).render("Quit", 1,[0,0,0]), (297, 262))
        window.blit(pygame.font.Font(None, 30).render(koguaeg, 1,[0,0,0]), (320, 170))
        window.blit(pygame.font.Font(None, 30).render("Time:", 1,[0,0,0]), (255, 170))
        
        pygame.display.update()