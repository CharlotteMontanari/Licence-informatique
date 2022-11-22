ch = input("Saisir une chaine:")
i = 0
som = 0
while i < len(ch):
    if ch[i] == ' ':
        som = som + 1
    i = i + 1
print("Il y a", som, "espace(s)")