l_chaine = input("Chaine: ")
ch_min = l_chaine[0]
i = 0
while i < len(l_chaine):
    if len(l_chaine[i]) < len(ch_min):
        ch_min = ch_min + l_chaine[i]
    i = i + 1
print(ch_min)

l_tuple = [(-6, 5, 2), (3, 5, 5)]
l_1 = []
for tup in l_tuple:
    som = 0
    for el in tup:
        som = som + el
    if som <= 1:
        l_1 += [tup]
print(l_1)

ch = input('Entrez une chaine de caracteres : ')
pair = int(len(ch))
n = 0
if pair / 2 == pair // 2:
    while n < pair // 2:
        print(ch[0+n] + ch[-1-n])
        n = n + 1
else:
    while n < pair // 2:
        print(ch[0+n] + ch[-1-n])
        n = n + 1
    print(ch[n])

ch = input("Saisir un mot: ")
car = input("Saisir la lettre a doubler: ")
sh = ""
i = 0
while i < len(ch):
    if car == ch[i]:
        sh = sh + ch[i]
        sh = sh + ch[i]
        i = i + 1
    else:
        sh = sh + ch[i]
        i = i + 1
print(sh)