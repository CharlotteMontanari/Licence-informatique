#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <math.h>
#include <time.h>
#include <stdbool.h>

typedef unsigned int uint;
typedef unsigned long long ullong;

void Echange(uint *t, uint a, uint b) {
    uint temp = t[a];
    t[a] = t[b];
    t[b] = temp;
}

void affiche(uint *t, uint n) {
    for (int i=0; i<n; i++)
        printf("%d | ", t[i]);
    printf("\n");
}

void Tamiser(uint *t, uint ipere, uint n, ullong *e) {
    uint ifils = (2 * ipere)+1;
    if ((ifils < n-1) && (t[ifils+1] > t[ifils]))
        ifils++;
    if ((ifils <= n-1) && t[ipere] < t[ifils]) {
        Echange(t, ipere, ifils);
        Tamiser(t, ifils, n, e);
    }
    *e = *e + 1;
}

void Entasser(uint *t, uint n, ullong *e) {
    int i = n / 2;
    while (i >= 0) {
        Tamiser(t, i, n, e);
        i--;
    }
}

void TriTas(uint *t, uint n, ullong *e) {
    Entasser(t, n, e);
    int k = n-1;
    while (k > 0) {
        Echange(t, 0, k);
        Tamiser(t, 0, k, e);
        k--;
    }
}

uint *GenPerm(uint n) {
    uint *t = (uint*)malloc(sizeof(uint)*n);
    for (int el=0; el<=n; el++) 
        t[el] = el+1;
    int i = 0;
    srand(time(NULL));
    while (i < n) {
        int alea = rand()%((n - i) + i);
        Echange(t, alea, i);
        i++;
    }
    /*for (int el=0; el<n; el++)
        printf("%d | ", t[el]);
    printf("\n");*/
    return t;
}

int main() {
    uint tab[7] = {6, 7, 5, 4, 9, 2, 3};
    uint f = 7;
    ullong e = 0;
    //Tamiser(tab, 0, 6, e);
    //Entasser(tab, f, e);
    //TriTas(tab, f, e);
    //affiche(tab, f);
    FILE *fichier= fopen("gnu.txt","w");
    for(int i=0; i<100; i++) {
        e = 0;
        TriTas(GenPerm(i), i, &e);
        fprintf(fichier,"%d\t%llu\n", i, e);
    }
    return 0;
}