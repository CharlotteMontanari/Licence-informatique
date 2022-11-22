def f(x, a, b):
    if a > b:
        a, b = b, a
    if x <= a:
        print(a)
    elif x >= b:
        print(b)
    else:
        if (x - a) > (b - x):
            print(b)
        else:
            print(a)

f(2, 0, 2)

