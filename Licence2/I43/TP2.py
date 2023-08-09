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
    return [a, u%mod, v1]

def enumere_keys(n):
    liste = []
    mod = n
    for el in range(2, n):
        for i in range(1, n):
            if euclide_e(el, n)[0] == 1:
                liste += [[el, i, (euclide_e(el, n)[2])%n]]
    return liste
#print(enumere_keys(29))

def brute_force(fic, n, esp):
    fichier = open(fic, 'r')
    for ligne in fichier:
        for car in ligne:
            print(car)
    fichier.close()
nom = "crypto1.txt"
#print(brute_force(nom, 10, 5))