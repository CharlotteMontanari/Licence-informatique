l1 = input("l1: ")
copie = [0] * len(l1)
print(copie)
i, j = 0, -1
while i < len(l1):
    copie[j] = l1[i]
    i,j = i+1,j-1
print(copie)

L = "4616843221"
maxi = L[0]
i = 0
while i < len(L):
    if maxi < L[i]:
        maxi = L[i]
    i = i + 1
print(maxi)

chaine = input("chaine: ")
print(chaine.replace(' ',''))