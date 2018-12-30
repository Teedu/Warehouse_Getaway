import pygame
from Heli import taustamuusika    #impordime muusika funktsiooni

pygame.init()
window = pygame.display.set_mode([640, 480])  #teeme akna
red = [255,0,0]
taust = pygame.image.load("menüütaust.png")  #laadime tausta

def menüü():
    
    taustamuusika(-1) #muusika käima nii kauaks kui while loop kestab
    
    menu = True 
    while menu:
        for i in pygame.event.get(): #et saaks kinni panna ristist
            if i.type==pygame.QUIT:
                pygame.quit()
                sys.exit()

        window.fill([255,255,255]) #täidame akna valgega
        window.blit(taust,(0,0)) #lisame taustapildi
        pygame.draw.rect(window, red, (270, 200, 100, 40), 2) #joonistame kolm kasti nuppude jaoks
        pygame.draw.rect(window, red, (270, 250, 100, 40), 2)
        pygame.draw.rect(window, red, (270, 300, 100, 40), 2)
        
        hiir = pygame.mouse.get_pos() #küsime hiire andmeid
        klik = pygame.mouse.get_pressed() 
        
        if 270+100 > hiir[0] > 270 and 200+40 > hiir[1] > 200: #kui selles piirkonnas ollakse hiirega siis täitub kast punase värviga
            pygame.draw.rect(window, red, (270, 200, 100, 40), 0) 
            if klik[0] == 1: #kui seal alas klikata siis menüü lõpetab töötamise ja loopist minnakse välja
                menu = False 
                
        elif 270+100 > hiir[0] > 270 and 250+40 > hiir[1] > 200: #sama
            pygame.draw.rect(window, red, (270, 250, 100, 40), 0) 
            if klik[0] == 1: #klikates seal alas läheb käima uus while loop, millega tekib uus ekraan, kus kuvatakse pilti millega tegelast kontrollida saab
                menu2 = True
                while menu2:
                    for i in pygame.event.get(): #et ikka sulgeda saaks ka
                        if i.type==pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        if i.type == pygame.MOUSEBUTTONDOWN: #ükskõik mis hiire klahvi klikates saab loopist välja ja tagasi tuleb esialgne menüü vaade
                            menu2 = False
                    window.fill([255,255,255])
                    klahvid = pygame.image.load("wasd.png") #photoshopis enda tehtud pilt
                    window.blit(klahvid, (0, 0))
                    pygame.display.update()
                
                            
        elif 270+100 > hiir[0] > 270 and 300+40 > hiir[1] > 200:
            pygame.draw.rect(window, red, (270, 300, 100, 40), 0) 
            if klik[0] == 1: #klikates seal alas läheb pygame ehk üldse mäng kinni
                pygame.quit()
        
        window.blit(pygame.font.Font(None, 70).render("Warehouse Getaway", 1,[0,0,0]), (85, 120)) #mängu pealkirja kuvamine
        window.blit(pygame.font.Font(None, 30).render("Start", 1,[0,0,0]), (295, 210)) #mängu menüü nuppude pealkirjastamine
        window.blit(pygame.font.Font(None, 30).render("Controls", 1,[0,0,0]), (277, 262))
        window.blit(pygame.font.Font(None, 30).render("Quit", 1,[0,0,0]), (297, 312))
        
        pygame.display.update()

menüü()
     

    