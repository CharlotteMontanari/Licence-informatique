cr = '*'
ch = input( )
lch = len(ch)
nch = ch[0]
i = 1
while i < lch:
    nch = nch + cr + ch[i]
    i = i + 1
print(nch)