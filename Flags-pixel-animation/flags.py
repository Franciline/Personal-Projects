import pygame
import time

# ------------------------- SETTINGS --------------------------------

#INITIALIZATION OF COLORS

#LGBT flag
RED = (254, 0, 0)
ORANGE = (255, 142, 1)
YELLOW = (255, 238, 0)
GREEN = (2, 130, 21)
BLUE = (1, 76, 255)
PURPLE = (138, 1, 140)
BLACK = (179,242,255)

#BISEXUAL flag
PURPLE2 = (214, 2, 112)
PINK = (154, 79, 149)
BLUE2 = (0, 57, 167)

#LESBIAN flag
LES1 = (214, 41, 0)
LES2 = (255, 155, 85)
LES3 = (255, 255, 255)
LES4 = (212, 98, 165)
LES5 = (164, 0, 98)

#PANSEXUAL flag
PAN1 = (255, 33, 140)
PAN2 = (255, 216, 0)
PAN3 = (33, 177, 255)

#ASEXUAL flag
ASSE1 = (0, 0, 0)
ASSE2 = (149, 149, 149)
ASSE3 = (255, 255, 255)
ASSE4 = (102, 0, 102)

#TRANSGENDER flag
TR1 = (91, 206, 250) 
TR2 = (245, 169, 184)
TR3 = (255, 255, 255)

#color settings for each flag: a number correspond a color
lgbtq = [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 0, 0, 0, 0]
bi = [0, 0, 0, 0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 0, 0, 0, 0]
les = [0, 0, 0, 0, 11, 11, 11, 11, 11, 12, 12, 12, 12, 12, 100, 100, 100, 100, 13, 13, 13, 13, 13, 14, 14, 14, 14, 14, 0, 0, 0, 0]
pan = [0, 0, 0, 0, 15, 15, 15, 15, 15, 15, 15, 15, 16, 16, 16, 16, 16, 16, 16, 16, 17, 17, 17, 17, 17, 17, 17, 17, 0, 0, 0, 0]
asse =[0, 0, 0, 0, 18, 18, 18, 18, 18, 18, 19, 19, 19, 19, 19, 19, 20, 20, 20, 20, 20, 20, 21, 21, 21, 21, 21, 21, 0, 0, 0, 0]
trg = [0, 0, 0, 0, 22, 22, 22, 22, 22, 23, 23, 23, 23, 23, 100, 100, 100, 100, 23, 23, 23, 23, 23, 22, 22, 22, 22, 22, 0, 0, 0, 0]

