#tp fait avec la librairie du prof

taille_ecran = 500
epaisseur_ligne = 10
increment = 1

init_window('TP6', taille_ecran, taille_ecran)

i = 0
delta = 0
while i < taille_ecran:
    if delta <255:
        hex_value = delta
        # On affiche la meme couleur 2 fois
        if i % 2 == 0:
            delta += increment
    else:
        hex_value = 255
    current_color(hex_value, hex_value, hex_value)
    line(0, i, taille_ecran, i, epaisseur_ligne)
    i += increment

main_loop()


from random import randrange
i = 0
liste = [0, 0, 0, 0, 0, 0]
while i < 10000:
    a = randrange(1, 7) # a va etre pris aleatoirement entre 1 et 6
    if a == 1:
        liste[0] += 1
    elif a == 2:
        liste[1] += 1
    elif a == 3:
        liste[2] += 1
    elif a == 4:
        liste[3] += 1
    elif a == 5:
        liste[4] += 1
    else:
        liste[5] += 1
    i += 1
print(liste)