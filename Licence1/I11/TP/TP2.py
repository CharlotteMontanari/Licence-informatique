# (1)
note = int(input("saisir une note: "))
if note >= 10:
    if note >= 12 and note < 14:
        print("exament reussit avec mention assez bien")
    elif note >= 14 and note < 16:
        print("examen reussit avec mention bien")
    elif note >= 16 and note <= 20:
        print("examen reussit avec mention tres bien")
else:
    print("examen raté")

# (2)
UE1 = int(input("Note UE1: "))
UE2 = int(input("Note UE2: "))
UE3 = int(input("Note UE3: "))
if (UE1 + UE2 + UE3)/3 >= 10:
    if UE1 < 10 or UE2 < 10 or UE3 < 10:
        print("semestre valide par compensation")
    else:
        print("semestre valide")
else:
    print("session de rattrapage")

# (3)
horaire = str(input("Entrer une heure: "))
h = int(horaire[:2])
# print(h)
m = int(horaire[3:])
# print(m)
if h < 13:
    print("vous etes en avance")
elif h == 13 and m == 0:
    print("vous etes a l'heure")
else:
    print("vous etes en retard")


a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
delta = b**2-4*a*c
if delta > 0:
    print("Il y a 2 solutions et delta:", delta)
    x1 = (-b-(delta**0.5))/(2*a)
    x2 = (-b+(delta**0.5))/(2*a)
    print("x1:", x1,"x2:", x2)
elif delta == 0:
    print("Il y a 1 solution et delta:", delta)
    x = -b/(2*a)
    print(x)
else:
    print("aucune solution")

# (1)
a = int(input("valeur de a: "))
b = int(input("valeur de b: "))
op = input("choix d'operateur(+,-,*,/): ")
if op == '+':
    print(a, "+", b, "=", a + b)
elif op == '-':
    print(a, "-", b, "=", a - b)
elif op == '*':
    print(a, "*", b, "=", a * b)
else:
    print(a, "/", b, "=", a / b)

n1 = int(input("saisir un nombre entier : "))
sommeimp = 0
sommep = 0
while n1 > 0 or n1 < 0 :
    if int(n1/2) == float(n1/2):
        sommep = sommep + n1
    else: 
        sommeimp = sommeimp + n1
    n1 = int(input("saisir un nombre entier : "))
print("somme des entiers pairs : ", sommep)
print("somme des entiers impairs : ", sommeimp)


tdm = int(input("La table de:"))
i = 1
while i <= 10:
    print(tdm * i)
    i = i + 1


# (1)
n = int(input("Donner un  nombre n: "))
S = 0
for i in range(1, n // 2 + 1):
    if n % i == 0:
        S = S + i
if S == n:
    print(n, "est un nombre parfait")
else:      
    print(n, "n'est pas un nombre parfait")

# (2)
n=1
# for n in range (1, 1000):
while  n <1000:
    S = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            S = S + i
    if S == n:
        print(n, "est un nombre parfait")
    n += 1 

# le modulo retourne seulement ce qu'il y a apres la virgule
v = int(input("valeur: "))
if v % 3 == 0:
    print("c'est divisible par 3")
else:
    print("ce n'est pas divisible par 3")


# meme chose sans modulo et sans diviseur
v = int(input("valeur de v: "))
n = 0
diviseur = int(input("diviseur: "))
while n < v:
    n = n + diviseur
if n == v:
    print(f"v est divisible par {diviseur}")
else:
    print(f"v n'est divisible par {diviseur}")

