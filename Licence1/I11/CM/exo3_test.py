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