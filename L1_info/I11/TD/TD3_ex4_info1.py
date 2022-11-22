# (1)
ch = input("Saisir un mot: ")
pos = int(input("Saisir une position: "))
cp = ''
i = 0
while i < len(ch):
    if i != pos:
        cp = cp + ch[i]
    i = i + 1
print(cp)

# (2)
ch = input("Saisir un mot: ")
cp = ''
i = 0
while i < len(ch):
    if ch[i] == ";" or i == ".":
        cp = cp + ','
    else:
        cp = cp + ch[i]
    i = i + 1
print(cp)

# (3)
c1 = input("c1: ")
c2 = input("c2: ")
ch = input("Saisir un mot: ")
cp = ''
i = 0
while i < len(ch):
    if ch[i] == c1:
        cp = cp + c2
    else:
        cp = cp + ch[i]
    i = i + 1
print(cp)