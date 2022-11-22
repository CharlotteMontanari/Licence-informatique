e_d = input("encode ou décode: ")
cle = int(input("Clé de chiffrement: "))
txt = input("Saisir un texte: ")
new_txt = ""
i = 0
while i < len(txt):
    if e_d == "encode":
        if txt[i] == ' ':
            new_txt += txt[i]
        else:
            new_txt += chr((ord(txt[i])) + cle)
    elif e_d == "decode":
        if txt[i] == ' ':
            new_txt += txt[i]
        else:
            new_txt += chr((ord(txt[i])) - cle)
    i += 1
print(new_txt)