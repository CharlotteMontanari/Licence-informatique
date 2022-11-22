#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <math.h>
#include <time.h>
#include <stdbool.h>

typedef unsigned int uint;
typedef unsigned long long ullong;
typedef enum {False = 0, True = 1} tbool;

// TRI FUSION

typedef struct tliste {
    uint n;
    uint *valeurs;
}tliste;

void Echange(tliste t, uint a, uint b) {
    uint temp = t.valeurs[a];
    t.valeurs[a] = t.valeurs[b];
    t.valeurs[b] = temp;
}

void affiche(uint *t, uint n) {
    for (int i=0; i<n; i++)
        printf("%d | ", t[i]);
    printf("\n");
}

void copier(tliste x, uint i, tliste y, uint j, uint n) {
    int k = 0;
    while (((i+k) < x.n) && ((j+k) < y.n) && (k < n)) {
        y.valeurs[j+k] = x.valeurs[i+k];
        k++;
    }
}

/*int main() {
    int valeurs[5] = {1,2,3,4,5};
    tliste X = {5, valeurs};
    int valeur[5] = {6,7,8,9,10};
    tliste Y = {5, valeur};
    copier(X, 1, Y, 2, 3);
    affiche(X.valeurs, 5);
    affiche(Y.valeurs, 5);
    return 0;
}*/

void Fusionner(tliste L, uint p, uint q, uint r) {
    tliste G = {q - p + 1, malloc(sizeof(int)*(q - p + 1))};
    tliste D = {r - q, malloc(sizeof(int)*(r - q))};
    int ng = q - p + 1;
    int nd = r - q;
    copier(L, p, G, 0, ng);
    copier(L, q+1, D, 0, nd);
    int i = 0;
    int j = 0;
    int k = p;
    while ((i < ng) && (j < nd)) {
        if (G.valeurs[i] < D.valeurs[j]) {
            L.valeurs[k] = G.valeurs[i];
            i++;
        }
        else {
            L.valeurs[k] = D.valeurs[j];
            j++;
        }
        k++;
    }
    copier(G, i, L, k, ng - i);
}

void TriFusion(tliste L, uint p, uint r) {
    if (p < r) {
        int q = (p + r) / 2;
        TriFusion(L, p, q);
        TriFusion(L, q+1, r);
        Fusionner(L, p, q, r);
    }
}

/*int main() {
    uint valeurs[9] = {1,4,7,3,8,9,5,6,2};
    tliste X = {9, valeurs};
    //Fusionner(X, 0, 4, 9);
    TriFusion(X, 0, 8);
    affiche(X.valeurs, 9);
    return 0;
}*/

// TRI RAPIDE

void reculer(tliste L, uint x, int *j) {
    *j = *j - 1;
    while ((L.valeurs[*j] > x) && (*j >= 0))
        (*j)--;
}

void avancer(tliste L, uint x, int *i) {
    *i = *i + 1;
    while ((L.valeurs[*i] < x) && (*i < L.n))
        (*i)++;
}

uint Partitionner(tliste L, uint p, uint r) {
    int x = L.valeurs[p];
    int i = p;
    int j = r;
    while (L.valeurs[j] > x)
        j--;
    while (i < j) {
        Echange(L, i, j);
        reculer(L, x, &j);
        avancer(L, x, &i);
    }
    return j;
}

void TriRapide(tliste L, uint p, uint r) {
    if (p < r) {
        int q = Partitionner(L, p, r);
        TriRapide(L, p, q);
        TriRapide(L, q+1, r);
    }
}

tbool EstTrie(tliste L) {
    int i = 0;
    int flag = True;
    while (L.valeurs[i] < L.n) {
        if (L.valeurs[i] > L.valeurs[i+1])
            return False;
        i++;
    }
    return True;
}

int main() {
    uint valeurs[9] = {2,1,2,3,4,5,6,7,8};
    tliste X = {9, valeurs};
    //int a = Partitionner(X, 0, 8);
    //printf("%d\n", a);
    //TriRapide(X, 0, 8);
    //affiche(X.valeurs, 9);
    tbool a = EstTrie(X);
    printf("%d\n", a);
    return 0;
}