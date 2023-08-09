#include "graphe.h"

int hamiltonien(graphe g) {
    int soluce = 0;
    int visite[0] = 1;
    int *l = calloc(g.nbs, sizeof(int));
    parcours(0, 1, g, l);
    free(l);
    return soluce;
}

void parcours(int s, int p, graphe g, int visite[]) {
    if (p == g.nbs) {
        if (g.mat[s][0])
            soluce++;
        return;
    }
    for (int t=0; t< g.nbs; t++) {
        if (!visite[t] && g.mat[s][t]) {
            visite[t] = 1;
            parcours(t, p+1, g, visite);
            visite[t] = 0;
        }
    }
}