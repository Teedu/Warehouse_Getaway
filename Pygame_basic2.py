import pygame

class Ruut(pygame.sprite.Sprite):
    
    def __init__(self, x, y): 
        
        super().__init__() 
        
        pygame.sprite.Sprite.__init__(self) #
        
        self.image = pygame.Surface([15, 15]) #loob selle kujutise
        self.image.fill([255,0,0]) #teeb selle punaseks
        
        self.rect = self.image.get_rect() #moodustab sellest ristküliku
        self.rect.y = y  #külgede väärtused
        self.rect.x = x
        
        self.kiirus_x = 0 #seda pole vaja vist sest kiirus on teises funktsioonis
        self.seinad = None
        
    def tp(self):
        if self.rect.x <20:
            self.rect.x = 20
        if self.rect.x >sx-20:
            self.rect.x = sx-20
        if self.rect.y > sy-20:
            self.rect.y = sy-20

    def update(self,VX,VY, seinad):
        self.rect.x += VX # liikumine
        self.rect.y += VY
        if jump != False: # hüppamine põrandal tööab
            VY=0
        
        #Seina puudutamise osa
            
        #paremale vasakule
        self.rect.x += self.rect.x
        
        seina_list = pygame.sprite.spritecollide(self, self.seinad, False)
        for sein in seina_list:
            if self.rect.x > sx/2:
                self.rect.right = sein.rect.left #kui ruut puudutab paremaküljega seina siis annab ruudule seina vasakupoole kodinaadid ehk ei saa läbi minna 
            else:
                self.rect.left = sein.rect.right #sama aga teistpid
        
        #Üles ALLA
        self.rect.y += self.rect.y
        
        seina_list = pygame.sprite.spritecollide(self, self.seinad, False)
        for sein in seina_list:
            if self.rect.y > sy/2:
                self.rect.bottom = sein.rect.top #sama aga y suunas
            else:
                self.rect.top = sein.rect.bottom
        
class Sein(pygame.sprite.Sprite):
    
    def __init__(self, x, y, width, heigth): 
        
        pygame.sprite.Sprite.__init__(self) #teeb sprite-i
        
        self.image = pygame.Surface([width, heigth])
        self.image.fill([0,0,255])
        
        self.rect = self.image.get_rect() #sama mis ruuduga
        self.rect.x = x
        self.rect.y = y
          
pygame.init()

aknaSuurus = pygame.display.Info()
sx = aknaSuurus.current_w # akna suurus x vastavalt monitorile
sy = aknaSuurus.current_h # akna suurus y vastavalt monitorile

#aken = pygame.display.set_mode([sx,sy])
aken = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) #kuvab mängu täisekraanil

VX=0
VY=0
XL=5

sprite_list = pygame.sprite.Group() #paneb listi sprite groupi 
seina_list = pygame.sprite.Group()

sein = Sein(760,1000,1000,50) #Loome seina selliste atribuutidega
seina_list.add(sein)     #SEin lisatakse listi
sprite_list.add(sein)     #Spritelisti ka

sein = Sein(320,400,1000,50)
seina_list.add(sein)
sprite_list.add(sein)

tüüp = Ruut(100, 100) #Loob ruudu mille nimi on tüüp
tüüp.seinad = seina_list 

sprite_list.add(tüüp) 

jump=False

töötab=True

while töötab:
    #if tüüp.y == 460 :                                                                    <=================
        #jump=True                                                                         <=================
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
    
    
    VY += 1 # gravitatsioon
    #sprite_list.update(VX, VY, seina_list)                                             # <=================
    #tüüp.tp()                                                                           <=================
    aken.fill([255,255,255])
    sprite_list.draw(aken) #joonistab spritid
    pygame.display.flip()
    pygame.time.delay(17)
    
pygame.quit()


