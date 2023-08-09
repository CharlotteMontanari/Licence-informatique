n1 = int(input("n1= "))
n2 = int(input("n2= "))
L = ["Bonjour", " ", "a", " tout", " le", " monde !!"]
Inf = []
Entre = []
Sup = []
i = 0
while i < len(L):
    if n1 < n2:
        if len(L[i]) < n1:
            Inf = Inf + [L[i]]
        elif len(L[i]) >= n1 and len(L[i]) <= n2:
            Entre = Entre + [L[i]]
        else:
            Sup = Sup + [L[i]]
    elif n2 < n1:
        if len(L[i]) < n2:
            Inf = Inf + [L[i]]
        elif len(L[i]) >= n2 and len(L[i])<=n1:
            Entre = Entre + [L[i]]
        else:
            Sup = Sup + [L[i]]
    i = i + 1
if n1 < n2:
    print("Chaines de longueur <", n1, " : ", Inf)
    print("Chaines de longueur entre", n1, " et ", n2, " : ", Entre)
    print("Chaines de longueur >", n2, " : ", Sup)
else:
    print("Chaines de longueur <", n2, " : ", Inf)
    print("Chaines de longueur entre", n2, " et ", n1, " : ", Entre)
    print("Chaines de longueur >", n1, " : ", Sup)

L = [-2,6,8,12,7,-7,14,13]
i = 0
min = L[i]
max = L[i]
while i < len(L):
    if L[i] <= min:
        min = L[i]
    if L[i] >= max:
        max = L[i]
    i = i + 1
print("min =", min)
print("max =", max)