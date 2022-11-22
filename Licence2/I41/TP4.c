#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

typedef unsigned long long ullong;
typedef unsigned int uint;

typedef struct tmat {
    ullong f1;
    ullong f2;
    ullong f3;
    ullong f4;
}tmat;

tmat produit(tmat a, tmat b) {
    tmat result;
    result.f1 = a.f1*b.f1 + a.f2*b.f3;
    result.f2 = a.f1*b.f2 + a.f2*b.f4;
    result.f3 = a.f3*b.f1 + a.f4*b.f2;
    result.f4 = a.f3*b.f2 + a.f4*b.f4;
    return result;
}

tmat puissance(tmat m, int n) {
    int i = 1;
    tmat nbre;
    nbre.f1 = 1; nbre.f2 = 0;
    nbre.f3 = 0; nbre.f4 = 1;
    for (int i=0; i<n; i++)
        nbre = produit(nbre, m);
    return nbre;
    }

/*int main() {
    int a = 2, b = 6;
    tmat c = puissance(2, 6);
    printf("%d^%d = %llu\n", a, b, c);
}*/

typedef struct binaire {
    int *bin;
    int taille;
} binaire;

binaire binary(int n) {
    binaire b;
    b.taille = ((int)log2(n) + 1);
    b.bin = malloc(sizeof(int)*b.taille);
    int i = 0;
    while (n != 0) {
        b.bin[i] = n % 2;
        n = (int)n / 2;
        printf("%d", b.bin[i]);
        i++;
    }
    return b;
}

/*int main() {
    binary(7);
    printf("\n");
}*/

tmat SM(tmat m, int n) {
    tmat r;
    r.f1 = 1; r.f2 = 0;
    r.f3 = 0; r.f4 = 1;
    binaire b = binary(n);
    int i = b.taille - 1;
    while (i > 0) {
        r = produit(r, r);
        if (b.bin[i] == 1)
            r = produit(r, m);
        i = i - 1;
    }
    return r;
}

/*int main() {
    tmat matrice;
    matrice.f1 = 1; matrice.f2 = 0;
    matrice.f3 = 0; matrice.f4 = 1;
    tmat a = SM(matrice, 6);
    printf("%d\n", a);
}*/

