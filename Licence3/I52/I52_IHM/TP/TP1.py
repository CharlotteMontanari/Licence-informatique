def couleur(fichier):
    file = open(fichier, "r")
    line = file.readlines()
    dico = {}
    for ligne in line:
        k = []
        k += ligne.split()
        dico[tuple(k[0:3])] = k[3:]
    liste = []
    i = 0
    for i in dico:
        liste += dico[i]
    return dico
#print(couleur("rgb.txt"))