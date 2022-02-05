import pygame
# import numpy as np
import os, inspect
# import pygame.surfarray as surfarray
from random import randint

#recherche du répertoire de travail
scriptPATH = os.path.abspath(inspect.getsourcefile(lambda:0)) # compatible interactive Python Shell
scriptDIR  = os.path.dirname(scriptPATH)
assets = os.path.join(scriptDIR,"data")
planche_sprites = pygame.image.load(os.path.join(assets, "spritep1.bmp"))
planche_sprites.set_colorkey((0,0,0))

LARG = 300
def ChargeSerieSprites(id):
    sprite = []
    for i in range(23):
        spr = planche_sprites.subsurface(( LARG* i, LARG * id, LARG, LARG))
        test = spr.get_at((10,10))
        if ( test != (255,0,0,255) ):
            sprite.append( spr )
    return sprite

    



## Initialisation


pygame.mixer.pre_init(frequency = 22050, size = -16, channels = 2, buffer = 1)
pygame.init()

WINDOW_SIZE = [800, 500]
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Goodman Fighter Alpha 1")

clock = pygame.time.Clock()

fond_jap = pygame.image.load(os.path.join(assets, "fond.png"))
fond_us = pygame.image.load(os.path.join(assets,"fond1.png"))
fond=fond_jap

barre = pygame.image.load(os.path.join(assets, "barre de vie.png"))

menu1 = pygame.image.load(os.path.join(assets, "menu1.png"))
menu2 = pygame.image.load(os.path.join(assets, "menu2.png"))
menu3 = pygame.image.load(os.path.join(assets,"menu3.png"))

levelselect1 = pygame.image.load(os.path.join(assets,"levelselect1.png"))
levelselect2 = pygame.image.load(os.path.join(assets,"levelselect2.png"))


tuto1 = pygame.image.load(os.path.join(assets,"Tuto 1.png"))
tuto2 = pygame.image.load(os.path.join(assets,"Tuto 2.png"))
tuto3 = pygame.image.load(os.path.join(assets,"Tuto 3.png"))
tuto4 = pygame.image.load(os.path.join(assets,"Tuto 4.png"))
tuto5 = pygame.image.load(os.path.join(assets,"Tuto 5.png"))
tuto6 = pygame.image.load(os.path.join(assets,"Tuto 6.png"))





round1 = pygame.image.load(os.path.join(assets, "ROUND1.png"))
round1.set_colorkey((0,0,0))
round2 = pygame.image.load(os.path.join(assets, "ROUND2.png"))
round2.set_colorkey((0,0,0))
round3 = pygame.image.load(os.path.join(assets, "ROUND3.png"))
round3.set_colorkey((0,0,0))
fight = pygame.image.load(os.path.join(assets,"FIGHT.png"))
fight.set_colorkey((0,0,0))
ko = pygame.image.load(os.path.join(assets,"KO.png"))
ko.set_colorkey((0,0,0))

p1_win = pygame.image.load(os.path.join(assets,"p1wins.bmp"))
p2_win = pygame.image.load(os.path.join(assets,"p2wins.bmp"))
p1_win.set_colorkey((0,0,0))
p2_win.set_colorkey((0,0,0))


round1_son = pygame.mixer.Sound(os.path.join(assets,"round1.ogg"))
round2_son = pygame.mixer.Sound(os.path.join(assets,"round2.ogg"))
round3_son = pygame.mixer.Sound(os.path.join(assets,"round3.ogg"))






# pygame.mixer.music.play()
sonfk_start1 = pygame.mixer.Sound(os.path.join(assets,"General 23.wav"))
sonfk_end1 = pygame.mixer.Sound(os.path.join(assets,"2AH.wav"))
sonnj1 = pygame.mixer.Sound(os.path.join(assets,"2BHH.wav"))
sonlj1 = pygame.mixer.Sound(os.path.join(assets,"2BHH.wav"))
sonsk1 = pygame.mixer.Sound(os.path.join(assets,"2BHH.wav"))
sonsj1 = pygame.mixer.Sound(os.path.join(assets,"2BHH.wav"))
sonnk1 = pygame.mixer.Sound(os.path.join(assets,"2EH.wav"))
sonlk1 = pygame.mixer.Sound(os.path.join(assets,"2LK.wav"))
sonlfj1 = pygame.mixer.Sound(os.path.join(assets,"3LFJ.wav"))
sonfj1 = pygame.mixer.Sound(os.path.join(assets,"6FJ.wav"))


sonfk_start2 = pygame.mixer.Sound(os.path.join(assets,"General 23.wav"))
sonfk_end2 = pygame.mixer.Sound(os.path.join(assets,"2AH.wav"))
sonnj2 = pygame.mixer.Sound(os.path.join(assets,"2BHH.wav"))
sonlj2 = pygame.mixer.Sound(os.path.join(assets,"2BHH.wav"))
sonsk2 = pygame.mixer.Sound(os.path.join(assets,"2BHH.wav"))
sonsj2 = pygame.mixer.Sound(os.path.join(assets,"2BHH.wav"))
sonnk2 = pygame.mixer.Sound(os.path.join(assets,"2EH.wav"))
sonlk2 = pygame.mixer.Sound(os.path.join(assets,"2LK.wav"))
sonlfj2 = pygame.mixer.Sound(os.path.join(assets,"3LFJ.wav"))
sonfj2 = pygame.mixer.Sound(os.path.join(assets,"6FJ.wav"))

terre1 = pygame.mixer.Sound(os.path.join(assets,"terre.wav"))
terre2 = pygame.mixer.Sound(os.path.join(assets,"terre.wav"))

garde1 = pygame.mixer.Sound(os.path.join(assets,"garde.wav"))
garde2 = pygame.mixer.Sound(os.path.join(assets,"garde.wav"))


fw = fond.get_width()
fh = fond.get_height()


