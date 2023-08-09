from itertools import chain
import random

#Pour écrire une ligne dans un fichier : destination.write(ligne), 
#ligne étant une chaine de caractères.

def vigenere_chiffre(f_in, f_out, cle):
    source = open(f_in, "r")
    destination = open(f_out, "w")
    n = len(cle)
    mod = 26
    dico = {'a':'a', 'b':'b', 'c':'c', 'd':'d', 'e':'e', 'f':'f', 'g':'g', 'h':'h',
            'i':'i', 'j':'j', 'k':'k', 'l':'l', 'm':'m', 'n':'n', 'o':'o', 'p':'p',
            'q':'q', 'r':'r', 's':'s', 't':'t', 'u':'u', 'v':'v', 'w':'w', 'x':'x',
            'y':'y', 'z':'z', 'â':'a','ä':'a', 'à':'a', 'ç':'c', 'é':'e', 'è':'e', 
            'ê':'e', 'ë':'e', 'î':'i', 'ï':'i', 'ì':'i', 'ô':'o', 'ù':'u', 'û':'u'} 
    i = 0
    for ligne in source:
        for lettre in ligne:
            if lettre.lower() in dico:
                l = ord(dico[lettre.lower()]) - 97
                c = ord(cle[i]) - 97
                destination.write(chr(((l+c) % mod) + 97))
                i = (i + 1) % n
            if lettre == '\n':
                destination.write('\n')
    source.close()
    destination.close()
#print(vigenere_chiffre('clair_vigenere.txt', 'chiffre_vigenere.txt', 'pivot'))

def vigenere_dechiffre(f_in, f_out, cle):
    source = open(f_in, "r")
    destination = open(f_out, "w")
    n = len(cle)
    mod = 26
    i = 0
    for ligne in source:
        for lettre in ligne[:-1]:
            l = ord(lettre) -  97
            d = ord(cle[i]) - 97
            destination.write(chr(((l-d) % mod) + 97))
            i = (i + 1) % n
        destination.write('\n')
    source.close()
    destination.close()
#print(vigenere_dechiffre('chiffre_vigenere.txt', 'dechiffre_vigenere.txt', 'pivot'))

def longueur_vigenere(f_in):
    dico = {}
    source = open(f_in, "r")
    i = 0
    triplet_max = 0
    chaines = ''
    for ligne in source:
        lettre = 0
        while lettre < len(ligne):
            triplet = ligne[lettre:lettre+3]
            if triplet not in dico:
                dico[triplet] = 1
            else:
                dico[triplet] += 1
            if dico[triplet] > triplet_max and triplet != '\n':
                triplet_max = dico[triplet]
                chaine = triplet
            lettre += 1
    return chaine, triplet_max
#print(longueur_vigenere('longueur_cle.txt'))
