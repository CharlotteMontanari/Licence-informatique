def string_to_state_message(message):
    tableau = [[], [], [], []]
    i = 0
    for el in range(len(message)):
        tableau[el%4] += [ord(message[el])]
    return tableau
#print(string_to_state_message("Abasourdissantes"))

def euclide_e(a, n):
    mod = n
    u = 1
    v = 0
    u1 = 0
    v1 = 1
    while n != 0:
        u, v, u1, v1 = u1, v1, u - a//n * u1, v - a//n * v1
        #print(u1, v1)
        a, n = n, a%n
        #print("a:",a)
        #print("n:",n)
    return u%mod #[a, u%mod, v1]

def subbytes(etat):
    A = [[1,0,0,0,1,1,1,1], [1,1,0,0,0,1,1,1], [1,1,1,0,0,0,1,1], [1,1,1,1,0,0,0,1],
         [1,1,1,1,1,0,0,0], [0,1,1,1,1,1,0,0], [0,0,1,1,1,1,1,0], [0,0,0,1,1,1,1,1]]
    b = [1,1,0,0,0,1,1,0]
    for liste in range(len(etat)):
        for el in range(len(etat[0])):
            x = etat[liste][el]
            y = 0
            if x != 0:
                inverse = inv(x)
            s = 0
            for i in range(len(A)):
                somme = 0
                for j in range(len(A[0])):
                    y = (inverse >> j) & 1
                    somme ^= (A[i][j] & y)
                somme ^= b[i]
                s |= somme << i
            etat[liste][el] = s
    return etat
#print(subbytes([[65, 111, 105, 110], [98, 117, 115, 116], [97, 114, 115, 101], [115, 100, 97, 115]]))

def shiftrows(etat):
    liste = [0]*len(etat)
    liste[0] = etat[0]
    liste[1] = etat[1:] + etat[0]
    liste[2] = etat[2:] + etat[:2]
    liste[3] = etat[3:] + etat[-1]
    return liste
print(shiftrows([[65, 111, 105, 110], [98, 117, 115, 116], [97, 114, 115, 101], [115, 100, 97, 115]]))