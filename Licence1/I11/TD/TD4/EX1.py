from math import *

n = int(input())
x = int(input())
i = 1
som = cos(0)
while i <= n :
    som = som + cos(i*x)
    i = i + 1
    if som == 1/2 + ((sin((2*n+1)*x)) / 2 *(sin(x/2))):
        print(True)
    else:
        print(False)
    print(som == 1/2 + ((sin((2*n+1)*x)) / 2 * (sin(x/2))))