#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>
#include <math.h>
#include "lib/graphe.h"

int soluce = 0;

void traitement(int p, int *t, int n) {
    for (int i=0; i<n; i++)
        printf("%d\n", t[i]);
}

void partition(int p, int s, int t[], int n) {
    if (s == 0) {
        soluce++;
        traitement(p, t, n);
        return;
    }
    if (s < p)
        return;
    int q = s/p;
    for (int i=0; i <= q; i++) {
        t[p] = i;
        partition(p+1, s-i*p, t, n);
    }
    t[p] = 0;
}

int clique_maximal(graphe g) {
    int *clique = calloc(g.nbs+1, sizeof(int));
    int ans = 0;
    int s = 1;
    int appart;
    if (g.nbs > 0) {
        unsigned int *perm = GenPerm(g.nbs);
            clique[0] = perm[0];
        ans = 1;
        clique[s] = -1;
        appart = 1;
        int i;
        int j;
        for (i=1; i<g.nbs; i++) {
            j = 0;
            appart = 1;
            for (j=0; ((appart == 1) && (clique[j] != -1)) ; j++) {
                if (g.mat[clique[j]][perm[i]] != 1)
                    appart = 0;
            }
            if (appart == 1) {
                clique[s++] = perm[i];
                clique[s] = -1;
                ans++;
            }
        }
    }
    return ans;
}

unsigned int *GenPerm(unsigned int n) {
    unsigned int aux;
    unsigned int e;
    srand(time(NULL));
    unsigned int *ans = (unsigned int *)malloc(sizeof(unsigned int) * n);
    for (unsigned int i=0; i<n; i++) {
        ans[i] = i;   
    }
    for (unsigned int j=0; j<n; j++) {
        e = (rand() % n-j) + j;
        aux = ans[e];
        ans[e] = ans[j];
        ans[j] = aux;
    }
    for (unsigned int j=0; j<n; j++)
        printf("%d -> %d\n", j, ans[j]);
    return ans;
}

int main() {
    int n = 6;
    int *tab = calloc(n, sizeof(int));
    partition(1, n, tab, n);
    printf("%d\n", soluce);
    return 0;
}
