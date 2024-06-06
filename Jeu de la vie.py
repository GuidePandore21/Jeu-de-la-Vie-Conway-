import pygame

HEIGHT = 100
WIDTH = 100

# -------------------- FONCTIONS --------------------#

def initMatrice(longueur, largeur):
    matrice = []
    
    for x in range(largeur):
        matrice.append([])
        for y in range(longueur):
            matrice[x].append(0)
    
    return matrice

def changerValeurMatrice(matrice, x, y, newValeur):
    matrice[x][y] = newValeur
    
# -------------------- PYGAME --------------------#

pygame.init()
SCREEN = pygame.display.set_mode((HEIGHT, WIDTH))
CLOCK =pygame.time.Clock()
RUNNING = True
DT = 0

while RUNNING:
    for event in pygame.event.get():
        if event.type() == pygame.QUIT:
            RUNNING = False
    
    SCREEN.fill("green")
    
    # Code
    
    DT = CLOCK.tick(60) / 1000