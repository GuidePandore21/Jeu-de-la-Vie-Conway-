import pygame
import tkinter as tk
from tkinter import messagebox

WIDTH = 100
HEIGHT = 50
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
    for x in range(ROWS):
        for y in range(COLS):
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
    
# -------------------- PYGAME --------------------#
def jeuDelaVie(matrice):
    pygame.init()
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    CLOCK = pygame.time.Clock()
    RUNNING = True
    DT = 0

    while RUNNING:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
        
        SCREEN.fill("green")
        
        for x in range(len(matrice)):
            for y in range(len(matrice[x])):
                if matrice[x][y] == 0 :
                    pygame.draw.rect(SCREEN, "black", [y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE])
                else:
                    pygame.draw.rect(SCREEN, "white", [y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE])
        
        pygame.display.flip()
        
        newMatrice = prochaineMatrice(matrice)
        matrice = newMatrice
        
        DT = CLOCK.tick(60) / 1000
        
        pygame.time.wait(1000)

    pygame.quit()

# -------------------- INTERFACE --------------------#

root = tk.Tk()
root.title("Jeu de la vie - Conway")
root.geometry("1000x600")

def onCelluleClick(row, col):
    button = buttons[row][col]
    current_color = button.cget('bg')
    
    if current_color == 'black':
        new_color = 'white'
        changerValeurMatrice(MATRICE, row, col, 1)
    else:
        new_color = 'black' 
        changerValeurMatrice(MATRICE, row, col, 0)
    
    button.config(bg=new_color)

def onStartButtonClick():
    jeuDelaVie(MATRICE)

buttons = [[None for _ in range(COLS)] for _ in range(ROWS)]

for row in range(ROWS):
    for col in range(COLS):
        button = tk.Button(root, bg='black', fg='white', command=lambda r=row, c=col: onCelluleClick(r, c), width=2, height=1)
        button.grid(row=row, column=col,)
        buttons[row][col] = button
        
startButton = tk.Button(root, text="Start", bg='blue', fg='white', width=10, height=2, command=lambda r=ROWS + 3, c=COLS // 2: onStartButtonClick())
startButton.grid(row=ROWS + 3, column=COLS, pady=10, padx=10, sticky='se')

root.mainloop()