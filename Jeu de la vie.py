import pygame

HEIGHT = 1000
WIDTH = 1000
CELL_SIZE = 10
ROWS = HEIGHT // CELL_SIZE
COLS = WIDTH // CELL_SIZE

# -------------------- FONCTIONS --------------------#

def initMatrice(rows, cols):
    matrice = []
    for y in range(rows):
        matrice.append([0] * cols)
    return matrice

def combienDeVoisin(matrice, x, y):
    nbVoisin = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(matrice) and 0 <= ny < len(matrice[0]):
                if matrice[nx][ny] == 1:
                    nbVoisin += 1
    return nbVoisin

def prochaineMatrice(matrice):
    newMatrice = initMatrice(ROWS, COLS)
    for y in range(ROWS):
        for x in range(COLS):
            if matrice[x][y] == 0:
                if combienDeVoisin(matrice, x, y) == 3:
                    newMatrice[x][y] = 1
            elif matrice[x][y] == 1:
                if combienDeVoisin(matrice, x, y) in [2, 3]:
                    newMatrice[x][y] = 1
    return newMatrice

def changerValeurMatrice(matrice, x, y, newValeur):
    matrice[x][y] = newValeur

MATRICE = initMatrice(ROWS, COLS)

# changerValeurMatrice(MATRICE, HEIGHT // 2, WIDTH // 2, 1)
    
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
                pygame.draw.rect(SCREEN, "black", [x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE])
            else:
                pygame.draw.rect(SCREEN, "white", [x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE])
    
    pygame.display.flip()
    
    MATRICE = prochaineMatrice(MATRICE)
    
    DT = CLOCK.tick(60) / 1000
    
    pygame.time.wait(1000)

pygame.quit()
