def cases_fou(col, lig):
    l, c = lig + 1, col + 1
    case = []
    while l <= 7 and c <= 7:
        case += [(c, l)]
        c, l = c + 1, l + 1

    l, c = lig - 1, col + 1
    while l >= 0 and c <= 7:
        case += [(c, l)]
        l, c = l - 1, c + 1

    l, c = lig - 1, col - 1
    while l >= 0 and c >= 0:
        case += [(c, l)]
        l, c = lig - 1, col - 1

    l, c = lig + 1, col -1
    while l <= 7 and c >= 0:
        case += [(c, l)]
        l, c = l + 1, c - 1
    return case

def cases_tour(col, lig):
    l, c = lig + 1, col
    case = []
    while l <= 7:
        case += [(c, l)]
        l += 1

    l, c = lig - 1, col
    while l >= 0:
        case += [(c, l)]
        l -= 1

    l, c = lig, col + 1
    while c <= 7:
        case += [(c, l)]
        c += 1

    l, c = lig, col - 1
    while c >= 0:
        case += [(c, l)]
        c -= 1
    return case

def cases_reine(col, lig):
    l, c = lig + 1, col + 1
    case = []
    while l <= 7 and c <= 7:
        case += [(c, l)]
        l, c = l + 1, c + 1 

    l, c = lig - 1, col + 1
    while l >= 0 and c <= 7:
        case += [(c, l)]
        l, c = l - 1, c + 1

    l, c = lig - 1, col - 1
    while l >= 0 and c >= 0:
        case += [(c, l)]
        l, c = l - 1, c - 1

    l, c = lig + 1, col - 1
    while l <= 7 and c >= 0:
        case += [(c, l)]
        l, c = l + 1, c - 1

    l, c = lig + 1, col
    while l <= 7:
        case += [(c, l)]
        l += 1

    l, c = lig - 1, col
    while l >= 0:
        case += [(c, l)]
        l -= 1

    l, c = lig, col + 1
    while c <= 7:
        case += [(c, l)]
        c += 1

    l, c = lig, col - 1
    while c >= 0:
        case += [(c, l)]
        c -= 1
    return case
    
def cases_roi(col,lig):
   case = []
   l, c = lig + 1, col + 1
   case += [(c, l)]

   l, c = lig, col + 1
   case += [(c, l)]

   l, c = lig - 1, col + 1
   case += [(c, l)]

   l, c = lig - 1, col
   case += [(c, l)]

   l, c = lig - 1, col - 1
   case += [(c, l)]

   l, c = lig, col - 1
   case += [(c, l)]

   l, c = lig + 1, col - 1
   case += [(c, l)]

   l, c = lig + 1, col
   case += [(c, l)]
   return case

def cases_cavalier(col,lig):
    case = []
    if not (col + 2 > 7):
        if not (lig + 1 > 7):
            case += [(col + 2, lig + 1)]
        if not (lig - 1 < 0):
            case += [(col + 2, lig - 1)]

    if not (col - 2 < 0):
        if not (lig + 1 > 7):
            case += [(col - 2, lig + 1)]
        if not (lig - 1 < 0):
            case += [(col - 2, lig - 1)]

    if not (lig + 2 > 7):
        if not (col + 1 >7):
            case += [(col + 1, lig + 2)]
        if not (col - 1< 0):
            case += [(col - 1, lig + 2)]

    if not (lig - 2 < 0):
        if not(col + 1 > 7):
            case += [(col + 1, lig - 2)]
        if not (col - 1 < 0):
            case += [(col - 1, lig - 2)]
    return case

def cases_pion(col,lig):
    case = []
    l, c = lig, col
    if l <= 7 and l > 0:
        if lig == 6:
            l, c = lig - 2, col
            case += [(c, l)]
            l, c = lig - 1, col
            case += [(c, l)]
        else:
            l, c = lig - 1, col
            case += [(c, l)]
    return case