liste_sprites = []
for a in range (planche_sprites.get_height()//300):
    
    liste_sprites.append( ChargeSerieSprites(a) )


p1_coup = 0
p2_coup = 0
candechop = True

# Création des états
libre = 0
recov = 1
avanc = 2
recul = 3
gardeh = 4
gardel = 5
terre = 6
sautup = 7
sautdown = 18
prepa = 8
hitstunh = 9
hitstunl = 10
blockstunh = 11
blockstunl = 12
accroupi = 13
projet = 14
chute = 15
grabber = 16
grabbed = 17

# Création des coups
mid = 0
low = 1
ovh = 2
throw = 3


# nj - normal sans direction
# Un coup de poing léger
nj = {}
nj["degat"] = 300
nj["cible"] = mid
nj["startup"] = 5
nj["active"] = 1
nj["recovery"] = 6
nj["hitstun"] = 18
nj["blockstun"] = 12


# fj - normal avant
# Collarbone breaker
fj={}
fj["degat"] = 600
fj["cible"] = ovh
fj['startup'] = 19
fj['active'] = 1
fj['recovery'] = 17
fj['hitstun'] = 18
fj['blockstun'] = 13


# lj - normal bas
# Crouch kick
lj={}
lj['degat'] = 500
lj['cible'] = low
lj['startup'] = 6
lj['active'] = 1
lj['recovery'] = 15
lj['hitstun'] = 16
lj['blockstun'] = 12


# lfj - normal bas-avant
# Anti-air
lfj={}
lfj['degat'] = 900
lfj['cible'] = mid
lfj['startup'] = 6
lfj['active'] = 1
lfj['recovery'] = 22
lfj['hitstun'] = 18
lfj['blockstun'] = 13



# sj - normal saut
# 
sj = {}
sj['degat'] = 800
sj['cible'] = ovh
sj['startup'] = 4
sj['recovery'] = 4
sj['hitstun'] = 20
sj['blockstun'] = 15



# nk - special sans direction
# Balayette
nk={}
nk['degat'] = 1000
nk['cible'] = low
nk['startup'] = 8
nk['active'] = 1
nk['recovery'] = 22
nk['hitstun'] = 40
nk['blockstun'] = 11


# fk - special avant
# Joudan sokutogeri
fk = {}
fk["degat"] = 1000
fk["cible"] = mid
fk["startup"] = 28
fk["active"] = 1
fk["recovery"] = 40
fk["hitstun"] = 40
fk["blockstun"] = 30


# lk - special bas
# throw
lk = {}
lk['degat'] = 1200
lk['cible'] = throw
lk['startup'] = 4
lk['active'] = 1
lk['recovery'] = 18



# sk - spécial saut
# 
sk = {}
sk['degat'] = 500
sk['cible'] = ovh
sk['startup'] = 4
sk['recovery'] = 4
sk['hitstun'] = 20
sk['blockstun'] = 15




p1_score = 0
p2_score = 0

starty = 138


done = False

play = False
tuto = False
menud_hold = False
menuj_hold = False
menu_selection = 1
buffer = 50



## Main Screen
while not done:
    
    if (pygame.mixer.music.get_busy()) :    
        pygame.mixer.music.stop()
    
    event = pygame.event.Event(pygame.USEREVENT)    # Remise à zero de la variable event

    for event in pygame.event.get():  # User did something

        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    

    if menud_hold :
        if not (KeysPressed[pygame.K_w] or KeysPressed[pygame.K_s]):
            menud_hold = False
            
    if menuj_hold:
        if not (KeysPressed[pygame.K_j]):
            menuj_hold = False


    KeysPressed = pygame.key.get_pressed()
    if KeysPressed[pygame.K_w] and not menud_hold:
        if menu_selection == 2:
            menu_selection = 1
        elif menu_selection == 3:
            menu_selection = 2
    elif KeysPressed[pygame.K_s] and not menud_hold:
        if menu_selection == 1:
            menu_selection = 2
        elif menu_selection == 2:
            menu_selection = 3
    
    
    menud_hold = KeysPressed[pygame.K_w] or KeysPressed[pygame.K_s]

    if KeysPressed[pygame.K_j] and buffer >= 50:
        if menu_selection == 1:
            round = 1
            p1_score = 0
            p2_score = 0
            play = True
        elif menu_selection == 2:
            tuto = True
            count = 0
        elif menu_selection ==3:
            done= True
            
    buffer+=1
            
    if menu_selection == 1:
        screen.blit(menu1,(0,0))
    elif menu_selection == 2:
        screen.blit(menu2,(0,0))
    elif menu_selection == 3:
        screen.blit(menu3,(0,0))

    pygame.display.flip()
    menuj_hold = True
    
    ## Tutoriel
    while not done and tuto and count <=5:
        event = pygame.event.Event(pygame.USEREVENT)    # Remise à zero de la variable event
        buffer = 0
        for event in pygame.event.get():  # User did something
    
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
                
        KeysPressed = pygame.key.get_pressed()
                
        if menuj_hold:
            if not KeysPressed[pygame.K_j]:
                menuj_hold = False
        
        if not menuj_hold and KeysPressed[pygame.K_j]:
            count +=1
            menuj_hold = True
    
        if count == 0:
            screen.blit(tuto1,(0,0))
        elif count == 1:
            screen.blit(tuto2,(0,0))
        elif count == 2:
            screen.blit(tuto3,(0,0))
        elif count ==3:
            screen.blit(tuto4,(0,0))
        elif count ==4:
            screen.blit(tuto5,(0,0))
        elif count == 5:
            screen.blit(tuto6,(0,0))
        pygame.display.flip()
    
    
    ## Level selection
    

    
    while not done and play:
        
        event = pygame.event.Event(pygame.USEREVENT)    # Remise à zero de la variable event
    
        for event in pygame.event.get():  # User did something
    
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
                
        KeysPressed = pygame.key.get_pressed()
                
        if menuj_hold:
            if not KeysPressed[pygame.K_j]:
                menuj_hold = False
                
        if (KeysPressed[pygame.K_a] or KeysPressed[pygame.K_d]) and not menud_hold:
            if menu_selection == 1:
                menu_selection = 2
            else:
                menu_selection = 1
                
        menud_hold = KeysPressed[pygame.K_a] or KeysPressed[pygame.K_d]
                
        if KeysPressed[pygame.K_j] and not menuj_hold:
            if menu_selection == 1:
                fond = fond_jap
                musique = pygame.mixer.music.load(os.path.join(assets, "SF2court_ogg.ogg"))
    
            elif menu_selection == 2:
                fond = fond_us
                musique = pygame.mixer.music.load(os.path.join(assets, "Guile.ogg"))
            break
        
        
        if menu_selection == 1:
            round = 1
            screen.blit(levelselect1,(0,0))
        elif menu_selection == 2:
            screen.blit(levelselect2,(0,0))
        pygame.display.flip()
        
        
    
    
        
    ## CountDown
    while not done and not(p1_score>=2 or p2_score>=2) and play:    
    
        event = pygame.event.Event(pygame.USEREVENT)    # Remise à zero de la variable event
    
        for event in pygame.event.get():  # User did something
    
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
    
        count = 0
        jdx = 350
        jdy = 0
            
        # Création du p1
        p1_x = fw//2 - 200
        p1_y = starty
        p1_etat = libre
        p1_pv = 10000
        p1_sprite = liste_sprites[0][0]
        p1_son = sonfk_end1
        p1_hitbox = 80
        
        # Création du p2
        p2_x = fw//2 + 100
        p2_y = starty
        p2_etat = libre
        p2_pv = 10000
        p2_sprite = liste_sprites[1][0]
        p2_son = sonfk_end2
        p2_hitbox = 80
        
        done = False
        
        
        c = 0
        
        
        p1_direction = 1
        p2_direction = -1
        
        p1_hold = False
        p2_hold = False
        
        
        p1_sj = False
        p2_sj = False
        
        
        p1_sk = False
        p2_sk = False
    
        
        while not done and play:
            if count>=160:
                break
            if count == 35:
                if round ==1:
                    round1_son.play()
                elif round ==2:
                    round2_son.play()
                elif round==3:
                    round3_son.play()
            
            if not(pygame.mixer.music.get_busy()) :    
                pygame.mixer.music.play()
            zonejaune = pygame.Rect( jdx, jdy, WINDOW_SIZE[0], WINDOW_SIZE[1] )
            screen.blit(fond,(0,0), area = zonejaune)
            screen.blit(barre,(40,40))
            screen.blit(barre,(WINDOW_SIZE[0] - 40 - barre.get_width(),40))
            screen.blit(p1_sprite,(p1_x-jdx  ,p1_y))
            screen.blit(pygame.transform.flip(p2_sprite,True,False),(p2_x-jdx -205 ,p2_y))
            if count>=20:
                if count<=110:
                    if round == 1:
                        screen.blit(round1,(0,0))
                    elif round == 2:
                        screen.blit(round2,(0,0))
                    elif round ==3:
                        screen.blit(round3,(0,0))
                else:
                    screen.blit(fight,(0,0))
            pygame.display.flip()
            count+=1
            
        
        
        ## In-game
        
        while not done and play:
            event = pygame.event.Event(pygame.USEREVENT)    # Remise à zero de la variable event
        
            for event in pygame.event.get():  # User did something
        
                if event.type == pygame.QUIT:  # If user clicked close
                    done = True  # Flag that we are done so we exit this loop
        
            time = int( pygame.time.get_ticks() / 100 )
        
            # Logique
            
            if not(pygame.mixer.music.get_busy()) :    
                pygame.mixer.music.play()
                
                
                
            if not (p1_etat == terre) :
                p1_hitbox = 80
            
            if not (p2_etat == terre) :
                p2_hitbox = 80
            
            
            KeysPressed = pygame.key.get_pressed()
            
            
            
            p1_bool = p1_etat == libre or p1_etat == avanc or p1_etat == recul or p1_etat == accroupi
        
            
            if p1_hold :
                if not (KeysPressed[pygame.K_j] or KeysPressed[pygame.K_k]):
                    p1_hold = False
            
            
            if p2_hold :
                if not (KeysPressed[pygame.K_KP2] or KeysPressed[pygame.K_KP3]):
                    p2_hold = False
            
        
            if (p1_x == p2_x) and p1_x < 750:
                p2_x += 2
            elif (p1_x == p2_x) and p1_x > 750:
                p2_x -= 2
            
            if (p1_x < p2_x)  and (((p1_x - p2_x)**2 + (p1_y - p2_y)**2))**(0.5) <= p2_hitbox and p1_x > 1:
                p1_x -= 3
                p2_x +=3
            elif  (p1_x > p2_x)  and (((p1_x - p2_x)**2 + (p1_y - p2_y)**2))**(0.5) <= p2_hitbox and p1_x + 100 < 1500:    
                p1_x += 3
                p2_x -=3
    
            if p2_x < 1:
                p2_x = 2
            elif p2_x + 100 > 1499:
                p2_x = 1398
            
            
            if (p1_x < 1):
                p1_x = 2
            elif p1_x + 100 > 1500:
                p1_x = 1398
            
            
            
            
            if p1_bool:
                
                if (p1_x-1-p2_x)**2 > (p1_x-p2_x)**2:
                    p1_direction = 1
                else:
                    p1_direction = -1
                
                
                if KeysPressed[pygame.K_j] and not p1_hold :
                    if KeysPressed[pygame.K_s] :
                        if ((p1_x-1-p2_x)**2 > (p1_x-p2_x)**2 and KeysPressed[pygame.K_d]): 
                            # p1 fait lfj
                            p1_etat = prepa
                            p1_coup = "lfj"
                            p1_startup = 0
                            p1_direction = 1
                        elif ((p1_x+1-p2_x)**2 > (p1_x-p2_x)**2 and KeysPressed[pygame.K_a]):
                            # p1 fait lfj
                            p1_etat = prepa
                            p1_coup = "lfj"
                            p1_startup = 0
                            p1_direction = -1
                        else:
                            # p1 fait lj
                            p1_etat = prepa
                            p1_coup = "lj"
                            p1_startup = 0
                            if (p1_x-1-p2_x)**2 > (p1_x-p2_x)**2:
                                p1_direction = 1
                            else:
                                p1_direction = -1
                    elif KeysPressed[pygame.K_a] :
                        if (p1_x-1-p2_x)**2 > (p1_x-p2_x)**2:   # p1 fait nj
                            p1_coup = "nj"
                            p1_etat = prepa
                            p1_startup = 0
                            p1_direction = 1
                        else:   # p1 fait fk
                            b=0
                            p1_startup = 0
                            p1_etat = prepa
                            p1_coup = "fj"
                            p1_direction = -1
                    elif KeysPressed[pygame.K_d] :
                        if (p1_x+1-p2_x)**2 > (p1_x-p2_x)**2:   # p1 fait nj
                            p1_coup = "nj"
                            p1_etat = prepa
                            p1_startup = 0
                            p1_direction = -1
                        else:   # p1 fait fk
                            b=0
                            p1_startup = 0
                            p1_etat = prepa
                            p1_coup = "fj"
                            p1_direction = 1
                    else:
                        # p1 fait nj
                        p1_etat = prepa
                        p1_coup = "nj"
                        p1_startup = 0
                        if (p1_x-1-p2_x)**2 > (p1_x-p2_x)**2:
                            p1_direction = 1
                        else:
                            p1_direction = -1
                elif KeysPressed[pygame.K_k] and not p1_hold :
                    if KeysPressed[pygame.K_s]:
                        # p1 fait lk
                        p1_etat = prepa
                        p1_coup = "lk"
                        p1_startup = 0
                        if (p1_x-1-p2_x)**2 > (p1_x-p2_x)**2:
                            p1_direction = 3
                        else:
                            p1_direction = -3
                    elif KeysPressed[pygame.K_d]:
                        if (p1_x+1-p2_x)**2 > (p1_x-p2_x)**2:   # p1 fait nk
                            p1_coup = "nk"
                            p1_etat = prepa
                            p1_startup = 0
                            p1_direction = -3
                        else:   # p1 fait fk
                            b=0
                            p1_startup = 0
                            p1_etat = prepa
                            p1_coup = "fk"
                            p1_direction = 3
                    elif KeysPressed[pygame.K_a]:
                        if (p1_x-1-p2_x)**2 > (p1_x-p2_x)**2:   # p1 fait nk
                            p1_coup = "nk"
                            p1_etat = prepa
                            p1_startup = 0
                            p1_direction = 3
                        else:   # p1 fait fk
                            b=0
                            p1_startup = 0
                            p1_etat = prepa
                            p1_coup = "fk"
                            p1_direction = -3
                    else:# p1 fait nk
                        p1_coup = "nk"
                        p1_etat = prepa
                        p1_startup = 0
                        if (p1_x-1-p2_x)**2 > (p1_x-p2_x)**2:
                            p1_direction = 3
                        else:
                            p1_direction = -3
                elif KeysPressed[pygame.K_w]:
                    p1_coup = "saut"
                    p1_etat = prepa
                    p1_startup = 0
                elif KeysPressed[pygame.K_s]:
                    p1_etat = accroupi
                elif KeysPressed[pygame.K_a] :
                    if (p1_x-1-p2_x)**2 > (p1_x-p2_x)**2:
                        p1_etat = recul
                    else :
                        p1_etat = avanc
                    if p1_x - jdx >  0  and (((p1_x - p2_x)**2 + (p1_y - p2_y)**2))**(0.5) > p2_hitbox:
                        p1_x-=3
                    
                    if p1_x <  0:
                        p1_x = 2
                        
                elif KeysPressed[pygame.K_d] :
                    if (p1_x+1-p2_x)**2 > (p1_x-p2_x)**2:
                        p1_etat = recul
                    else :
                        p1_etat = avanc
                    if p1_x - jdx< WINDOW_SIZE[0] - 109  and (((p1_x - p2_x)**2 + (p1_y - p2_y)**2))**(0.5) > p2_hitbox:
                        p1_x+=3
                        
                else :
                    p1_etat = libre
                #Décalage écran
            if (p1_x - jdx <  10)  and (jdx > 0 ):
                p1_x =  jdx + 9
                jdx -= 3
        
        
        
        
            if (p1_x - jdx + 100 >  WINDOW_SIZE[0] - 10) and (jdx < fw - WINDOW_SIZE[0]):
                p1_x =  jdx + WINDOW_SIZE[0] - 109
                jdx += 3
                    
        
            
            p2_bool = p2_etat == libre or p2_etat == avanc or p2_etat == recul or p2_etat == accroupi
            if p2_bool:
                
                
                if (p1_x-1-p2_x)**2 > (p1_x-p2_x)**2:
                    p2_direction = -1
                else:
                    p2_direction = 1
                
                
                if KeysPressed[pygame.K_KP2] and not p2_hold :
                    if KeysPressed[pygame.K_DOWN] :
                        if ((p2_x-1-p1_x)**2 > (p2_x-p1_x)**2 and KeysPressed[pygame.K_RIGHT]): 
                            # p2 fait lfj
                            p2_etat = prepa
                            p2_coup = "lfj"
                            p2_startup = 0
                            p2_direction = 1
                        elif ((p2_x+1-p1_x)**2 > (p2_x-p1_x)**2 and KeysPressed[pygame.K_LEFT]):
                            # p2 fait lfj
                            p2_etat = prepa
                            p2_coup = "lfj"
                            p2_startup = 0
                            p2_direction = -1
                        else:
                            # p2 fait lj
                            p2_etat = prepa
                            p2_coup = "lj"
                            p2_startup = 0
                            if (p2_x-1-p1_x)**2 > (p2_x-p1_x)**2:
                                p2_direction = 1
                            else:
                                p2_direction = -1
                    elif KeysPressed[pygame.K_LEFT] :
                        if (p2_x-1-p1_x)**2 > (p2_x-p1_x)**2: # p2 fait nj
                            p2_coup = "nj"
                            p2_etat = prepa
                            p2_startup = 0
                            p2_direction = 1
                        else: # p2 fait fk
                            bb=0
                            p2_startup = 0
                            p2_etat = prepa
                            p2_coup = "fj"
                            p2_direction = -1
                    elif KeysPressed[pygame.K_RIGHT] :
                        if (p2_x+1-p1_x)**2 > (p2_x-p1_x)**2: # p2 fait nj
                            p2_coup = "nj"
                            p2_etat = prepa
                            p2_startup = 0
                            p2_direction = -1
                        else: # p2 fait fj
                            bb=0
                            p2_startup = 0
                            p2_etat = prepa
                            p2_coup = "fj"
                            p2_direction = 1
                    else:
                        # p2 fait nj
                        p2_etat = prepa
                        p2_coup = "nj"
                        p2_startup = 0
                        if (p2_x-1-p1_x)**2 > (p2_x-p1_x)**2:
                            p2_direction = 1
                        else:
                            p2_direction = -1
                elif KeysPressed[pygame.K_KP3] and not p2_hold :
                    if KeysPressed[pygame.K_DOWN]:
                        # p2 fait lk
                        p2_etat = prepa
                        p2_coup = "lk"
                        p2_startup = 0
                        if (p2_x-1-p1_x)**2 > (p2_x-p1_x)**2:
                            p2_direction = 3
                        else:
                            p2_direction = -3
                    elif KeysPressed[pygame.K_RIGHT]:
                        if (p2_x+1-p1_x)**2 > (p2_x-p1_x)**2: # p2 fait nk
                            p2_coup = "nk"
                            p2_etat = prepa
                            p2_startup = 0
                            p2_direction = -3
                        else: # p2 fait fk
                            bb=0
                            p2_startup = 0
                            p2_etat = prepa
                            p2_coup = "fk"
                            p2_direction = 3
        
                    elif KeysPressed[pygame.K_LEFT]:
                        if (p2_x-1-p1_x)**2 > (p2_x-p1_x)**2: # p2 fait nk
                            p2_coup = "nk"
                            p2_etat = prepa
                            p2_startup = 0
                            p2_direction = 3
                        else: # p2 fait fk
                            bb=0
                            p2_startup = 0
                            p2_etat = prepa
                            p2_coup = "fk"
                            p2_direction = -3
                    else:
                        # p2 fait nk
                        p2_etat = prepa
                        p2_coup = "nk"
                        p2_startup = 0
                        if (p2_x-1-p1_x)**2 > (p2_x-p1_x)**2:
                            p2_direction = 3
                        else:
                            p2_direction = -3
                            
                elif KeysPressed[pygame.K_UP]:
                    p2_coup = "saut"
                    p2_etat = prepa
                    p2_startup = 0
                elif KeysPressed[pygame.K_DOWN] :
                    p2_etat = accroupi
                elif KeysPressed[pygame.K_LEFT] :
                    if (p2_x-1-p1_x)**2 > (p2_x-p1_x)**2:
                        p2_etat = recul
                    else :
                        p2_etat = avanc
                    if p2_x - jdx >  0  and (((p1_x - p2_x)**2 + (p1_y - p2_y)**2))**(0.5) > p1_hitbox:
                        p2_x-=3
                        
                elif KeysPressed[pygame.K_RIGHT] :
                    if (p2_x+1-p1_x)**2 > (p2_x-p1_x)**2:
                        p2_etat = recul
                    else :
                        p2_etat = avanc
                    
                    if p2_x - jdx< WINDOW_SIZE[0] -109  and (((p1_x - p2_x)**2 + (p1_y - p2_y)**2))**(0.5) > p1_hitbox:
                        p2_x+=3
                    
                else:
                    p2_etat = libre
                #Décalage écran
            if (p2_x - jdx <  10)  and (jdx > 0 ):
                p2_x =  jdx + 9
                jdx -= 3
            
                
            if (p2_x - jdx + 100 >  WINDOW_SIZE[0] - 10) and (jdx < fw - WINDOW_SIZE[0]):
                p2_x =  jdx + WINDOW_SIZE[0] - 109
                jdx +=3
                
            if p1_etat == accroupi:
                p1_sprite = liste_sprites[7][0]
            
            elif p1_etat == libre or p1_etat == recul or p1_etat == avanc:
                p1_sprite = liste_sprites[0][time%len(liste_sprites[0])]
        
            if p2_etat == accroupi:
                p2_sprite = liste_sprites[7][1]
                
            elif p2_etat == libre or p2_etat == recul or p2_etat == avanc:
                p2_sprite = liste_sprites[1][(time+10)%len(liste_sprites[1])]
            
            
            if p1_etat == prepa:
                if p2_etat == recul:
                    p2_etat = gardeh
                elif p2_etat == accroupi and ((KeysPressed[pygame.K_LEFT] and (p2_x-1-p1_x)**2 > (p2_x-p1_x)**2) or (KeysPressed[pygame.K_RIGHT] and (p2_x+1-p1_x)**2 > (p2_x-p1_x)**2)):
                    p2_etat = gardel
                
                if p1_coup == "saut":
                    if p1_startup>=5:
                        if KeysPressed[pygame.K_d]:
                            p1_saut = 4
                            if (p1_x+1-p2_x)**2 > (p1_x-p2_x)**2:
                                p1_sprite = liste_sprites[10][5]
                            else:
                                p1_sprite = liste_sprites[10][4]
                        elif KeysPressed[pygame.K_a]:
                            p1_saut = -4
                            if (p1_x-1-p2_x)**2 > (p1_x-p2_x)**2:
                                p1_sprite = liste_sprites[10][5]
                            else:
                                p1_sprite = liste_sprites[10][4]
                        else:
                            p1_sprite = liste_sprites[10][6]
                            p1_saut= 0
                        p1_etat = sautup
                    else:
                        p1_sprite = liste_sprites[10][p1_startup]
                if p1_coup == "nj":
                    if p1_startup >= nj["startup"] + nj["active"]:
                        p1_etat = recov
                        p1_recov = nj["recovery"]
                        if ((p1_direction>0 and p1_x+100 > p2_x) or (p1_direction<0 and p1_x < p2_x+100)) and not p2_etat == terre and p2_y > 70:
                            if p2_etat == blockstunh or p2_etat == blockstunl or p2_etat == gardeh or p2_etat == gardel:
                                if not ((KeysPressed[pygame.K_LEFT] and (p2_x-1-p1_x)**2 > (p2_x-p1_x)**2) or (KeysPressed[pygame.K_RIGHT] and (p2_x+1-p1_x)**2 > (p2_x-p1_x)**2)):
                                    p2_etat = libre
                                elif KeysPressed[pygame.K_DOWN]:
                                    p2_etat = gardel
                                else:
                                    p2_etat = gardeh
                                    
                            if p2_etat == sautup or p2_etat == sautdown:
                                p2_etat = chute
                                p2_pv -= nj["degat"]
                                
                                p1_son = sonnj1
                                p1_son.play()
                                
                            else:
                                if not (p2_etat == gardeh or p2_etat == gardel):
                                    p1_son = sonnj1
                                    p1_son.play()
                                    
                                    p2_pv -= nj["degat"]
                                    if p2_etat == hitstunl or p2_etat == accroupi:
                                        p2_etat = hitstunl
                                    else:
                                        p2_etat = hitstunh
                                    p2_stun = nj["hitstun"]
                                elif p2_etat == gardeh or p2_etat == gardel:
                                    p1_son = garde1
                                    p1_son.play()
                                    p2_stun = nj["blockstun"]
                                    if p2_etat == gardel:
                                        p2_etat = blockstunl
                                    else:
                                        p2_etat = blockstunh
                    else:
                        p1_sprite = liste_sprites[2][p1_startup]
                elif p1_coup == "fk":
                    if p1_startup >= fk["startup"] + fk["active"]:
                        p1_etat = recov
                        p1_recov = fk["recovery"]
                        b=0
                        p1_sprite = liste_sprites[8][0]
                        if ((p1_direction>0 and p1_x+200 > p2_x) or (p1_direction<0 and p1_x < p2_x+200)) and not p2_etat == terre and p2_y > 90:
                            if p2_etat == blockstunh or p2_etat == blockstunl or p2_etat == gardeh or p2_etat == gardel:
                                if not ((KeysPressed[pygame.K_LEFT] and (p2_x-1-p1_x)**2 > (p2_x-p1_x)**2) or (KeysPressed[pygame.K_RIGHT] and (p2_x+1-p1_x)**2 > (p2_x-p1_x)**2)):
                                    p2_etat = libre
                                elif KeysPressed[pygame.K_DOWN]:
                                    p2_etat = gardel
                                else:
                                    p2_etat = gardeh
                                    
                            if p2_etat == sautup or p2_etat == sautdown:
                                p2_etat = chute
                                p2_pv -= fk["degat"]
                                sonfk_start1.stop()
                                sonfk_end1.play()
                            else:
                                if not (p2_etat == gardeh or p2_etat == gardel):
                                    sonfk_start1.stop()
                                    sonfk_end1.play()
                                    p2_pv -= fk["degat"]
                                    p2_etat = projet
                                    p2_stun = fk["hitstun"]
                                elif p2_etat == gardeh or p2_etat == gardel:
                                    p1_son = garde1
                                    p1_son.play()
                                    if p2_etat == gardel:
                                        p2_etat = blockstunl
                                    else:
                                        p2_etat = blockstunh
                                    p2_stun = fk["blockstun"]
                    elif p1_startup < fk["startup"] + fk["active"]:
                        if (p1_startup == 0) :
                            
                            p1_son = sonfk_start1
                            p1_son.play()
                        if not(( p2_x < 1 ) or ( p2_x + 100 > 1499 )) :
                            p1_x +=p1_direction
                        
                        elif (p1_x + 55 < p2_x and p1_direction > 0) or ( p1_x > p2_x + 55 and p1_direction < 0 ) :
                            p1_x +=p1_direction
        
                        
                        if p1_startup % 2 == 0 and p1_startup != 0 and p1_startup < 25:
                            b += 1
                        elif p1_startup != 0 and p1_startup > 25:
                            b += 1
                        
                        p1_sprite = liste_sprites[3][b]
                        if p2_etat != sautup and p2_etat != sautdown:
                            if p1_direction >0:
                                if p1_x+55 > p2_x :
                                    p2_x+=p1_direction*3
                            if p1_direction <0:
                                if p1_x < p2_x+55 :
                                    p2_x+=p1_direction*3
                elif p1_coup == "lj":
                    if p1_startup >= lj["startup"] + lj["active"]:
                        p1_etat = recov
                        p1_recov = lj["recovery"]
                        if ((p1_direction>0 and p1_x+150 > p2_x) or (p1_direction<0 and p1_x < p2_x+150)) and not p2_etat == terre and not p2_etat == sautup and not p2_etat == sautdown:
                            if p2_etat == blockstunh or p2_etat == blockstunl:
                                if not ((KeysPressed[pygame.K_LEFT] and (p2_x-1-p1_x)**2 > (p2_x-p1_x)**2) or (KeysPressed[pygame.K_RIGHT] and (p2_x+1-p1_x)**2 > (p2_x-p1_x)**2)) or p2_etat == gardeh or p2_etat == gardel:
                                    p2_etat = libre
                                elif KeysPressed[pygame.K_DOWN]:
                                    p2_etat = gardel
                                else:
                                    p2_etat = gardeh
                            if not ( p2_etat == gardel):
                                p1_son = sonlj1
                                p1_son.play()
                                p2_pv -= lj["degat"]
                                if p2_etat == hitstunl or p2_etat == accroupi:
                                    p2_etat = hitstunl
                                else:
                                    p2_etat = hitstunh
                                p2_stun = lj["hitstun"]
                            elif p2_etat == gardel:
                                p1_son = garde1
                                p1_son.play()
                                p2_stun = lj["blockstun"]
                                p2_etat = blockstunl
                    else:
                        p1_sprite = liste_sprites[13][p1_startup]
        
        
                elif p1_coup == "nk":
                    if p1_startup >= nk["startup"] + nk["active"]:
                        p1_etat = recov
                        p1_recov = nk["recovery"]
                        if ((p1_direction>0 and p1_x+200 > p2_x) or (p1_direction<0 and p1_x < p2_x+200)) and not p2_etat == terre and not p2_etat == sautup and not p2_etat == sautdown:
                            if p2_etat == blockstunh or p2_etat == blockstunl or p2_etat == gardeh or p2_etat == gardel:
                                if not ((KeysPressed[pygame.K_LEFT] and (p2_x-1-p1_x)**2 > (p2_x-p1_x)**2) or (KeysPressed[pygame.K_RIGHT] and (p2_x+1-p1_x)**2 > (p2_x-p1_x)**2)):
                                    p2_etat = libre
                                elif KeysPressed[pygame.K_DOWN]:
                                    p2_etat = gardel
                                else:
                                    p2_etat = gardeh
                            if not ( p2_etat == gardel):
                                p1_son = sonnk1
                                p1_son.play()
                                p2_pv -= nk["degat"]
                                p2_etat = projet
                                p2_stun = nk["hitstun"]
                            elif p2_etat == gardel:
                                p1_son = garde1
                                p1_son.play()
                                p2_stun = nk["blockstun"]
                                p2_etat = blockstunl
        
                    else:
                        p1_sprite = liste_sprites[15][p1_startup]
        
                elif p1_coup == "lk":
                    if p1_startup >= lk["startup"] + lk["active"]:
                        if ((p1_direction>0 and p1_x+100 > p2_x) or (p1_direction<0 and p1_x < p2_x+100)) and not p2_etat == terre and not p2_etat == hitstunh and not p2_etat == hitstunl and not p2_etat == sautup and not p2_etat == sautdown:
                            if p2_etat == prepa and p2_coup == "lk":
                                dechop = True
                            else:
                                dechop = False
                            candechop = True
                            if p2_etat == prepa or p2_etat == recov:
                                candechop = False
                            p1_son = sonlk1
                            p1_son.play()
                            p1_etat = grabber
                            p2_etat = grabbed
                            p2_stun = 0
                            p1_sprite = liste_sprites[8][2]
                            p2_sprite = liste_sprites[8][6]
                        else:
                            p1_etat = recov
                            p1_recov = lk['recovery']
                    else:
                        p1_sprite = liste_sprites[7][4+p1_startup]
                        
                elif p1_coup == "fj":
                    if p1_startup >= fj["startup"] + fj["active"]:
                        p1_etat = recov
                        p1_recov = fj["recovery"]
                        if (p1_direction>0 and p1_x+170 > p2_x and p1_x < p2_x) or (p1_direction<0 and p1_x < p2_x+170 and p1_x > p2_x) and not p2_etat == terre and p2_y > 60:
                            if p2_etat == blockstunh or p2_etat == blockstunl or p2_etat == gardeh or p2_etat == gardel:
                                if not ((KeysPressed[pygame.K_LEFT] and (p2_x-1-p1_x)**2 > (p2_x-p1_x)**2) or (KeysPressed[pygame.K_RIGHT] and (p2_x+1-p1_x)**2 > (p2_x-p1_x)**2)):
                                    p2_etat = libre
                                elif KeysPressed[pygame.K_DOWN]:
                                    p2_etat = gardel
                                else:
                                    p2_etat = gardeh
                            if p2_etat == sautup or p2_etat == sautdown:
                                p2_etat = chute
                                p2_pv -= fj["degat"]
                                p1_son = sonfj1
                                p1_son.play()
                            else:
                                if not ( p2_etat == gardeh):
                                    p1_son = sonfj1
                                    p1_son.play()
                                    p2_pv -= fj["degat"]
                                    if p2_etat == hitstunl or p2_etat == accroupi:
                                        p2_etat = hitstunl
                                    else:
                                        p2_etat = hitstunh
                                    p2_stun = fj["hitstun"]
                                elif p2_etat == gardeh:
                                    p1_son = garde1
                                    p1_son.play()
                                    p2_stun = fj["blockstun"]
                                    p2_etat = blockstunh
                    else:
                        p1_sprite = liste_sprites[17][p1_startup]
                        
                        
                if p1_coup == "lfj":
                    if p1_startup >= lfj["startup"] + lfj["active"]:
                        p1_etat = recov
                        p1_recov = lfj["recovery"]
                        if ((p1_direction>0 and p1_x+100 > p2_x) or (p1_direction<0 and p1_x < p2_x+100)) and not p2_etat == terre:
                            if p2_etat == blockstunh or p2_etat == blockstunl or p2_etat == gardeh or p2_etat == gardel:
                                if not ((KeysPressed[pygame.K_LEFT] and (p2_x-1-p1_x)**2 > (p2_x-p1_x)**2) or (KeysPressed[pygame.K_RIGHT] and (p2_x+1-p1_x)**2 > (p2_x-p1_x)**2)):
                                    p2_etat = libre
                                elif KeysPressed[pygame.K_DOWN]:
                                    p2_etat = gardel
                                else:
                                    p2_etat = gardeh
                            if p2_etat == sautup or p2_etat == sautdown:
                                p2_etat = chute
                                p2_pv -= lfj["degat"]
                                p1_son = sonlfj1
                                p1_son.play()
                            else:
                                if not (p2_etat == gardeh or p2_etat == gardel):
                                    p1_son = sonlfj1
                                    p1_son.play()
                                    p2_pv -= lfj["degat"]
                                    if p2_etat == hitstunl or p2_etat == accroupi:
                                        p2_etat = hitstunl
                                    else:
                                        p2_etat = hitstunh
                                    p2_stun = lfj["hitstun"]
                                elif p2_etat == gardeh or p2_etat == gardel:
                                    p1_son = garde1
                                    p1_son.play()
                                    p2_stun = lfj["blockstun"]
                                    if p2_etat == gardel:
                                        p2_etat = blockstunl
                                    else:
                                        p2_etat = blockstunh
                    else:
                        p1_sprite = liste_sprites[20][p1_startup]
                p1_startup +=1
                
            
            
            
    
            
            
            
            if p2_etat == prepa:
                if p1_etat == recul:
                    p1_etat = gardeh
                elif p1_etat == accroupi and ((KeysPressed[pygame.K_d] and (p1_x-1-p2_x)**2 < (p1_x-p2_x)**2) or (KeysPressed[pygame.K_a] and (p1_x+1-p2_x)**2 < (p1_x-p2_x)**2)):
                    p1_etat = gardel
                    
                    
                if p2_coup == "saut":
                    if p2_startup>=5:
                        if KeysPressed[pygame.K_RIGHT]:
                            p2_saut = 4
                            if (p2_x+1-p1_x)**2 > (p2_x-p1_x)**2:
                                p2_sprite = liste_sprites[11][5]
                            else:
                                p2_sprite = liste_sprites[11][4]
                        elif KeysPressed[pygame.K_LEFT]:
                            p2_saut = -4
                            if (p2_x-1-p1_x)**2 > (p2_x-p1_x)**2:
                                p2_sprite = liste_sprites[11][5]
                            else:
                                p2_sprite = liste_sprites[11][4]
                        else:
                            p2_sprite = liste_sprites[11][6]
                            p2_saut= 0
                        p2_etat = sautup
                    else:
                        p2_sprite = liste_sprites[11][p2_startup]
                    
                    
                    
                elif p2_coup == "nj":
                    if p2_startup >= nj["startup"] + nj["active"]:
                        p2_etat = recov
                        p2_recov = nj["recovery"]
                        if ((p2_direction>0 and p2_x+100 > p1_x) or (p2_direction<0 and p2_x < p1_x+100)) and not p1_etat == terre and p1_y > 70:
                            if p1_etat == blockstunh or p1_etat == blockstunl:
                                if not ((KeysPressed[pygame.K_d] and (p1_x-1-p2_x)**2 < (p1_x-p2_x)**2) or (KeysPressed[pygame.K_a] and (p1_x+1-p2_x)**2 < (p1_x-p2_x)**2)):
                                    p1_etat = libre
                                elif KeysPressed[pygame.K_s]:
                                    p1_etat = gardel
                                else:
                                    p1_etat = gardeh
                            
                            if p1_etat == sautup or p1_etat == sautdown:
                                p1_etat = chute
                                p1_pv -= nj["degat"]
                                p2_son = sonnj2
                                p2_son.play()
                            else:
                                if not (p1_etat == gardeh or p1_etat == gardel):
                                    p2_son = sonnj2
                                    p2_son.play()
                                    p1_pv -= nj["degat"]
                                    if p1_etat == hitstunl or p1_etat == accroupi:
                                        p1_etat = hitstunl
                                    else:
                                        p1_etat = hitstunh
                                    p1_stun = nj["hitstun"]
            
                                elif p1_etat == gardeh or p1_etat == gardel:
                                    p2_son = garde2
                                    p2_son.play()
                                    if p1_etat == gardel:
                                        p1_etat = blockstunl
                                    else:
                                        p1_etat = blockstunh
                                    p1_stun = nj["blockstun"]
                    else:
                        p2_sprite = liste_sprites[4][p2_startup]
                            
                elif p2_coup == "fk":
                    
                    if p2_startup >= fk["startup"] + fk["active"]:
                        p2_etat = recov
                        p2_recov = fk["recovery"]
                        bb=0
                        p2_sprite = liste_sprites[8][1]
                        if ((p2_direction>0 and p2_x+200 > p1_x) or (p2_direction<0 and p2_x < p1_x+200)) and not p1_etat == terre and p1_y > 90:
                            if p1_etat == blockstunh or p1_etat == blockstunl:
                                if not ((KeysPressed[pygame.K_d] and (p1_x-1-p2_x)**2 < (p1_x-p2_x)**2) or (KeysPressed[pygame.K_a] and (p1_x+1-p2_x)**2 < (p1_x-p2_x)**2)):
                                    p1_etat = libre
                                elif KeysPressed[pygame.K_s]:
                                    p1_etat = gardel
                                else:
                                    p1_etat = gardeh
                            if p1_etat == sautup or p1_etat == sautdown:
                                sonfk_start2.stop()
                                sonfk_end2.play()
                                p1_etat = chute
                                p1_pv -= fk["degat"]
                            else:
                                if not (p1_etat == gardeh or p1_etat == gardel):
                                    sonfk_start2.stop()
                                    sonfk_end2.play()
                                    p1_pv -= fk["degat"]
                                    p1_etat = projet
                                    p1_stun = fk["hitstun"]
                                elif p1_etat == gardeh or p1_etat == gardel:
                                    p2_son = garde2
                                    p2_son.play()
                                    if p1_etat == gardel:
                                        p1_etat = blockstunl
                                    else:
                                        p1_etat = blockstunh
                                    p1_stun = fk["blockstun"]
                    elif p2_startup < fk["startup"] + fk["active"]:
                        if (p2_startup == 0) :
                        
                            
                            p2_son = sonfk_start2
                            p2_son.play()
                        if p2_startup % 2 == 0 and p2_startup != 0 and p2_startup < 25:
                            bb += 1
                        elif p2_startup != 0 and p2_startup > 25:
                            bb += 1
                        
                        p2_sprite = liste_sprites[5][bb]
                        if not(( p1_x < 1 ) or ( p1_x + 100 > 1499 )) :
                            p2_x +=p2_direction
                        
                        elif (p2_x + 55 < p1_x and p2_direction > 0) or ( p2_x > p1_x + 55 and p2_direction < 0 ) :
                            p2_x +=p2_direction
                        if p1_etat != sautup and p1_etat != sautdown:
                            if p2_direction >0:
                                if p2_x+55 > p1_x :
                                    p1_x+=p2_direction*3
                            if p2_direction <0:
                                if p2_x < p1_x+55 :
                                    p1_x+=p2_direction*3
                elif p2_coup == "lj":
                    if p2_startup >= lj["startup"] + lj["active"]:
                        p2_etat = recov
                        p2_recov = lj["recovery"]
                        if ((p2_direction>0 and p2_x+150 > p1_x) or (p2_direction<0 and p2_x < p1_x+150)) and not p1_etat == terre and not p1_etat == sautup and not p1_etat == sautdown:
                            if p1_etat == blockstunh or p1_etat == blockstunl:
                                if not ((KeysPressed[pygame.K_d] and (p1_x-1-p2_x)**2 < (p1_x-p2_x)**2) or (KeysPressed[pygame.K_a] and (p1_x+1-p2_x)**2 < (p1_x-p2_x)**2)):
                                    p1_etat = libre
                                elif KeysPressed[pygame.K_s]:
                                    p1_etat = gardel
                                else:
                                    p1_etat = gardeh
                            if not ( p1_etat == gardel):
                                p2_son = sonlj2
                                p2_son.play()
                                p1_pv -= lj["degat"]
                                if p1_etat == hitstunl or p1_etat == accroupi:
                                    p1_etat = hitstunl
                                else:
                                    p1_etat = hitstunh
                                p1_stun = lj["hitstun"]
                            elif p1_etat == gardel:
                                p2_son = garde2
                                p2_son.play()
                                p1_stun = lj["blockstun"]
                                p1_etat = blockstunl
        
                    else:
                        p2_sprite = liste_sprites[14][p2_startup]
        
                elif p2_coup == "lk":
                    if p2_startup >= lk["startup"] + lk["active"]:
                        if ((p2_direction>0 and p2_x+100 > p1_x) or (p2_direction<0 and p2_x < p1_x+100)) and not p1_etat == terre and not p1_etat == hitstunh and not p1_etat == hitstunl and not p1_etat == sautup and not p1_etat == sautdown:
                            if p1_etat == prepa and p1_coup == "lk":
                                dechop = True
                            else:
                                dechop = False
                            candechop = True
                            if p1_etat == prepa or p1_etat == recov:
                                candechop = False
                            p2_son = sonlk2
                            p2_son.play()
                            p2_etat = grabber
                            p1_etat = grabbed
                            p1_stun = 0
                            p2_sprite = liste_sprites[8][7]
                            p1_sprite = liste_sprites[8][11]
                        else:
                            p2_etat = recov
                            p2_recov = lk['recovery']
                    else:
                        p2_sprite = liste_sprites[7][9+p2_startup]
                        
                elif p2_coup == "nk":
                    if p2_startup >= nk["startup"] + nk["active"]:
                        p2_etat = recov
                        p2_recov = nk["recovery"]
                        if ((p2_direction>0 and p2_x+200 > p1_x) or (p2_direction<0 and p2_x < p1_x+200)) and not p1_etat == terre and not p1_etat == sautup and not p1_etat == sautdown:
                            if p1_etat == blockstunh or p1_etat == blockstunl or p1_etat == gardeh or p1_etat == gardel:
                                if not ((KeysPressed[pygame.K_d] and (p1_x-1-p2_x)**2 < (p1_x-p2_x)**2) or (KeysPressed[pygame.K_a] and (p1_x+1-p2_x)**2 < (p1_x-p2_x)**2)):
                                    p1_etat = libre
                                elif KeysPressed[pygame.K_s]:
                                    p1_etat = gardel
                                else:
                                    p1_etat = gardeh
                            if not ( p1_etat == gardel):
                                p2_son = sonnk2
                                p2_son.play()
                                p1_pv -= nk["degat"]
                                p1_etat = projet
                                p1_stun = nk["hitstun"]
                            elif p1_etat == gardel:
                                p2_son = garde2
                                p2_son.play()
                                p1_stun = nk["blockstun"]
                                p1_etat = blockstunl
        
                    else:
                        p2_sprite = liste_sprites[16][p2_startup]
                elif p2_coup == "fj":
                    if p2_startup >= fj["startup"] + fj["active"]:
                        p2_etat = recov
                        p2_recov = fj["recovery"]
                        if ((p2_direction>0 and p2_x+170 > p1_x and p2_x<p1_x) or (p2_direction<0 and p2_x < p1_x+170 and p2_x>p1_x)) and not p1_etat == terre and p1_y > 60 :
                            if p1_etat == blockstunh or p1_etat == blockstunl:
                                if not ((KeysPressed[pygame.K_d] and (p1_x-1-p2_x)**2 < (p1_x-p2_x)**2) or (KeysPressed[pygame.K_a] and (p1_x+1-p2_x)**2 < (p1_x-p2_x)**2)):
                                    p1_etat = libre
                                elif KeysPressed[pygame.K_s]:
                                    p1_etat = gardel
                                else:
                                    p1_etat = gardeh
                            if p1_etat == sautup or p1_etat == sautdown:
                                p1_etat = chute
                                p1_pv -= fj["degat"]
                                p2_son = sonfj2
                                p2_son.play()
                            elif not ( p1_etat == gardeh):
                                p2_son = sonfj2
                                p2_son.play()
                                p1_pv -= fj["degat"]
                                if p1_etat == hitstunl or p1_etat == accroupi:
                                    p1_etat = hitstunl
                                else:
                                    p1_etat = hitstunh
                                p1_stun = fj["hitstun"]
                            elif p1_etat == gardeh:
                                p2_son = garde2
                                p2_son.play()
                                p1_stun = fj["blockstun"]
                                p1_etat = blockstunh
                    else:
                        p2_sprite = liste_sprites[18][p2_startup]
                elif p2_coup == "lfj":
                    if p2_startup >= lfj["startup"] + lfj["active"]:
                        p2_etat = recov
                        p2_recov = lfj["recovery"]
                        if ((p2_direction>0 and p2_x+100 > p1_x) or (p2_direction<0 and p2_x < p1_x+100)) and not p1_etat == terre :
                            if p1_etat == blockstunh or p1_etat == blockstunl:
                                if not ((KeysPressed[pygame.K_d] and (p1_x-1-p2_x)**2 < (p1_x-p2_x)**2) or (KeysPressed[pygame.K_a] and (p1_x+1-p2_x)**2 < (p1_x-p2_x)**2)):
                                    p1_etat = libre
                                elif KeysPressed[pygame.K_s]:
                                    p1_etat = gardel
                                else:
                                    p1_etat = gardeh
                            if p1_etat == sautup or p1_etat == sautdown:
                                p1_etat = chute
                                p1_pv -= lfj["degat"]
                                p2_son = sonlfj2
                                p2_son.play()
                            elif not ( p1_etat == gardeh):
                                p2_son = sonlfj2
                                p2_son.play()
                                p1_pv -= lfj["degat"]
                                if p1_etat == hitstunl or p1_etat == accroupi:
                                    p1_etat = hitstunl
                                else:
                                    p1_etat = hitstunh
                                p1_stun = lfj["hitstun"]
                            elif p1_etat == gardeh:
                                p2_son = garde2
                                p2_son.play()
                                p1_stun = lfj["blockstun"]
                                p1_etat = blockstunh
                    else:
                        p2_sprite = liste_sprites[21][p2_startup]
        
                p2_startup +=1
            
        
            if p1_etat == grabbed:
                p1_stun += 1
                if not dechop and p1_stun < 30:
                    if p1_stun > 15:
                        p2_sprite = liste_sprites[8][8]
                    elif KeysPressed[pygame.K_s] and KeysPressed[pygame.K_k] and candechop:
                        dechop = True
                elif p1_stun >= 30 :
                    p1_pv -= lk['degat']
                    p2_sprite = liste_sprites[8][9]
                    p2_etat = recov
                    p2_recov = 30
                    p1_etat = projet
                    p1_stun = 50
                else:
                    p2_etat = hitstunh
                    p2_stun = 20
                    p1_direction = -p2_direction
                    p1_sprite = liste_sprites[8][10]
                    p1_recov = 20
                    p1_etat = recov
                    p1_coup = 0
        
        
            if p2_etat == grabbed:
                p2_stun += 1
                if not dechop and p2_stun < 30:
                    if p2_stun > 15:
                        p1_sprite = liste_sprites[8][3]
                    elif KeysPressed[pygame.K_DOWN] and KeysPressed[pygame.K_KP3] and candechop:
                        dechop = True
                elif p2_stun >= 30 :
                    p2_pv -= lk['degat']
                    p1_sprite = liste_sprites[8][4]
                    p1_etat = recov
                    p1_recov = 30
                    p2_etat = projet
                    p2_stun = 50
                else:
                    p1_etat = hitstunh
                    p1_stun = 20
                    p2_direction = -p1_direction
                    p2_sprite = liste_sprites[8][5]
                    p2_recov = 20
                    p2_etat = recov
                    p2_coup = 0
        
        
            if p1_etat == sautup:
                if (p1_x > 0 and p1_x + 100 < 1499) and ((((p1_x - p2_x)**2 + (p1_y - p2_y)**2))**(0.5) > p2_hitbox or (not (p2_etat == sautup or p2_etat == sautdown))):
                    p1_x += p1_saut
                    
                elif (p1_x < 0):
                    p1_x = 1
                elif (p1_x + 100 > 1499):
                    p1_x = 1398
                    
                if p1_y <=-50:
                    p1_etat = sautdown
                elif p1_y <= -30:
                    p1_y-=7
                elif p1_y <=40:
                    p1_y-=8
                elif p1_y <= 100:
                    p1_y-=9
                else: 
                    p1_y-=10
        
            if p1_etat == sautdown :
                if p1_x > 1 and p1_x + 100 < 1499  and ((((p1_x - p2_x)**2 + (p1_y - p2_y)**2))**(0.5) > p2_hitbox or (not (p2_etat == sautup or p2_etat == sautdown))):
                    p1_x += p1_saut
                
                if p1_sj:
                    if p2_etat == recul:
                        p2_etat = gardeh
                    elif p2_etat == accroupi and ((KeysPressed[pygame.K_LEFT] and (p2_x-1-p1_x)**2 > (p2_x-p1_x)**2) or (KeysPressed[pygame.K_RIGHT] and (p2_x+1-p1_x)**2 > (p2_x-p1_x)**2)):
                        p2_etat = gardel
                
                    p1_startup+=1
                    if p1_startup > 6  and p1_startup <13:
                        p1_sprite = liste_sprites[19][1]
                    elif p1_startup ==13:
                        if ((p1_direction>0 and p1_x+100 > p2_x and p1_x < p2_x) or (p1_direction<0 and p1_x < p2_x+100 and p1_x > p2_x)) and (not p2_etat == terre) and p1_y<p2_y:
                            if p2_etat == blockstunh or p2_etat == blockstunl:
                                if not ((KeysPressed[pygame.K_LEFT] and (p2_x-1-p1_x)**2 > (p2_x-p1_x)**2) or (KeysPressed[pygame.K_RIGHT] and (p2_x+1-p1_x)**2 > (p2_x-p1_x)**2)) or p2_etat == gardeh or p2_etat == gardel:
                                    p2_etat = libre
                                elif KeysPressed[pygame.K_DOWN]:
                                    p2_etat = gardel
                                else:
                                    p2_etat = gardeh
                            if p2_etat == sautup or p2_etat == sautdown:
                                p2_etat = chute
                                p2_pv -= sj["degat"]
                                p1_son = sonsj1
                                p1_son.play()
                            else:
                                if not ( p2_etat == gardeh):
                                    p1_son = sonsj1
                                    p1_son.play()
                                    p2_pv -= sj["degat"]
                                    if p2_etat == hitstunl or p2_etat == accroupi:
                                        p2_etat = hitstunl
                                    else:
                                        p2_etat = hitstunh
                                    p2_stun = sj["hitstun"]
                                elif p2_etat == gardeh:
                                    p1_son = garde1
                                    p1_son.play()
                                    p2_stun = sj["blockstun"]
                                    p2_etat = blockstunh
                    else:
                        p1_sprite = liste_sprites[19][0]
                        
                elif p1_sk:
                    if p2_etat == recul:
                        p2_etat = gardeh
                    elif p2_etat == accroupi and ((KeysPressed[pygame.K_LEFT] and (p2_x-1-p1_x)**2 > (p2_x-p1_x)**2) or (KeysPressed[pygame.K_RIGHT] and (p2_x+1-p1_x)**2 > (p2_x-p1_x)**2)):
                        p2_etat = gardel
                    p1_startup+=1
                    if p1_startup > 6 and p1_startup < 13:
                        p1_sprite = liste_sprites[19][3]
                    elif p1_startup == 13:
                        if ((p1_direction>0 and p1_x+100 > p2_x and p1_x > p2_x) or (p1_direction<0 and p1_x < p2_x+100 and p1_x < p2_x)) and (not p2_etat == terre) and p1_y<p2_y:
                            if p2_etat == blockstunh or p2_etat == blockstunl:
                                if not ((KeysPressed[pygame.K_LEFT] and (p2_x-1-p1_x)**2 > (p2_x-p1_x)**2) or (KeysPressed[pygame.K_RIGHT] and (p2_x+1-p1_x)**2 > (p2_x-p1_x)**2)) or p2_etat == gardeh or p2_etat == gardel:
                                    p2_etat = libre
                                elif KeysPressed[pygame.K_DOWN]:
                                    p2_etat = gardel
                                else:
                                    p2_etat = gardeh
                            if p2_etat == sautup or p2_etat == sautdown:
                                p2_etat = chute
                                p2_pv -= sk["degat"]
                                p1_son = sonsk1
                                p1_son.play()
                            else:
                                if not ( p2_etat == gardeh):
                                    p1_son = sonsk1
                                    p1_son.play()
                                    p2_pv -= sk["degat"]
                                    if p2_etat == hitstunl or p2_etat == accroupi:
                                        p2_etat = hitstunl
                                    else:
                                        p2_etat = hitstunh
                                    p2_stun = sk["hitstun"]
                                elif p2_etat == gardeh:
                                    p1_son = garde1
                                    p1_son.play()
                                    p2_stun = sk["blockstun"]
                                    p2_etat = blockstunh
                    else:
                        p1_sprite = liste_sprites[19][2]
                
                elif KeysPressed[pygame.K_j]:
                    p1_sj = True
                    p1_startup = 0
                elif KeysPressed[pygame.K_k]:
                    p1_sk = True
                    p1_startup = 0
                    
                if p1_y >=starty:
                    if KeysPressed[pygame.K_j] or KeysPressed[pygame.K_k]:
                        p1_hold = True
                    p1_etat = libre
                    p1_sj = False
                    p1_sk = False
                elif p1_y >= 100:
                    p1_y+=10
                elif p1_y >= -45:
                    p1_y+=9
                else :
                    p1_y+=1
        
        
        
        
        
        
            if p2_etat == sautup:
                if (p2_x > 0 and p2_x + 100 < 1499) and ((((p2_x - p1_x)**2 + (p2_y - p1_y)**2))**(0.5) > p1_hitbox or (not (p1_etat == sautup or p1_etat == sautdown))):
                    p2_x += p2_saut
                    
                elif (p2_x < 0):
                    p2_x = 1
                elif (p2_x + 100 > 1499):
                    p2_x = 1398
                
                
                
                
                if p2_y <=-50:
                    p2_etat = sautdown
                elif p2_y <= -30:
                    p2_y-=7
                elif p2_y <=40:
                    p2_y-=8
                elif p2_y <= 100:
                    p2_y-=9
                else:
                    p2_y-=10
        
            if p2_etat == sautdown :
                if p2_x > 1 and p2_x + 100 < 1499 and ((((p2_x - p1_x)**2 + (p2_y - p1_y)**2))**(0.5) > p1_hitbox or (not (p1_etat == sautup or p1_etat == sautdown))):
                    p2_x += p2_saut
                
                if p2_sj:
                    if p1_etat == recul:
                        p1_etat = gardeh
                    elif p1_etat == accroupi and ((KeysPressed[pygame.K_d] and (p1_x-1-p2_x)**2 < (p1_x-p2_x)**2) or (KeysPressed[pygame.K_a] and (p1_x+1-p2_x)**2 < (p1_x-p2_x)**2)):
                        p1_etat = gardel
                
                    p2_startup+=1
                    if p2_startup > 6  and p2_startup <13:
                        p2_sprite = liste_sprites[19][5]
                    elif p2_startup ==13:
                        if ((p2_direction>0 and p2_x+100 > p1_x and p2_x<p1_x) or (p2_direction<0 and p2_x < p1_x+100 and p2_x>p1_x)) and not p1_etat == terre and p2_y<p1_y:
                            if p1_etat == blockstunh or p1_etat == blockstunl:
                                if not ((KeysPressed[pygame.K_a] and (p1_x-1-p2_x)**2 > (p1_x-p2_x)**2) or (KeysPressed[pygame.K_d] and (p1_x+1-p2_x)**2 > (p1_x-p2_x)**2)) or p1_etat == gardeh or p1_etat == gardel:
                                    p1_etat = libre
                                elif KeysPressed[pygame.K_s]:
                                    p1_etat = gardel
                                else:
                                    p1_etat = gardeh
                            if p1_etat == sautup or p1_etat == sautdown:
                                p1_etat = chute
                                p1_pv -= sj["degat"]
                                p2_son = sonsj2
                                p2_son.play()
                            else:
                                if not ( p1_etat == gardeh):
                                    p2_son = sonsj2
                                    p2_son.play()
                                    p1_pv -= sj["degat"]
                                    if p1_etat == hitstunl or p1_etat == accroupi:
                                        p1_etat = hitstunl
                                    else:
                                        p1_etat = hitstunh
                                    p1_stun = sj["hitstun"]
                                elif p1_etat == gardeh:
                                    p2_son = garde2
                                    p2_son.play()
                                    p1_stun = sj["blockstun"]
                                    p1_etat = blockstunh
                    else:
                        p2_sprite = liste_sprites[19][4]
                        
                elif p2_sk:
                    if p1_etat == recul:
                        p1_etat = gardeh
                    elif p1_etat == accroupi and ((KeysPressed[pygame.K_d] and (p1_x-1-p2_x)**2 < (p1_x-p2_x)**2) or (KeysPressed[pygame.K_a] and (p1_x+1-p2_x)**2 < (p1_x-p2_x)**2)):
                        p1_etat = gardel
                    p2_startup+=1
                    if p2_startup > 6 and p2_startup < 13:
                        p2_sprite = liste_sprites[19][7]
                    elif p2_startup == 13:
                        if ((p2_direction>0 and p2_x+100 > p1_x and p2_x>p1_x) or (p2_direction<0 and p2_x < p1_x+100 and p2_x<p1_x)) and not p1_etat == terre and p2_y<p1_y:
                            if p1_etat == blockstunh or p1_etat == blockstunl:
                                if not ((KeysPressed[pygame.K_a] and (p1_x-1-p2_x)**2 > (p1_x-p2_x)**2) or (KeysPressed[pygame.K_d] and (p1_x+1-p2_x)**2 > (p1_x-p2_x)**2)) or p1_etat == gardeh or p1_etat == gardel:
                                    p1_etat = libre
                                elif KeysPressed[pygame.K_s]:
                                    p1_etat = gardel
                                else:
                                    p1_etat = gardeh
                            if p1_etat == sautup or p1_etat == sautdown:
                                p1_etat = chute
                                p1_pv -= sk["degat"]
                                p2_son = sonsk2
                                p2_son.play()
                            else:
                                if not ( p1_etat == gardeh):
                                    p2_son = sonsk2
                                    p2_son.play()
                                    p1_pv -= sk["degat"]
                                    if p1_etat == hitstunl or p1_etat == accroupi:
                                        p1_etat = hitstunl
                                    else:
                                        p1_etat = hitstunh
                                    p1_stun = sk["hitstun"]
                                elif p1_etat == gardeh:
                                    p2_son = garde2
                                    p2_son.play()
                                    p1_stun = sk["blockstun"]
                                    p1_etat = blockstunh
                    else:
                        p2_sprite = liste_sprites[19][6]
                
                elif KeysPressed[pygame.K_KP2]:
                    p2_sj = True
                    p2_startup = 0
                elif KeysPressed[pygame.K_KP3]:
                    p2_sk = True
                    p2_startup = 0
                    
                if p2_y >=starty:
                    if KeysPressed[pygame.K_KP2] or KeysPressed[pygame.K_KP3]:
                        p2_hold = True
                    p2_etat = libre
                    p2_sj = False
                    p2_sk = False
                elif p2_y >= 100:
                    p2_y+=10
                elif p2_y >= -45:
                    p2_y+=9
                else :
                    p2_y+=1
        
        
        
        
        
        
        
        
        
            if p1_etat == recov:
                p1_recov -= 1
                if p1_recov == 0:
                    p1_etat = libre
                    if KeysPressed[pygame.K_j] or KeysPressed[pygame.K_k]:
                        p1_hold = True
                elif ((p1_coup == "lj" and p1_recov >= lj['recovery'] - 3) or (p1_coup == "nj" and p1_recov >= nj['recovery'] - 3)) and (p2_etat == hitstunl or p2_etat == hitstunh or p2_etat == blockstunl or p2_etat == blockstunh):
                    if KeysPressed[pygame.K_k]:
                        if KeysPressed[pygame.K_s]:
                            # p1 fait rien
                            loic=0
                        elif KeysPressed[pygame.K_d]:
                            if (p1_x+1-p2_x)**2 > (p1_x-p2_x)**2:   # p1 fait nk
                                p1_coup = "nk"
                                p1_etat = prepa
                                p1_startup = 0
                                p1_direction = -3
                            else:   # p1 fait fk
                                b=0
                                p1_startup = 0
                                p1_etat = prepa
                                p1_coup = "fk"
                                p1_direction = 3
                        elif KeysPressed[pygame.K_a]:
                            if (p1_x-1-p2_x)**2 > (p1_x-p2_x)**2:   # p1 fait nk
                                p1_coup = "nk"
                                p1_etat = prepa
                                p1_startup = 0
                                p1_direction = 3
                            else:   # p1 fait fk
                                b=0
                                p1_startup = 0
                                p1_etat = prepa
                                p1_coup = "fk"
                                p1_direction = -3
                        else:# p1 fait nk
                            p1_coup = "nk"
                            p1_etat = prepa
                            p1_startup = 0
                            if (p1_x-1-p2_x)**2 > (p1_x-p2_x)**2:
                                p1_direction = 3
                            else:
                                p1_direction = -3
        
            if p2_etat == recov:
                p2_recov -= 1
                if p2_recov == 0:
                    p2_etat = libre
                    if KeysPressed[pygame.K_KP2] or KeysPressed[pygame.K_KP3]:
                        p2_hold = True
                elif ((p2_coup == "lj" and p2_recov >= lj['recovery'] - 3) or (p2_coup == "nj" and p2_recov >= nj['recovery'] - 3)) and (p1_etat == hitstunl or p1_etat == hitstunh or p1_etat == blockstunl or p1_etat == blockstunh):
                    if KeysPressed[pygame.K_KP3] :
                        if KeysPressed[pygame.K_DOWN]:
                            # p2 fait rien
                            loic=0
                        elif KeysPressed[pygame.K_RIGHT]:
                            if (p2_x+1-p1_x)**2 > (p2_x-p1_x)**2: # p2 fait nk
                                p2_coup = "nk"
                                p2_etat = prepa
                                p2_startup = 0
                            else: # p2 fait fk
                                bb=0
                                p2_startup = 0
                                p2_etat = prepa
                                p2_coup = "fk"
                                p2_direction = 3
            
                        elif KeysPressed[pygame.K_LEFT]:
                            if (p2_x-1-p1_x)**2 > (p2_x-p1_x)**2: # p2 fait nk
                                p2_coup = "nk"
                                p2_etat = prepa
                                p2_startup = 0
                            else: # p2 fait fk
                                bb=0
                                p2_startup = 0
                                p2_etat = prepa
                                p2_coup = "fk"
                                p2_direction = -3
                        else:
                            # p2 fait nk
                            p2_etat = prepa
                            p2_coup = "nk"
                            p2_startup = 0
                            if (p2_x-1-p1_x)**2 > (p2_x-p1_x)**2:
                                p2_direction = 3
                            else:
                                p2_direction = -3
        
            if p1_etat == hitstunh or p1_etat == hitstunl or p1_etat == blockstunh or p1_etat == blockstunl or p1_etat == projet:
                if p1_stun <= 0:
                    if p1_etat == projet:
                        p1_etat = terre
                        p1_son = terre1
                        p1_son.play()
                        p1_stun = 50
                        p1_xm = p1_x
                        p1_x += 20*p2_direction
                    else:
                        p1_etat = libre
                    if KeysPressed[pygame.K_j] or KeysPressed[pygame.K_k]:
                        p1_hold = True
                else:
                    p1_stun-=1
                    if p1_etat == hitstunh:
                        p1_sprite = liste_sprites[6][0]
                    elif p1_etat == hitstunl:
                        p1_sprite = liste_sprites[6][2]
                    elif p1_etat == blockstunh:
                        p1_sprite = liste_sprites[12][0]
                    elif p1_etat == blockstunl:
                        p1_sprite = liste_sprites[7][2]
                    elif p1_etat == projet:
                        if p1_stun > 15:
                            p1_sprite = liste_sprites[9][0]
                        else:
                            p1_sprite = liste_sprites[9][1]
                    # C'est le moment où le gars il flanche (25) 
                    p1_x += p2_direction
                    if (( p1_x + 100 > WINDOW_SIZE[0] + jdx - 10 ) and ( jdx + WINDOW_SIZE[0] >= 1499)) and ( p2_direction > 0) :
                        p1_x = jdx + WINDOW_SIZE[0] - 109
                        # decalage du bully dans corner
                        p2_x += p2_direction*-1
                        
                    elif ( (p1_x < jdx + 10 ) and ( jdx <= 1 ) ) and ( p2_direction < 0 ) :
                        p1_x =  jdx + 9
                        # decalage du bully dans corner
                        p2_x += p2_direction*-1
                        
                        
                    elif ( p1_x - jdx + 100 > WINDOW_SIZE[0] - 10 )  or ( p1_x  < jdx + 10):    
                        jdx += p2_direction*2
                        
                    # C'est la fin du flanche 
            
            if p1_etat == chute:
                if p1_y > 138:
                    p1_sj = False
                    p1_sk = False
                    p1_y = 138
                    p1_etat = terre
                    p1_son = terre1
                    p1_son.play()
                    p1_stun = 50
                    p1_xm = p1_x
                    p1_x += 20* p2_direction
                else:
                    p1_sprite = liste_sprites[9][1]
                    p1_y +=7
                    p1_x +=3*p2_direction
            
            if p2_etat == chute:
                if p2_y > 138:
                    p2_sj = False
                    p2_sk = False
                    p2_y = 138
                    p2_etat = terre
                    p2_son = terre2
                    p2_son.play()
                    p2_stun = 50
                    p2_xm = p2_x
                    p2_x += 20* p1_direction
                else:
                    p2_sprite = liste_sprites[9][4]
                    p2_y +=7
                    p2_x +=3*p1_direction
            
            
            
            if p2_etat == hitstunh or p2_etat == hitstunl or p2_etat == blockstunh or p2_etat == blockstunl or p2_etat == projet:
                if p2_stun <= 0:
                    if p2_etat == projet:
                        p2_etat = terre
                        p2_son = terre2
                        p2_son.play()
                        p2_stun = 50
                        p2_xm = p2_x
                        p2_x += 20*p1_direction
                    else:
                        p2_etat = libre
                    if KeysPressed[pygame.K_KP2] or KeysPressed[pygame.K_KP3]:
                        p2_hold = True
                else:
                    p2_stun-=1
                    if p2_etat == hitstunh:
                        p2_sprite = liste_sprites[6][1]
                    elif p2_etat == hitstunl:
                        p2_sprite = liste_sprites[6][3]
                    elif p2_etat == blockstunh:
                        p2_sprite = liste_sprites[12][1]
                    elif p2_etat == blockstunl:
                        p2_sprite = liste_sprites[7][3]
                    elif p2_etat == projet:
                        if p2_stun > 15:
                            p2_sprite = liste_sprites[9][3]
                        else:
                            p2_sprite = liste_sprites[9][4]
                    # C'est le moment où le gars il flanche (25) 
                    p2_x += p1_direction
                    if (( p2_x + 100 > WINDOW_SIZE[0] + jdx - 10 ) and ( jdx + WINDOW_SIZE[0] >= 1499)) and ( p1_direction > 0) :
                        p2_x = jdx + WINDOW_SIZE[0] - 109
                        # decalage du bully dans corner
                        p1_x += p1_direction*-1
                        
                        
                    elif ( (p2_x < jdx + 10 ) and ( jdx <= 1 ) ) and ( p1_direction < 0 ) :
                        p2_x = jdx + 9
                        # decalage du bully dans corner
                        p1_x += p1_direction*-1
                        
                    elif ( p2_x - jdx + 100 > WINDOW_SIZE[0] - 10 )  or ( p2_x  < jdx + 1):    
                        jdx += p1_direction*2
                    # C'est la fin du flanche    
        
        
            if p1_etat == gardeh:
                if not p2_etat == prepa:
                    p1_etat = libre
                else:
                    if KeysPressed[pygame.K_j] and not p1_hold :
                        if KeysPressed[pygame.K_s] :
                            if ((p1_x-1-p2_x)**2 > (p1_x-p2_x)**2 and KeysPressed[pygame.K_d]): 
                                # p1 fait lfj
                                p1_etat = prepa
                                p1_coup = "lfj"
                                p1_startup = 0
                                p1_direction = 1
                            elif ((p1_x+1-p2_x)**2 > (p1_x-p2_x)**2 and KeysPressed[pygame.K_a]):
                                # p1 fait lfj
                                p1_etat = prepa
                                p1_coup = "lfj"
                                p1_startup = 0
                                p1_direction = -1
                            else:
                                # p1 fait lj
                                p1_etat = prepa
                                p1_coup = "lj"
                                p1_startup = 0
                                if (p1_x-1-p2_x)**2 > (p1_x-p2_x)**2:
                                    p1_direction = 1
                                else:
                                    p1_direction = -1
                        elif KeysPressed[pygame.K_a] :
                            if (p1_x-1-p2_x)**2 > (p1_x-p2_x)**2:   # p1 fait nj
                                p1_coup = "nj"
                                p1_etat = prepa
                                p1_startup = 0
                                p1_direction = 1
                            else:   # p1 fait fk
                                b=0
                                p1_startup = 0
                                p1_etat = prepa
                                p1_coup = "fj"
                                p1_direction = -1
                        elif KeysPressed[pygame.K_d] :
                            if (p1_x+1-p2_x)**2 > (p1_x-p2_x)**2:   # p1 fait nj
                                p1_coup = "nj"
                                p1_etat = prepa
                                p1_startup = 0
                                p1_direction = -1
                            else:   # p1 fait fk
                                b=0
                                p1_startup = 0
                                p1_etat = prepa
                                p1_coup = "fj"
                                p1_direction = 1
                        else:
                            # p1 fait nj
                            p1_etat = prepa
                            p1_coup = "nj"
                            p1_startup = 0
                            if (p1_x-1-p2_x)**2 > (p1_x-p2_x)**2:
                                p1_direction = 1
                            else:
                                p1_direction = -1
                    elif KeysPressed[pygame.K_k] and not p1_hold :
                        if KeysPressed[pygame.K_s]:
                            # p1 fait lk
                            p1_etat = prepa
                            p1_coup = "lk"
                            p1_startup = 0
                            if (p1_x-1-p2_x)**2 > (p1_x-p2_x)**2:
                                p1_direction = 3
                            else:
                                p1_direction = -3
                        elif KeysPressed[pygame.K_d]:
                            if (p1_x+1-p2_x)**2 > (p1_x-p2_x)**2:   # p1 fait nk
                                p1_coup = "nk"
                                p1_etat = prepa
                                p1_startup = 0
                                p1_direction = -3
                            else:   # p1 fait fk
                                b=0
                                p1_startup = 0
                                p1_etat = prepa
                                p1_coup = "fk"
                                p1_direction = 3
                        elif KeysPressed[pygame.K_a]:
                            if (p1_x-1-p2_x)**2 > (p1_x-p2_x)**2:   # p1 fait nk
                                p1_coup = "nk"
                                p1_etat = prepa
                                p1_startup = 0
                                p1_direction = 3
                            else:   # p1 fait fk
                                b=0
                                p1_startup = 0
                                p1_etat = prepa
                                p1_coup = "fk"
                                p1_direction = -3
                        else:# p1 fait nk
                            p1_coup = "nk"
                            p1_etat = prepa
                            p1_startup = 0
                            if (p1_x-1-p2_x)**2 > (p1_x-p2_x)**2:
                                p1_direction = 3
                            else:
                                p1_direction = -3
                    elif KeysPressed[pygame.K_w]:
                        p1_coup = "saut"
                        p1_etat = prepa
                        p1_startup = 0
                p1_sprite = liste_sprites[12][0]
            
            if p1_etat == gardel:
                if not p2_etat == prepa:
                    p1_etat = libre
                else:
                    if KeysPressed[pygame.K_j] and not p1_hold :
                        if KeysPressed[pygame.K_s] :
                            if ((p1_x-1-p2_x)**2 > (p1_x-p2_x)**2 and KeysPressed[pygame.K_d]): 
                                # p1 fait lfj
                                p1_etat = prepa
                                p1_coup = "lfj"
                                p1_startup = 0
                                p1_direction = 1
                            elif ((p1_x+1-p2_x)**2 > (p1_x-p2_x)**2 and KeysPressed[pygame.K_a]):
                                # p1 fait lfj
                                p1_etat = prepa
                                p1_coup = "lfj"
                                p1_startup = 0
                                p1_direction = -1
                            else:
                                # p1 fait lj
                                p1_etat = prepa
                                p1_coup = "lj"
                                p1_startup = 0
                                if (p1_x-1-p2_x)**2 > (p1_x-p2_x)**2:
                                    p1_direction = 1
                                else:
                                    p1_direction = -1
                        elif KeysPressed[pygame.K_a] :
                            if (p1_x-1-p2_x)**2 > (p1_x-p2_x)**2:   # p1 fait nj
                                p1_coup = "nj"
                                p1_etat = prepa
                                p1_startup = 0
                                p1_direction = 1
                            else:   # p1 fait fk
                                b=0
                                p1_startup = 0
                                p1_etat = prepa
                                p1_coup = "fj"
                                p1_direction = -1
                        elif KeysPressed[pygame.K_d] :
                            if (p1_x+1-p2_x)**2 > (p1_x-p2_x)**2:   # p1 fait nj
                                p1_coup = "nj"
                                p1_etat = prepa
                                p1_startup = 0
                                p1_direction = -1
                            else:   # p1 fait fk
                                b=0
                                p1_startup = 0
                                p1_etat = prepa
                                p1_coup = "fj"
                                p1_direction = 1
                        else:
                            # p1 fait nj
                            p1_etat = prepa
                            p1_coup = "nj"
                            p1_startup = 0
                            if (p1_x-1-p2_x)**2 > (p1_x-p2_x)**2:
                                p1_direction = 1
                            else:
                                p1_direction = -1
                    elif KeysPressed[pygame.K_k] and not p1_hold :
                        if KeysPressed[pygame.K_s]:
                            # p1 fait lk
                            p1_etat = prepa
                            p1_coup = "lk"
                            p1_startup = 0
                            if (p1_x-1-p2_x)**2 > (p1_x-p2_x)**2:
                                p1_direction = 3
                            else:
                                p1_direction = -3
                        elif KeysPressed[pygame.K_d]:
                            if (p1_x+1-p2_x)**2 > (p1_x-p2_x)**2:   # p1 fait nk
                                p1_coup = "nk"
                                p1_etat = prepa
                                p1_startup = 0
                                p1_direction = -3
                            else:   # p1 fait fk
                                b=0
                                p1_startup = 0
                                p1_etat = prepa
                                p1_coup = "fk"
                                p1_direction = 3
                        elif KeysPressed[pygame.K_a]:
                            if (p1_x-1-p2_x)**2 > (p1_x-p2_x)**2:   # p1 fait nk
                                p1_coup = "nk"
                                p1_etat = prepa
                                p1_startup = 0
                                p1_direction = 3
                            else:   # p1 fait fk
                                b=0
                                p1_startup = 0
                                p1_etat = prepa
                                p1_coup = "fk"
                                p1_direction = -3
                        else:# p1 fait nk
                            p1_coup = "nk"
                            p1_etat = prepa
                            p1_startup = 0
                            if (p1_x-1-p2_x)**2 > (p1_x-p2_x)**2:
                                p1_direction = 3
                            else:
                                p1_direction = -3
                    elif KeysPressed[pygame.K_w]:
                        p1_coup = "saut"
                        p1_etat = prepa
                        p1_startup = 0
                p1_sprite = liste_sprites[7][2]
            
            
            if p2_etat == gardeh:
                if not p1_etat == prepa:
                    p2_etat = libre
                else:
                    if KeysPressed[pygame.K_KP2] and not p2_hold :
                        if KeysPressed[pygame.K_DOWN] :
                            if ((p2_x-1-p1_x)**2 > (p2_x-p1_x)**2 and KeysPressed[pygame.K_RIGHT]): 
                                # p2 fait lfj
                                p2_etat = prepa
                                p2_coup = "lfj"
                                p2_startup = 0
                                p2_direction = 1
                            elif ((p2_x+1-p1_x)**2 > (p2_x-p1_x)**2 and KeysPressed[pygame.K_LEFT]):
                                # p2 fait lfj
                                p2_etat = prepa
                                p2_coup = "lfj"
                                p2_startup = 0
                                p2_direction = -1
                            else:
                                # p2 fait lj
                                p2_etat = prepa
                                p2_coup = "lj"
                                p2_startup = 0
                                if (p2_x-1-p1_x)**2 > (p2_x-p1_x)**2:
                                    p2_direction = 1
                                else:
                                    p2_direction = -1
                        elif KeysPressed[pygame.K_LEFT] :
                            if (p2_x-1-p1_x)**2 > (p2_x-p1_x)**2: # p2 fait nj
                                p2_coup = "nj"
                                p2_etat = prepa
                                p2_startup = 0
                                p2_direction = 1
                            else: # p2 fait fk
                                bb=0
                                p2_startup = 0
                                p2_etat = prepa
                                p2_coup = "fj"
                                p2_direction = -1
                        elif KeysPressed[pygame.K_RIGHT] :
                            if (p2_x+1-p1_x)**2 > (p2_x-p1_x)**2: # p2 fait nj
                                p2_coup = "nj"
                                p2_etat = prepa
                                p2_startup = 0
                                p2_direction = -1
                            else: # p2 fait fj
                                bb=0
                                p2_startup = 0
                                p2_etat = prepa
                                p2_coup = "fj"
                                p2_direction = 1
                        else:
                            # p2 fait nj
                            p2_etat = prepa
                            p2_coup = "nj"
                            p2_startup = 0
                            if (p2_x-1-p1_x)**2 > (p2_x-p1_x)**2:
                                p2_direction = 1
                            else:
                                p2_direction = -1
                    elif KeysPressed[pygame.K_KP3] and not p2_hold :
                        if KeysPressed[pygame.K_DOWN]:
                            # p2 fait lk
                            p2_etat = prepa
                            p2_coup = "lk"
                            p2_startup = 0
                            if (p2_x-1-p1_x)**2 > (p2_x-p1_x)**2:
                                p2_direction = 3
                            else:
                                p2_direction = -3
                        elif KeysPressed[pygame.K_RIGHT]:
                            if (p2_x+1-p1_x)**2 > (p2_x-p1_x)**2: # p2 fait nk
                                p2_coup = "nk"
                                p2_etat = prepa
                                p2_startup = 0
                                p2_direction = -3
                            else: # p2 fait fk
                                bb=0
                                p2_startup = 0
                                p2_etat = prepa
                                p2_coup = "fk"
                                p2_direction = 3
            
                        elif KeysPressed[pygame.K_LEFT]:
                            if (p2_x-1-p1_x)**2 > (p2_x-p1_x)**2: # p2 fait nk
                                p2_coup = "nk"
                                p2_etat = prepa
                                p2_startup = 0
                                p2_direction = 3
                            else: # p2 fait fk
                                bb=0
                                p2_startup = 0
                                p2_etat = prepa
                                p2_coup = "fk"
                                p2_direction = -3
                        else:
                            # p2 fait nk
                            p2_etat = prepa
                            p2_coup = "nk"
                            p2_startup = 0
                            if (p2_x-1-p1_x)**2 > (p2_x-p1_x)**2:
                                p2_direction = 3
                            else:
                                p2_direction = -3
                                
                    elif KeysPressed[pygame.K_UP]:
                        p2_coup = "saut"
                        p2_etat = prepa
                        p2_startup = 0
                p2_sprite = liste_sprites[12][1]
            
            if p2_etat == gardel:
                if not p1_etat == prepa:
                    p2_etat = libre
                else:
                    if KeysPressed[pygame.K_KP2] and not p2_hold :
                        if KeysPressed[pygame.K_DOWN] :
                            if ((p2_x-1-p1_x)**2 > (p2_x-p1_x)**2 and KeysPressed[pygame.K_RIGHT]): 
                                # p2 fait lfj
                                p2_etat = prepa
                                p2_coup = "lfj"
                                p2_startup = 0
                                p2_direction = 1
                            elif ((p2_x+1-p1_x)**2 > (p2_x-p1_x)**2 and KeysPressed[pygame.K_LEFT]):
                                # p2 fait lfj
                                p2_etat = prepa
                                p2_coup = "lfj"
                                p2_startup = 0
                                p2_direction = -1
                            else:
                                # p2 fait lj
                                p2_etat = prepa
                                p2_coup = "lj"
                                p2_startup = 0
                                if (p2_x-1-p1_x)**2 > (p2_x-p1_x)**2:
                                    p2_direction = 1
                                else:
                                    p2_direction = -1
                        elif KeysPressed[pygame.K_LEFT] :
                            if (p2_x-1-p1_x)**2 > (p2_x-p1_x)**2: # p2 fait nj
                                p2_coup = "nj"
                                p2_etat = prepa
                                p2_startup = 0
                                p2_direction = 1
                            else: # p2 fait fk
                                bb=0
                                p2_startup = 0
                                p2_etat = prepa
                                p2_coup = "fj"
                                p2_direction = -1
                        elif KeysPressed[pygame.K_RIGHT] :
                            if (p2_x+1-p1_x)**2 > (p2_x-p1_x)**2: # p2 fait nj
                                p2_coup = "nj"
                                p2_etat = prepa
                                p2_startup = 0
                                p2_direction = -1
                            else: # p2 fait fj
                                bb=0
                                p2_startup = 0
                                p2_etat = prepa
                                p2_coup = "fj"
                                p2_direction = 1
                        else:
                            # p2 fait nj
                            p2_etat = prepa
                            p2_coup = "nj"
                            p2_startup = 0
                            if (p2_x-1-p1_x)**2 > (p2_x-p1_x)**2:
                                p2_direction = 1
                            else:
                                p2_direction = -1
                    elif KeysPressed[pygame.K_KP3] and not p2_hold :
                        if KeysPressed[pygame.K_DOWN]:
                            # p2 fait lk
                            p2_etat = prepa
                            p2_coup = "lk"
                            p2_startup = 0
                            if (p2_x-1-p1_x)**2 > (p2_x-p1_x)**2:
                                p2_direction = 3
                            else:
                                p2_direction = -3
                        elif KeysPressed[pygame.K_RIGHT]:
                            if (p2_x+1-p1_x)**2 > (p2_x-p1_x)**2: # p2 fait nk
                                p2_coup = "nk"
                                p2_etat = prepa
                                p2_startup = 0
                                p2_direction = -3
                            else: # p2 fait fk
                                bb=0
                                p2_startup = 0
                                p2_etat = prepa
                                p2_coup = "fk"
                                p2_direction = 3
            
                        elif KeysPressed[pygame.K_LEFT]:
                            if (p2_x-1-p1_x)**2 > (p2_x-p1_x)**2: # p2 fait nk
                                p2_coup = "nk"
                                p2_etat = prepa
                                p2_startup = 0
                                p2_direction = 3
                            else: # p2 fait fk
                                bb=0
                                p2_startup = 0
                                p2_etat = prepa
                                p2_coup = "fk"
                                p2_direction = -3
                        else:
                            # p2 fait nk
                            p2_etat = prepa
                            p2_coup = "nk"
                            p2_startup = 0
                            if (p2_x-1-p1_x)**2 > (p2_x-p1_x)**2:
                                p2_direction = 3
                            else:
                                p2_direction = -3
                                
                    elif KeysPressed[pygame.K_UP]:
                        p2_coup = "saut"
                        p2_etat = prepa
                        p2_startup = 0
                p2_sprite = liste_sprites[7][3]
            
            if p1_etat == terre:
                p1_hitbox = 150
                if p1_stun == 0:
                    if KeysPressed[pygame.K_j] or KeysPressed[pygame.K_k]:
                        p1_hold = True
                    p1_etat = libre
                    p1_x = p1_xm
                    p1_sprite = liste_sprites[7][0]
                else:
                    p1_stun -=1
                    p1_sprite = liste_sprites[9][2]
            
            if p2_etat == terre:
                p2_hitbox = 150
                if p2_stun == 0:
                    if KeysPressed[pygame.K_KP2] or KeysPressed[pygame.K_KP3]:
                        p2_hold = True
                    p2_etat = libre
                    p2_x = p2_xm
                    p2_sprite = liste_sprites[7][1]
                else:
                    p2_stun -=1
                    p2_sprite = liste_sprites[9][5]
            
            
            p1_pourcentage_pv =  (( p1_pv * 100 ) / 10000)
            if p1_pourcentage_pv <=0:
                p1_pourcentage_pv = 0
            p2_pourcentage_pv =  (( p2_pv * 100 ) / 10000)
            if p2_pourcentage_pv <=0:
                p2_pourcentage_pv = -1
        
        
            # Dessin
            zonejaune = pygame.Rect( jdx, jdy, WINDOW_SIZE[0], WINDOW_SIZE[1] )
            screen.blit(fond,(0,0), area = zonejaune)
            screen.blit(barre,(40,40))
            screen.blit(barre,(WINDOW_SIZE[0] - 40 - barre.get_width(),40))
            if ( p1_pourcentage_pv != 100 ) :
                pygame.draw.rect(screen, (255,0,0),(41,41,(barre.get_width()-2) - (barre.get_width()-2) * p1_pourcentage_pv  / 100 ,barre.get_height()-2),0)
        
            if ( p2_pourcentage_pv != 100 ) :
                pygame.draw.rect(screen, (255,0,0),((WINDOW_SIZE[0] - 40) - ((barre.get_width()-2) - (barre.get_width()-2) * p2_pourcentage_pv  / 100)  ,41,(barre.get_width()-2) - (barre.get_width()-2) * p2_pourcentage_pv  / 100 ,barre.get_height()-2),0)
                #Afficher p1 et p2
            # if p1_x < p2_x:
            #     screen.blit(p1_sprite,(p1_x-jdx  ,p1_y))
            #     screen.blit(pygame.transform.flip(p2_sprite,True,False),(p2_x-jdx -205 ,p2_y))
        
            #   else:
            #     screen.blit(pygame.transform.flip(p1_sprite,True,False),(p1_x-jdx -205 ,p1_y))
            #     screen.blit(p2_sprite,(p2_x-jdx  ,p2_y))
        
            if p1_direction > 0:
                screen.blit(p1_sprite,(p1_x-jdx  ,p1_y))
            else:
                screen.blit(pygame.transform.flip(p1_sprite,True,False),(p1_x-jdx -205 ,p1_y))
                
            if p2_direction > 0:
                screen.blit(p2_sprite,(p2_x-jdx  ,p2_y))
            else:
                screen.blit(pygame.transform.flip(p2_sprite,True,False),(p2_x-jdx -205 ,p2_y))
                
        
            if p1_pv<=0 or p2_pv<=0:
                break
        
        
        
            # Go ahead and update the screen with what we've drawn.
            pygame.display.flip()
            # Frames par seconde = 60
            clock.tick(60)
            
        if not done and play:
            if p1_pv<=0:
                p2_score +=1
            elif p2_pv<=0:
                p1_score += 1
            round +=1
            count = 0
            while count <=150:
                count+=1
                zonejaune = pygame.Rect( jdx, jdy, WINDOW_SIZE[0], WINDOW_SIZE[1] )
                screen.blit(fond,(0,0), area = zonejaune)
                screen.blit(barre,(40,40))
                screen.blit(barre,(WINDOW_SIZE[0] - 40 - barre.get_width(),40))
                if ( p1_pourcentage_pv != 100 ) :
                    pygame.draw.rect(screen, (255,0,0),(40,40,barre.get_width() - barre.get_width() * p1_pourcentage_pv  / 100 ,barre.get_height()),0)
            
                if ( p2_pourcentage_pv != 100 ) :
                    pygame.draw.rect(screen, (255,0,0),((WINDOW_SIZE[0] - 39) - (barre.get_width() - barre.get_width() * p2_pourcentage_pv  / 100)  ,40,barre.get_width() - barre.get_width() * p2_pourcentage_pv  / 100 ,barre.get_height()),0)
                if p1_direction > 0:
                    screen.blit(p1_sprite,(p1_x-jdx  ,p1_y))
                else:
                    screen.blit(pygame.transform.flip(p1_sprite,True,False),(p1_x-jdx -205 ,p1_y))
                    
                if p2_direction > 0:
                    screen.blit(p2_sprite,(p2_x-jdx  ,p2_y))
                else:
                    screen.blit(pygame.transform.flip(p2_sprite,True,False),(p2_x-jdx -205 ,p2_y))
                if count >=20 and count <=135:
                    screen.blit(ko,(0,0))
                pygame.display.flip()
                
    buffer2 = 0
    while not done and play:
        KeysPressed = pygame.key.get_pressed()
        if not(pygame.mixer.music.get_busy()) :    
            pygame.mixer.music.play()
        if KeysPressed[pygame.K_j] and buffer2>=50:
            menuj_hold = True
            buffer = 0
            break
        jdx=350
        jdy=0
        zonejaune = pygame.Rect( jdx, jdy, WINDOW_SIZE[0], WINDOW_SIZE[1] )
        screen.blit(fond,(0,0), area = zonejaune)
        event = pygame.event.Event(pygame.USEREVENT)    # Remise à zero de la variable event
    
        for event in pygame.event.get():  # User did something
    
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
        if p1_score >=2:
            screen.blit(p1_win,(0,0))
        elif p2_score >=2:
            screen.blit(p2_win,(0,0))
        pygame.display.flip()
        buffer2+=1
    play = False
    tuto = False
pygame.quit()
        
        
        
        
        
        
        
        
        
