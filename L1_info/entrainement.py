def echanger(liste, i, j):
    aux = liste[i]
    liste[i] = liste[j]
    liste[j] = aux

#def ordre_alphabetique(liste):
#    mot = 0
#    comp = 0
#    fin_liste = len(liste) - 1
#    while comp < fin_liste:
#        lettre = 0
#        variant = mot + 1
#        while variant <= fin_liste:
#            if ord(liste[mot][lettre]) > ord(liste[variant][lettre]):
#                echanger(liste, mot, variant)
#                variant += 1
#            elif ord(liste[mot][lettre]) == ord(liste[variant][lettre]):
#                lettre += 1
#                if len(liste[mot][lettre]) > len(liste[variant][lettre]):
#                    echanger(liste, mot, variant)
#                if ord(liste[mot][lettre]) != ord(liste[variant][lettre]):
#                    if ord(liste[mot][lettre]) > ord(liste[variant][lettre]):
#                        echanger(liste, mot, variant)
#            else:
#                variant += 1
#        mot += 1
#        comp += 1
#    return liste
#la_liste = ['zoo', 'coucou', 'cou', 'cousou', 'alors', 'bonjour']
#print(ordre_alphabetique(la_liste))

def compare_mots(ch1, ch2):
    lettre = 0
    while lettre < len(ch1) and lettre < len(ch2):
        if ord(ch1[lettre]) > ord(ch2[lettre]):
            return ch2
        elif ord(ch1[lettre]) < ord(ch2[lettre]):
            return ch1
        lettre += 1
    if lettre == len(ch2):
        if ch2 in ch1:
            return ch2
    return ch1
chr1 = 'coucou'
chr2 = 'cou'
print(compare_mots(chr1, chr2))

duration = '13:05'
heure, minute = duration.split(':')
heure = int(heure)
minute = int(minute)
print(heure * 60 + minute)