def echanger(liste, i, j):
    aux = liste[i]
    liste[i] = liste[j]
    liste[j] = aux

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