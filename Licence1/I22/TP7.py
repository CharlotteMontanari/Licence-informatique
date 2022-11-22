import random

def init_ram_list(t):
    ram = [0] * t
    return ram
# print(init_ram_list(4)) 

def fill_ram_random(ram, n):
    for i in range(n):
        j = random.randint(0, len(ram)-1)
        while ram[j] != 0:
            j = random.randint(0, len(ram)-1)
        alea = random.randint(1, 255)
        ram[j] = alea
    return ram
# print(fill_ram_random(init_ram_list(6), 2))

def fill_ram_place(ram, n):
    for i in range(n):
        j = random.randint(0, len(ram)-1)
        while ram[j] != 0:
            j = random.randint(0, len(ram)-1)
        ram[j] = j
    return ram
# print(fill_ram_place(init_ram_list(6), 2))

def get_value_list(ram, adresse):
    return ram[adresse]
# print(get_value_list(fill_ram_place(init_ram_list(6), 4), 2))

def init_ram_dict(taille):
    dico = {'taille': taille}
    return dico
# print(init_ram_dict(2))

def fill_ram_random_dict(ram, n):
    for i in range(n):
        j = random.randint(0, ram['taille']-1)
        while j in ram.keys():
            j = random.randint(0, ram['taille']-1)
        alea = random.randint(1, 255)
        ram[j] = alea
    return ram
# print(fill_ram_random_dict(init_ram_dict(10), 6))

def fill_ram_place_dict(ram, n):
    for i in range(n):
        j = random.randint(0, ram['taille']-1)
        while j in ram.keys():
            j = random.randint(0, ram['taille']-1)
        ram[j] = j
    return ram
# print(fill_ram_place_dict(init_ram_dict(10), 6))

def get_value_dict(ram, adresse):
    if adresse > ram['taille']:
        return 'adresse invalide'
    if adresse not in ram.keys():
        return 0
    else:
        return ram[adresse]
# print(get_value_dict(fill_ram_place_dict(init_ram_dict(10), 6), 20))

def in_cache(mem_asso, mem_class, adresse):
    memoire = ()
    if adresse in mem_asso and mem_class[adresse]['ok'] == True:
        memoire += ('HIT',)
        memoire += (mem_class[adresse]['data'],)
    else:
        memoire += ('MISS',)
        memoire += (None,)
    return memoire
mem1 = [4, 1, 2, 0]
mem2 = [{'ok': True, 'data': 0x44}, {'ok': False, 'data': 0xFF},
        {'ok': True, 'data': 0x22}, {'ok': True, 'data': 0x00}]
# print(in_cache(mem1, mem2, 2))

def in_cache_direct_mapped(mem_class, adresse):
    memoire = ()
    if adresse > len(mem_class):
        adresse = adresse % len(mem_class)
    if mem_class[adresse]['ok'] == True:
        memoire += ('HIT',)
        memoire += (mem_class[adresse]['data'],)
    else:
        memoire += ('MISS',)
        memoire += (None,)
    return memoire  
m = [{'ok': True, 'data': 0x00}, {'ok': False, 'data': 0xFF},
     {'ok': True, 'data': 0x22}, {'ok': True, 'data': 0x77}]
# print(in_cache_direct_mapped(m, 7))

def in_cache_direct_mapped_fixed(mem_class, adresse):
    if mem_class[adresse%(len(mem_class))]['ok'] == True:
        if adresse // len(mem_class) == mem_class[adresse%len(mem_class)]['tag']:
            return ('HIT',mem_class[adresse%(len(mem_class))]['data'])
        else:
            return ("MISS", None)
    else:
        return ("MISS", None)
m = [{'ok': True, 'data': 0x00, 'tag': 0x0}, {'ok': False, 'data': 0xFF, 'tag': 0x1},
     {'ok': True, 'data': 0x22, 'tag': 0x0}, {'ok': True, 'data': 0x77, 'tag': 0x1}]
# print(in_cache_direct_mapped_fixed(m, 3))

def replace_ramdom(mem_asso, mem_class):
    memoire = []
    for el in range(len(mem_class)):
        if mem_class[el]['ok'] == False:
            memoire += [el]
    if memoire == '':
        return random.randint(0, len(mem_class))
    else:
        return random.randint(0, len(mem_class))
m1 = [4, 1, 2, 0]
m2 = [{'ok': True, 'data': 0x44}, {'ok': False, 'data': 0xFF},
      {'ok': True, 'data': 0x22}, {'ok': True, 'data': 0x00}]
# print(replace_ramdom(m1, m2))

def add_fifo(fifo, valeur):
    i = 0
    while fifo[i] != None:
        i += 1
    if fifo[i] != None:
        return fifo
    else:
        fifo[i] = valeur
    return fifo
f = [None, None, None, None]
# print(add_fifo(f, 10))
# print(add_fifo(f, 99))

def get_fifo(fifo):
    val = fifo[0]
    fifo2 = fifo
    del fifo2[0]
    fifo2.append(None)
    return (fifo2, val)
f = [10, 99, 2, None]
# print(get_fifo(f))

def replace_fifo(mem, fifo):
    index = fifo[0]
    is_false = False
    for i in range(0, len(mem)):
        if mem[i]["ok"] == False:
            is_false = True
            index = i

    if is_false:
        add_fifo(fifo, index)
    else:
        tmp = fifo[0]
        for i in range(0, len(fifo) - 1):
                fifo[i] = fifo[i+1]
        fifo[len(fifo) - 1] = tmp

    return (index, fifo)
mem_class = [{'ok': True, 'data': 0x44}, {'ok': False, 'data': 0xFF},
             {'ok': True, 'data': 0x22}, {'ok': True, 'data': 0x00}]
f = [2, 3, 0, None]
# print(replace_fifo(mem_class, f))

def update_lru(pile, valeur):
    l = []
    none_number = 0
    for x in pile:
        if x == None:
            none_number += 1
        elif x == valeur:
            pass
        else:
            l.append(x)
    l.append(valeur)
    for i in range(0, none_number):
        l.append(None)
    return l
p = [2, 3, 0, None]
# print(update_lru(p, 3))