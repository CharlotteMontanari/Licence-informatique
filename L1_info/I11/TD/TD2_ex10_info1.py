# (1)
n = int(input("Saisir un chiffre: "))
max = n 
while n != 0:
    if n > max :
        max = n
    n = int(input("Saisir un chiffre: "))
print(max)

# (2)
n = int(input("Nombre de valeur a saisir"))
val = int(input())
max = val
i = 1
while i < n :
    if val > max :
        max = n
    val = int(input())
    i = i + 1
    print(max)