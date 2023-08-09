def parcours_ligne(n):
    case = []
    l, c = 0, 0
    while l < n:
        while c < n:
            case += [(c, l)]
            c += 1
        l += 1
        c = 0
    return case
    
def parcours_colonne(n):
    case = []
    l, c = 0, 0
    while c < n:
        while l <n:
            case += [(c, l)]
            l += 1
        c += 1
        l = 0
    return case
    
def parcours_diagonal(n):
    case = []
    lig, col = 0, n - 1
    l, c = lig, col
    case += [(c, l)]
    while l != n - 1:
        col -= 1
        l, c = lig, col
        while c != n - 1:
            case += [(c,l)]
            c += 1
            l += 1
        case += [(c, l)]
    while l != n and c != 0:
        lig += 1
        l, c = lig, col
        while l != n - 1:
            case += [(c, l)]
            c += 1
            l += 1
        case += [(c, l)]
    return case

def parcours_antidiagonal(n):
    case = []
    lig, col = n - 1, n - 1
    l, c = lig, col
    case += [(l, c)]
    while col > 0:
        col -= 1
        l, c = lig, col
        while c < n-1 and l > 0:
            case += [(c, l)]
            c += 1
            l -= 1
        case += [(c, l)]
    while lig > 0:
        lig -= 1
        l, c = lig, col
        while l > 0:
            case += [(c, l)]
            c += 1
            l -= 1
        case += [(c, l)]
    return case
    
def parcours_serpentin(n):
    case = []
    l, c = 0, 0
    case += [(c, l)]
    i = 1
    j = 1
    while l != n // 2 and c != n // 2:
        while c < n - i:
            c += 1
            case += [(c, l)]
        while l < n - i:
            l += 1
            case += [(c, l)]
        while c > j - 1:
            c -= 1
            case += [(c, l)]
        while l > j:
            l -= 1
            case += [(c, l)]
        i += 1
        j += 1
    if n % 2 != 0:
        c += 1
        case += [(c, l)]
    return case

def parcours_sinusoidal(n):
    case = []
    l, c = 0, 0
    case += [(c, l)]
    while c < n - 1:
        while l < n - 1:
            l += 1
            case += [(c, l)]
        if c == n - 1:
            break
        c += 1
        case += [(c, l)]
        while l > 0:
            l -= 1
            case += [(c, l)]
        c += 1
        case += [(c, l)]
    return case

def parcours_zigzag(n):
    case = []
    l, c = 0, 0
    case += [(c, l)]
    while l < n - 1:
        while c < n - 1:
            c += 1
            case += [(c, l)]
        if l == n - 1:
            break
        l += 1
        case += [(c, l)]
        while c > 0:
            c -= 1
            case += [(c, l)]
        l += 1
        case += [(c, l)]
    return case
