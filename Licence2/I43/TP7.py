def sbox(a):
    row = ((a >> 5)<<1) | (a & 1)
    column = (a & 30) >> 1
    return [row, column]
#print(sbox(49))

def crypto(a, b):
    liste = [58,50,42,34,26,18,10,2,60,52,44,36,28,20,12,4,62,54,46,38,30,22,14,6,64,56,48,40,32,24,16,8,
             57,49,41,33,25,17,9,1,59,51,43,35,27,19,11,3,61,53,45,37,29,21,13,5,63,55,47,39,31,23,15,7]
    gauche = ''
    droite = ''
    i = 0
    while i < len(liste):
        
a = 0xef6b0deebd3cd2f5
b = 0xfe7a0dfafd6dd7a4
#print(crypto(a, b))