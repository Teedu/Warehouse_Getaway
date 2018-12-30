import pygame, time
from Heli import success

pygame.init()
window = pygame.display.set_mode([640, 480]) #loome akna
red = [255,0,0] #anname sõnale red punase värvi väärtuse et oleks lihtsam kasutada.
taust = pygame.image.load("menüütaust.png") #laeme tausta

def võiduekraan(koguaeg): #funktsioon algab
    
    success() #võidu helifail
    
    menu = True 
    while menu: #loop algab
        for i in pygame.event.get():#vajalik et saaks ikka akent sulgeda alati
            if i.type==pygame.QUIT:
                pygame.quit()
                sys.exit()

        window.fill([255,255,255]) #täidame ekraani valgega
        window.blit(taust,(0,0)) #lisame taustapildi
        pygame.draw.rect(window, red, (270, 200, 100, 40), 2) #joonistame nupud
        pygame.draw.rect(window, red, (270, 250, 100, 40), 2)
        
        
        hiir = pygame.mouse.get_pos() #küsime hiire andmeid
        klik = pygame.mouse.get_pressed()
        
        if 270+100 > hiir[0] > 270 and 200+40 > hiir[1] > 200: #kui hiir asub sellisel alal siis muutub see nupp niiöelda aktiivseks täites selle punase värviga
            pygame.draw.rect(window, red, (270, 200, 100, 40), 0)
            if klik[0] == 1: #kui klikata sellele nupule läheb menüü kinni
                menu = False
        elif 270+100 > hiir[0] > 270 and 250+40 > hiir[1] > 250: #sama
            pygame.draw.rect(window, red, (270, 250, 100, 40), 0)
            if klik[0] == 1: #klikates läheb terve mäng kinni
                pygame.quit()
                 
        window.blit(pygame.font.Font(None, 70).render("You won!", 1,[0,0,0]), (210, 120)) #pealkiri võidumenüüle
        window.blit(pygame.font.Font(None, 30).render("Retry", 1,[0,0,0]), (295, 211)) # nuppude nimetused
        window.blit(pygame.font.Font(None, 30).render("Quit", 1,[0,0,0]), (297, 262))
        window.blit(pygame.font.Font(None, 30).render(koguaeg, 1,[0,0,0]), (320, 170)) #kuvame aega sekundites
        window.blit(pygame.font.Font(None, 30).render("Time:", 1,[0,0,0]), (255, 170)) #lisa selgitus, mida kuvatakse
        
        pygame.display.update()