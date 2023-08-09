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

/*int main() {
    uint tab[7] = {6, 7, 5, 4, 9, 1, 3};
    uint a = 1, b = 2;
    Echange(tab, a, b);
    affiche(tab, 7);
}*/

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
    for (int el=0; el<n; el++)
        printf("%d | ", t[el]);
    printf("\n");
    return t;
}

/*int main() {
    GenPerm(10);
    return 0;
}//*/

uint IdxMin(uint *t, uint a, uint b) {
    int imin = a;
    while (a < b) {
        if (t[a] < t[imin])
            imin = a;
        a++;
    }
    return imin;
}

/*int main() {
    uint tab[7] = {6, 7, 5, 4, 9, 0, 3};
    uint a = 0, b = 6;
    //int *tab = (int*)malloc(sizeof(int));
    affiche(tab, 7);
    uint min = IdxMin(tab, a, b);
    printf("min: %d\n", min);
    return 0;
}*/

ullong TriSelection(uint *t, uint n) {
    int i = 0;
    int imin;
    while (i < n) {
        imin = IdxMin(t, i, n);
        Echange(t, i, imin);
        i++;
    }
    return *t;
}

/*int main() {
    uint tab[7] = {6, 7, 5, 4, 9, 2, 3};
    uint f = 7;
    TriSelection(tab, f);
    affiche(tab, f);
    return 0;
}*/

ullong Propager(uint *t, uint a, uint b, ullong *e) {
    ullong cpt = 0;
    if (a < b) {
        while (a < b) {
            if (t[a] > t[a+1]) {
                Echange(t, a, a+1);
                *e = *e + 1;
            }
            cpt++;
            a++;
        }
    }else {
        while (a > b) {
            if (t[a-1] > t[a]) {
                Echange(t, a-1, a);
                *e = *e + 1;
            }
            a--;
            cpt++;
        }
    }
    return cpt;
}

/*int main() {
    uint tab[7] = {6, 7, 5, 4, 9, 2, 3};
    uint f = 7;
    ullong e = 0;
    Propager(tab, 0, f, &e);
    affiche(tab, f);
    return 0;
}//*/

ullong TriBulles(uint *t, uint n, ullong *e) {
    uint bbol = true;
    while (bbol && (n > 0)) {
        bbol = Propager(t, 0, n, e);
        n--;
    }
    return *t;
}

/*int main() {
    uint tab[7] = {6, 7, 5, 4, 9, 2, 3};
    uint f = 7;
    ullong e = 0;
    TriBulles(tab, f, &e);
    affiche(tab, f);
    return 0;
}//*/

ullong TriCocktail(uint *t, uint n, ullong *e) {
    int bbol = 0;
    int i = 0;
    int d = n-1;
    while (i < d) {
        bbol += Propager(t, i, d, e);
        d--;
        if ((i < d)) {
            bbol += Propager(t, d, i, e);
            i++;
        }
    }
    return *t;
}

/*int main() {
    uint tab[7] = {6, 7, 5, 4, 9, 2, 3};
    uint f = 7;
    ullong e = 0;
    TriCocktail(tab, f, &e);
    affiche(tab, f);
    return 0;
}//*/

ullong TriPeigne(uint *t, uint n, float coef, ullong *e) {
    int bbool = true;
    int k = n;
    while ((k > 1) || bbool) {
        if (k/coef > 1)
            k = k/coef;
        else
            k = 1;
        bbool = false;
        int i = 0;
        while (i < n - k) {
            if (t[i] > t[i + k]) {
                Echange(t, i, i+k);
                *e = *e + 1;
                bbool = true;
            }
            i++;
        }
    }
    return *t;
}

/*int main() {
    uint tab[7] = {6, 7, 5, 4, 9, 2, 3};
    uint f = 7;
    ullong e = 0;
    TriPeigne(tab, f, 2.0, &e);
    affiche(tab, f);
    return 0;
}*/

ullong Inserer(uint *t, uint n) {
    while ((n > 0) && (t[n] < t[n-1])) {
        Echange(t, n, n-1);
        n--;
    }
    return *t;
}

ullong TriInsertion(uint *t, uint n) {
    int i = 0;
    while (i < n) {
        Inserer(t, i);
        i++;
    }
    return *t;
}

/*int main() {
    uint tab[7] = {6, 7, 5, 4, 9, 2, 3};
    uint f = 7;
    TriInsertion(tab, f);
    affiche(tab, f);
    return 0;
}//*/

