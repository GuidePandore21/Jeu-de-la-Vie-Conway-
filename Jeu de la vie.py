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

def combienDeVoisin(matrice, x, y):
    nbVoisin = 0
    for x in range(-1, 2, 1):
        for y in range(-1, 2, 1):
            print(x, y)
            if x == 0 and y == 0:
                pass
            else:
                try:
                    if matrice[x][y] == 1:
                        nbVoisin += 1
                except:
                    pass
    return nbVoisin

def prochaineMatrice(matrice):
    newMatrice = initMatrice(HEIGHT // 10, WIDTH // 10)
    for x in range(len(matrice)):
        for y in range(len(matrice[x])):
            if matrice[x][y] == 0:
                if combienDeVoisin(matrice, x, y) == 3:
                    newMatrice[x][y] = 1
            if matrice[x][y] == 1:
                if combienDeVoisin(matrice, x, y) == 2 or combienDeVoisin(matrice, x, y) == 3:
                    newMatrice[x][y] = 1
    return newMatrice

def changerValeurMatrice(matrice, x, y, newValeur):
    matrice[x][y] = newValeur
    
MATRICE = initMatrice(HEIGHT // 10, WIDTH // 10)
    
# -------------------- PYGAME --------------------#

pygame.init()
SCREEN = pygame.display.set_mode((HEIGHT, WIDTH))
CLOCK =pygame.time.Clock()
RUNNING = True
DT = 0

while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
    
    SCREEN.fill("green")
    
    for x in range(len(MATRICE)):
        for y in range(len(MATRICE[x])):
            if MATRICE[x][y] == 0 :
                pygame.draw.rect(SCREEN, "black", [x * 10, y * 10, 10, 10])
            else:
                pygame.draw.rect(SCREEN, "white", [x * 10, y * 10, 10, 10])
    
    pygame.display.flip()
    
    MATRICE = prochaineMatrice(MATRICE)
    
    DT = CLOCK.tick(60) / 1000

pygame.quit()