#2D matrix that will represent the screen
tab = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
       [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
       [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
       [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
       [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
       [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3], 
       [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
       [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3], 
       [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
       [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
       [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
       [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
       [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
       [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
       [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
       [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
       [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
       [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
       [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
       [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
       [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

x, y = 40, 20
repeat = 1
screen = pygame.display.set_mode((x * (len(tab[0])+ repeat), y * (len(tab) + repeat))) #x, y

#---------------------------- ANIMATION ------------------------------

def descente(tableau):
    #first column goes down 
    y_max = len(tableau)
    for i in range(y_max-2, -1, -1):
        tableau[i + 1][0] = tab[i][0]
    tableau[0][0] = 0
    return tableau

def monter(tableau):
    #first column goes up
    y_max = len(tableau)
    for i in range(1, y_max):
        tableau[i - 1][0] = tableau[i][0]
    tableau[y_max - 1][0] = 0
    return tableau

def affiche(tableau):
    #shows the colors
    screen.fill(BLACK)

    for j in range(len(tableau)):
        for i in range(len(tableau[0])):    
            
            if tab[j][i] == 0:
                color = BLACK
            if tab[j][i] == 1:
                color = RED
            if tab[j][i] == 2:
                color = ORANGE
            if tab[j][i] == 3:
                color = YELLOW
            if tab[j][i] == 4:
                color = GREEN
            if tab[j][i] == 5:
                color = BLUE
            if tab[j][i] == 6:
                color = PURPLE

            if tab[j][i] == 7:
                color = PURPLE2
            if tab[j][i] == 8:
                color = PINK
            if tab[j][i] == 9:
                color = BLUE2
            
            if tab[j][i] == 11:
                color = LES1
            if tab[j][i] == 12:
                color = LES2
            if tab[j][i] == 100:
                color = LES3
            if tab[j][i] == 13:
                color = LES4
            if tab[j][i] == 14:
                color = LES5

            if tab[j][i] == 15:
                color = PAN1
            if tab[j][i] == 16:
                color = PAN2
            if tab[j][i] == 17:
                color = PAN3

            if tab[j][i] == 18:
                color = ASSE1
            if tab[j][i] == 19:
                color = ASSE2
            if tab[j][i] == 20:
                color = ASSE3
            if tab[j][i] == 21:
                color = ASSE4

            if tab[j][i] == 22:
                color = TR1
            if tab[j][i] == 23:
                color = TR2

            pygame.draw.rect(screen, color, pygame.Rect((i * x, (repeat + j) * y, x, y)))
            #pygame.display.flip()
    return

def following(tableau):
    #each column except the first will be shifted right
    x_max = len(tableau[0])
    y_max = len(tableau)
    for i in range(x_max - 1, 0, -1): 
        for j in range(y_max - 1, -1, -1):
            tableau[j][i] = tableau[j][i-1]
    return tableau

def transition(tableau, ligne):
    #condition: len(tableau) == len(ligne)
    #we only modify the first column of the table, the other columns will follow
    for i in range(len(tableau)):
        tableau[i][0] = ligne[i]
    return tableau

# ---------------------------- LANCEMENT -----------------------------

#repositionnement

tab1 = tab
for i in range(2):
    tab1 = descente(tab1)


#boucle
color = None
temps = 0.1
pygame.init()
compteur = 1
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    #start of the animation

    for i in range(4):
        tab1 = monter(tab1)
        tab1 = following(tab1)
        affiche(tab1)
        pygame.display.flip()
        time.sleep(temps)
    tab1 = following(tab1)
    affiche(tab1)
    pygame.display.flip()
    time.sleep(temps)

    for i in range(2):
        tab1 = descente(tab1)
        tab1 = following(tab1)
        affiche(tab1)
        pygame.display.flip()
        time.sleep(temps)
    tab1 = following(tab1)
    affiche(tab1)
    pygame.display.flip()
    time.sleep(temps)

    for i in range(2):
        tab1 = monter(tab1)
        tab1 = following(tab1)
        affiche(tab1)
        pygame.display.flip()
        time.sleep(temps)
    tab1 = following(tab1)
    affiche(tab1)
    pygame.display.flip()
    time.sleep(temps)
    
    for i in range(4):
        tab1 = descente(tab1)
        tab1 = following(tab1)
        affiche(tab1)
        pygame.display.flip()
        time.sleep(temps)
    tab1 = following(tab1)
    affiche(tab1)
    pygame.display.flip()
    time.sleep(temps)

    for i in range(2):
        tab1 = monter(tab1)
        tab1 = following(tab1)
        affiche(tab1)
        pygame.display.flip()
        time.sleep(temps)
    tab1 = following(tab1)
    affiche(tab1)
    pygame.display.flip()
    time.sleep(temps)

    for i in range(2):
        tab1 = descente(tab1)
        tab1 = following(tab1)
        affiche(tab1)
        pygame.display.flip()
        time.sleep(temps)
    tab1 = following(tab1)
    affiche(tab1)
    pygame.display.flip()
    time.sleep(temps)

    compteur += 0.5

    #we change the flag shown

    if compteur == 2:
        tab1 = transition(tab1, les)
    if compteur == 3:
        tab1 = transition(tab1, bi)
    if compteur == 4:
        tab1 = transition(tab1, asse)
    if compteur == 5:
        tab1 = transition(tab1, pan)
    if compteur == 6:
        tab1 = transition(tab1, trg)
    if compteur == 7:
        tab1 = transition(tab1, lgbtq)
        compteur = 0

pygame.quit()

