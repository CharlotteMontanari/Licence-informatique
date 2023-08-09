#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

enum tbool{False, True};

typedef enum tbool tbool;

tbool EstPalindrome(char *phrase) {
    int debut = 0;
    int fin = strlen(phrase)-1;
    while (debut < fin) {
        while (phrase[debut] == ' ')
            debut += 1;
        while (phrase[fin] == ' ')
            fin -= 1;
        if (toupper(phrase[debut]) != toupper(phrase[fin])) 
            return False;
        debut += 1;
        fin -= 1;
    }
    return True;
}

/*int main(int argc, char ** argv) {
    char chaine[100] = "";
    int i = 1;
    while (i < argc) {
        strcat(chaine, argv[i]);
        i++;
    }
    int a = EstPalindrome(chaine);
    printf("%d\n", a);
    return 0;
}*/

#define uint unsigned short

void echanger(int *liste, int i, int imin) {
    int aux;
    aux = liste[i];
    liste[i] = liste[imin];
    liste[imin] = aux;
}

int IdxMin(int *liste, int i, uint n) {
    int imin = i;
    while (i < n) {
        if (liste[i] < liste[imin])
            imin = i;
        i += 1;
    }
    return imin;
}

void TriSelection(int *liste, uint n) {
    int i = 0;
    int imin;
    while (i < n) {
        imin = IdxMin(liste, i, n);
        echanger(liste, i, imin);
        i += 1;
    }
}

/*int main() {
    int i = 0;
    const int n = 7;
    int liste[n] = {3,5,2,1,7,4,6};
    //int a = IdxMin(liste, 4, 7);
    //printf("%d", a);
    TriSelection(liste, n);
    printf("[");
    while (i < n) {
        printf("%d, ", liste[i]);
        i += 1;
    }
    printf("]\n");
    return 0;
}*/

uint PairOuImpair(uint n) {
    if (n % 2 == 0)
        n = n / 2;
        //printf("n/2\n");
    else
        n = 3*n + 1;
        //printf("3n+1\n");
    return 0;
}

/*int main() {
    PairOuImpair(12);
}*/

uint syracuse(uint u0) {
    int nbre = 1;
    while (u0 != 1) {
        if (u0 % 2 == 0) {
            u0 = u0 / 2;
            nbre += 1;
        }
        else {
            u0 = 3*u0+1;
            nbre += 1;
        }
    }
    return nbre;
}

/*int main() {
    int a = syracuse(12);
    printf("u%d = 1\n", a);
}*/

