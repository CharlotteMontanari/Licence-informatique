#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

typedef unsigned int uint;
typedef unsigned long long ullong;
typedef unsigned char uchar;

typedef struct {
  uint nbc;
  uint *chiffres;
}tnombre;

tnombre I2N(int n, uint base) {
    int taille = (log(n) / log(base)) + 1;
    tnombre convertit;
    convertit.nbc = taille;
    convertit.chiffres = malloc(sizeof(uint)*taille);
    int i = 0;
    while (n != 0) {
        convertit.chiffres[i] = n % base;
        n = n / base;
        i++; 
    }
    return convertit;
}

/*int main() {
    tnombre a = I2N(100, 16);
    printf("%u\n", a.nbc);
    for (int i=0; i<a.nbc; i++)
        printf("%u", a.chiffres[i]);
        printf("\n");
    return 0;
}*/

ullong Factorielle(uchar n) {
    ullong i = 1;
    for (int x=0; x<n; x++) {
        i = i * (x+1);
    }
    return i;
}

/*int main() {
    ullong a = Factorielle(6);
    printf("%llu\n", a);
    return 0;
}*/

tnombre S2N(char *chaine) {
    int t = atoi(chaine);
    return I2N(t, 10);
}

/*int main() {
    tnombre a = S2N("320154");
    for (int i=0; i<a.nbc; i++){
        printf("%u", a.chiffres[i]);
        printf("\n");}
    return 0;
}*/

char *N2S(tnombre N) {
    char *chaine = (char*)malloc(sizeof(char)*N.nbc);
    int i = N.nbc - 1;
    int j = 0;
    while (i >= 0) {
        chaine[j] = N.chiffres[i]+48;
        i--;
        j++;
    }
    return chaine;
}

/*int main() {
}*/

tnombre Addition(tnombre A, tnombre B, uint base) {
    int i = 0;
    if (B.nbc > A.nbc) {
        int aux = A;
        A = B;
        B = aux;
    }
    
}