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
    
    DT = CLOCK.tick(60) / 1000

pygame.quit()