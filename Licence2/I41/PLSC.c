#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

// En cas d'erreur sur les arguments
#define ERREUR_NBARGS 1

// Macro max
#define max(a,b) ( ((a) > (b)) ? (a) : (b) )

// Entiers non signés
typedef unsigned char uchar;
typedef unsigned int uint;

// Structure de chaîne de caractères
typedef char *tmot;

///////////////////////////////////////////////////////////////
// À COMPLÉTER - À COMPLÉTER - À COMPLÉTER - À COMPLÉTER 
// Renvoie la longueur du <mot> (chaine qui finit par '\0')
///////////////////////////////////////////////////////////////
uint len(tmot mot) {
    uint somme = 0; //je cree une variable pour stocker la somme des lettres
    int i = 0;
    while (mot[i] != '\0') { //tant que je n'atteins pas la fin du mot (\0) j'incremente i
        somme++;
        i++;
    }
    return somme;
}

/*int main() {
    tmot m = "coucou";
    uint a = len(m);
    printf("%d\n", a);
    return 0;
}*/

///////////////////////////////////////////////////////////////
// À COMPLÉTER - À COMPLÉTER - À COMPLÉTER - À COMPLÉTER 
// Renvoie VRAI (1) si u est un préfixe de v et FAUX (0) sinon.
///////////////////////////////////////////////////////////////
uchar EstPrefixe(tmot u, tmot v) {
    int vrai = 1;
    int faux = 0;
    int i = 0;
    int j = 0;
    if (strlen(u) < strlen(v)) //si le prefixe est superieur au mot, on renvoie 0
        return printf("%d\n", faux);
    else {
        while ((i < strlen(u)) && (j < strlen(v))) { //tant que que le prefixe est inferieur au mot, on test
            if (u[i] != v[j]) //on test chaque s'il sont differents, si oui, on renvoie 0
                return printf("%d\n", faux);
            i++;
            j++;
        } 
    }
    return printf("%d\n", vrai); //sinon, c'est bien un prefixe du mot
}

/*int main() {
    tmot a = "bonjour";
    tmot b = "bond";
    EstPrefixe(a, b);
    return 0;
}*/

///////////////////////////////////////////////////////////////
// À COMPLÉTER - À COMPLÉTER - À COMPLÉTER - À COMPLÉTER 
// Renvoie VRAI (1) si u est une ss-séq. de v et FAUX (0) sinon.
///////////////////////////////////////////////////////////////
uchar EstSousSeq(tmot u, tmot v) {
    int vrai = 1;
    int faux = 0;
    int somme = 0;
    int long_u = strlen(u);
    int long_v = strlen(v);
    int i = 0;
    int j = 0;
    if (long_u > long_v)
        return printf("%d\n", faux);
    else {
        while (j < long_v) { //je fais une boucle sur le mot le plus long
        if (u[i] == v[j]) { //je test si la lettre de u est dans v
            somme++; //si oui, j'augmente ma somme
            i++; //et je passe a la lettre de u suivante
        }
        j++;
        }
        if (somme == long_u) //si ma somme est egale a la longueur de u, u est une sous sequence
            return printf("%d\n", vrai);
        else
            return printf("%d\n", faux); //sinon, ce n'en est pas une
    }
}

/*int main() {
    tmot a = "babc";
    tmot b = "abcabac";
    EstSousSeq(a, b);
    return 0;
}*/

///////////////////////////////////////////////////////////////
// Affiche la table L des Longueurs de PLSC
///////////////////////////////////////////////////////////////
void AfficherTable(uint **L, tmot u, tmot v) {
    uint i,j;
    uint n = len(u);
    uint m = len(v);

    printf("     ");
    for (i = 0; i < m + 1; i++)
        printf("%3c",v[i]);
    printf("\n");  
    for (i = 0; i < n + 1; i++) {
        if (i > 0) 
            printf("%2c",u[i - 1]);
        else printf("  ");
        for (j = 0; j < m + 1; j++) {
            if ((i > 0) && (j > 0) && (u[i - 1] == v[j - 1]))
                printf("%3u",L[i][j]);	  
            else
                printf("%3u",L[i][j]);	  
        }
        printf("\n");
    }   
}


///////////////////////////////////////////////////////////////
// À COMPLÉTER - À COMPLÉTER - À COMPLÉTER - À COMPLÉTER 
// Construit et renvoie la table L des longueurs des PLSC
// de deux mots u et v.
///////////////////////////////////////////////////////////////
uint **LPLSC(tmot u, tmot v) {
    uint i = 0;
    uint j = 0;
    uint **tab = (uint**)malloc(sizeof(uint*)); //je cree un tableau 2 dimentions
    while (i < strlen(u)) {
        while (j < strlen(v)) {
            tab[j] = malloc(sizeof(uint)); //j'alloue pour les sous "listes"
            j++;
        }
        i++;
    }
    return tab;
}

/*int main() {
    tmot a = "algorithme";
    tmot b = "larme";
    uint **l = LPLSC(a, b);
    AfficherTable(l, a, b);
    return 0;
}*/

///////////////////////////////////////////////////////////////
// À COMPLÉTER - À COMPLÉTER - À COMPLÉTER - À COMPLÉTER 
// Renvoie une PLSC des mots u et v.
///////////////////////////////////////////////////////////////
//tmot PLSC(tmot u, tmot v) {}


/*int main(int argc, tmot argv[])
{
    if (argc < 2) {
        printf("Syntaxe: %s mot1 mot2\n",argv[0]);
        return ERREUR_NBARGS;
    }

    tmot u = argv[1];
    tmot v = argv[2];

    uint **L = LPLSC(u,v);  
    AfficherTable(L,u,v);

    printf("%s",PLSC(u,v));
    return 0;
}//*/