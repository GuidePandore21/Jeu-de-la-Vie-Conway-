import pygame
import tkinter as tk
from tkinter import messagebox

HEIGHT = 100
WIDTH = 100
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
    
# -------------------- PYGAME --------------------#

# pygame.init()
# SCREEN = pygame.display.set_mode((HEIGHT, WIDTH))
# CLOCK = pygame.time.Clock()
# RUNNING = True
# DT = 0

# while RUNNING:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             RUNNING = False
    
#     SCREEN.fill("green")
    
#     for x in range(len(MATRICE)):
#         for y in range(len(MATRICE[x])):
#             if MATRICE[x][y] == 0 :
#                 pygame.draw.rect(SCREEN, "black", [x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE])
#             else:
#                 pygame.draw.rect(SCREEN, "white", [x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE])
    
#     pygame.display.flip()
    
#     MATRICE = prochaineMatrice(MATRICE)
    
#     DT = CLOCK.tick(60) / 1000
    
#     pygame.time.wait(1000)

# pygame.quit()

# -------------------- INTERFACE --------------------#

root = tk.Tk()
root.title("Jeu de la vie - Conway")
root.geometry("500x500")

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

buttons = [[None for _ in range(COLS)] for _ in range(ROWS)]

for row in range(ROWS):
    for col in range(COLS):
        button = tk.Button(root, bg='black', fg='white', command=lambda r=row, c=col: onCelluleClick(r, c), width=2, height=1)
        button.grid(row=row, column=col,)
        buttons[row][col] = button

root.mainloop()