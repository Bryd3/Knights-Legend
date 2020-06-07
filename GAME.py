
import pygame
import time
import random
from pygame.locals import*
pygame.init()

#Variables:
pnjtype = 0 #Type d'ennemie
ph = 1 #Phase qui commence
a = 0 #Menu A
b = 0 #Menu B
d = 0 #Partie du menu joueur
e = 0
g = 0
pva = 100
pvb = 100
f = 0
#Taille de la fenêtre
fenetre = pygame.display.set_mode((600, 480))

#Chargement des éléments graphiques:
#Chargement et collage du fond:
fond = pygame.image.load("fond.png").convert()
fenetre.blit(fond, (0,0))
#Chargement des personnages:
player = pygame.image.load("sprite1.png").convert_alpha()
if pnjtype == 0: #Différents types d'ennemies:
    player2 = pygame.image.load("sprite2.png").convert_alpha()
else:
    player2 = pygame.image.load("sprite1.png").convert_alpha()
position = player.get_rect()
position2 = player.get_rect()
position = position.move(-200,200)
position2 = position2.move(600,200)
start_time = time.time()
#Chargement des menus et interfaces:
#Menus:
menu1 = pygame.image.load("menu1.png").convert_alpha()
menu2 = pygame.image.load("menu2.png").convert_alpha()
menu3 = pygame.image.load("menu3.png").convert_alpha()
#Interfaces:
barre = pygame.image.load("barre.png").convert_alpha()
pv = pygame.image.load("pv.png").convert_alpha()
pv = pygame.transform.scale(pv,(2,4))
barre = pygame.transform.scale(barre,(208,10))
t = pygame.image.load("time.png").convert_alpha()
pv2 = pygame.transform.scale(pv,(8,16))
positionpv = pv.get_rect()
positionpv = positionpv.move(50, 100)

#PHASE 1 : ANIMATION DÉBUT
for x in range(120):
     fenetre.blit(fond, position, position)
     fenetre.blit(fond, position2, position2)
     position = position.move(2, 0)
     position2 = position2.move(-2,0)
     fenetre.blit(player, position)
     fenetre.blit(player2, position2)
     pygame.display.update()
     pygame.time.delay(5)
#PHASE 2 : BOUCLE JOUEUR-ADVERSAIRE
while pva>0 and pvb>0:

#PHASE 2.1 : JOUEUR
    while ph == 1:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    a=a-1
                    print(a)
                if event.key == K_RIGHT:
                    a=a+1
                    print(a)
                if event.key == K_SPACE:
                    if a == 0:
                        g = 0
                        f = 0
                        fenetre.blit(pv2, positionpv)
                        p = random.uniform(0,1)
                        while g == 0 and f<180:
                            for event in pygame.event.get():
                                if event.type == KEYDOWN:
                                    if event.key == K_SPACE:
                                        g = g+1
                            fenetre.blit(fond, positionpv, positionpv)
                            fenetre.blit(t,(44,95))
                            fenetre.blit(pv2,(p*360+50,100))
                            positionpv = positionpv.move(2, 0)
                            f = f+1
                            fenetre.blit(pv2, positionpv)
                            pygame.display.update()
                            pygame.time.delay(5)

                        positionpv = positionpv.move(-(2*f)-1,0)
                        f = f+1
                        elapsed_time = time.time() - start_time

                        if f!=181:
                            e=e+1
                        if elapsed_time > (p-0.5) and elapsed_time < (p+0.5) and f!=180:
                            e=e+1
                        if elapsed_time > (p-0.3) and elapsed_time < (p+0.3) and f!=180:
                            e=e+1
                        if elapsed_time > (p-0.1) and elapsed_time < (p+0.1) and f!=180:
                            e=e+1
                        if elapsed_time > (p-0.05) and elapsed_time < (p+0.05) and f!=180:
                            e=e+1

                        for x in range(20): #Animation attaque
                             fenetre.blit(fond, position, position)
                             position = position.move(2, 0)
                             fenetre.blit(player, position)
                             fenetre.blit(player2, position2)
                             pygame.display.update()
                             pygame.time.delay(2)

                        for x in range(20):
                             fenetre.blit(fond, position, position)
                             position = position.move(-2, 0)
                             fenetre.blit(player, position)
                             fenetre.blit(player2, position2)
                             pygame.display.update()
                             pygame.time.delay(2)
                        pvb = pvb-(5*e)
                    if a == 1:
                        pva = pva+5

                    if a == 2:
                        pva = pva
                    ph = 2

            if a == 1:
                a = 1
                fenetre.blit(fond, (0,0))
                fenetre.blit(menu2, (0,0))

            if a == 2 or a == -1:
                a = 2
                fenetre.blit(fond, (0,0))
                fenetre.blit(menu3, (0,0))

            if a == 0 or a == 3:
                a = 0
                fenetre.blit(fond,(0,0))
                fenetre.blit(menu1, (0,0))

            fenetre.blit(player, position)
            fenetre.blit(player2, position2)
            fenetre.blit(barre, (20, 50))
            fenetre.blit(barre, (370, 50))
            for i in range(0,pva+1):
                fenetre.blit(pv, (2*i+22,52))
            for i in range(0,pvb+1):
                fenetre.blit(pv, (2*i+372,52))
            pygame.display.flip()

#PHASE 2.2 : ENNEMIE
    while ph == 2:

        pygame.time.delay(500)
        for x in range(20): #Animation attaque
             fenetre.blit(fond, position2, position2)
             position2 = position2.move(-2, 0)
             fenetre.blit(player, position)
             fenetre.blit(player2, position2)
             pygame.display.update()
             pygame.time.delay(2)

        for x in range(20):
             fenetre.blit(fond, position2, position2)
             position2 = position2.move(2, 0)
             fenetre.blit(player, position)
             fenetre.blit(player2, position2)
             pygame.display.update()
             pygame.time.delay(2)
        pva = pva - 10
        d = 0
        ph = 1

    fenetre.blit(barre, (20, 50))
    fenetre.blit(barre, (370, 50))
    for i in range(0,pva+1):
        fenetre.blit(pv, (i+22,52))
    for i in range(0,pvb+1):
        fenetre.blit(pv, (i+372,52))
    pygame.display.flip()
