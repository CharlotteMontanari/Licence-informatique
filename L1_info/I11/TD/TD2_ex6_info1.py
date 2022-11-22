# etoile paire
etoile = ''
i = 2
while i <= 8:
    etoile = etoile + '**'
    print(etoile)
    i = i + 1

# etoile impaire
etoile = '*'
i = 1
while i <= 8:
    etoile = etoile + '**'
    print(etoile)
    i = i + 1

# etoile puissance
etoile = '*'
i = 2
while i <= 8:
    print(etoile)
    etoile = etoile + etoile
    i = i + 1