def BaryCentre(l):
    somme = 0
    i = 0
    while i < len(l):
        somme += l[i]
        i += 1
    j = 0
    centre = 0
    while centre < somme:
        centre += l[j]
        somme -= l[j]
        j += 1
    return j-1
liste = [1,2,3,4,5,6]
print(BaryCentre(liste))
