#f = open('texte1')
#print(f.read(12))

#f = open('texte1')
#print(f.readline())
#f.readline()
#print(f.readline())

#f = open('texte1')
#g = f.readlines()
#print(g[1])
#print(g[3])

#f = open('texte1')
#print(f.readline())
#print(f.readline())
#print(f.readline())
#f.seek(0)
#print(f.read(3))

#afficher du 11 au 15 eme caractere
#afficher 3eme ligne entiere
#afficher dans la ligne 2: 10 premiers caracteres
#afficher toute la ligne 1
#f = open('texte1')
#f.seek(11)
#print(f.read(4))
#f.seek(0)
#f.readline()
#f.readline()
#print(f.readline())
#f.seek(0)
#f.readline()
#print(f.read(10))
#f.seek(0)
#print(f.readline())

#f = open('fichier_test', 'w')
#f.write('La cigale et la fourmi')

#f = open('fichier_test', 'a')
#f.write('\n')
#f.write('Le scorpion et la grenouille')

#f = open('valeurs')
#print(f.read(4))
#cela ne marche car cest un fichier binaire

#f = open('fichier_bis', 'w')
#f.write('1337, -2, 10.25')
#od -t c fichier_bis

import struct

# Conversion byte vers str
#chaine.decode('UTF-8')
#print(chaine)
# Conversion str vers byte
#chaine.encode('UTF-8')

# Conversion byte vers un nombre
#nbre = struct.unpack('<b', octet)[0]
# Conversion nombre vers byte
#octet = struct.pack('<b', nbre)

#f = open('valeurs', 'rb')
#octet = f.read(1)
#nbre = struct.unpack('<B', octet)[0]
#print(nbre)
#192 sur 8bits

#octet = f.read(1)
#nbre = struct.unpack('<b', octet)[0]
#print(nbre)
#-1 sur 8bits

#octet = f.read(2)
#nbre = struct.unpack('<bb', octet)[0]
#print(nbre)
#-2 sur 16bits

#octet = f.read(4)
#nbre = struct.unpack('>I', octet)[0]
#print(nbre)
#1633837924 sur 32bits

#octet = f.read(4)
#nbre = struct.unpack('<f', octet)[0]
#print(nbre)
#1.0 sur 32bits

#octet = f.read(8)
#nbre = struct.unpack('<d', octet)[0]
#print(nbre)
#-10.25 sur 64bits

#f = open('fichier_bin', 'wb')
#nbre = 1337
#octet = struct.pack('<H', nbre)
#f.write(octet)

#nbre = -2
#octet = struct.pack('<i', nbre)
#f.write(octet)

#nbre = 10.25
#octet = struct.pack('<f', nbre)
#f.write(octet)


#f = open('fichier_bin', 'rb')
#octet = f.read(2)
#nbre = struct.unpack('<h', octet)[0]
#print(nbre)

#octet = f.read(4)
#nbre = struct.unpack('<i', octet)[0]
#print(nbre)

#octet = f.read(4)
#nbre = struct.unpack('<f', octet)[0]
#print(nbre)


#def majuscule(ch):
#    chaine = ''
#    for i in ch:
#        new_ch = chr(ord(i) - 32)
#        chaine += new_ch
#    return chaine
#print(majuscule('coucou'))


#def val2ascii(entier):
#	liste = []
#	char = ''
#	cle = 48
#	quotient = entier
#	while quotient != 0:
#		reste = quotient % 10
#		quotient = quotient // 10
#		liste.insert(0, reste + cle)
#	for el in liste:
#		char += chr(el)
#	return char	
#v = val2ascii(115)		
#print(type(v), v)