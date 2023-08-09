# (4)
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
delta = b**2-4*a*c
if delta > 0:
    print("Il y a 2 solutions et delta:", delta)
    x1 = (-b-(delta**0.5))/(2*a)
    x2 = (-b+(delta**0.5))/(2*a)
    print("x1:", x1,"x2:", x2)
elif delta == 0:
    print("Il y a 1 solution et delta:", delta)
    x = -b/(2*a)
    print(x)
else:
    print("aucune solution")