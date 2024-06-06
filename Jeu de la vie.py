def initMatrice(longueur, largeur):
    matrice = []
    
    for x in range(largeur):
        matrice.append([])
        for y in range(longueur):
            matrice[x].append(0)
    
    return matrice

print(initMatrice(3, 3))