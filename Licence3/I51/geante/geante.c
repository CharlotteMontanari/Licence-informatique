#include "geante.h"
#include "graphe.h"
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int *clr = NULL;

void ppr2(int s, graphe g, int *cpt) {
    int t;
    clr[s] = 1;
    *cpt = *cpt + 1;
    for (t=0; t<g.nbs; t++) {
        if (g.mat[s][t] && clr[t] == 0)
            ppr2(t, g, cpt);
    }
}

int geante(graphe g) {
    int max = 0, s, cpt = 0;
    clr = calloc(g.nbs, sizeof(uchar));
    for (s=0; s<g.nbs; s++) {
        if (clr[0] == 0) {
            cpt = 0;
            ppr2(s, g, &cpt);
        }
        if (cpt > max)
            max = cpt;
    }
    free(clr);
    return max;
}

int composanteGeante(graphe g) {
    int taille;
    int s;
    int max = 0;
    clr = calloc(g.nbs, sizeof(uchar));
    for (s=0; s<g.nbs; s++) {
        if (clr[s] == 0) {
            taille = 0;
            ppr2(s, g, &taille);
            max = max > taille ? max : taille;
        }
    }
    free(clr);
    return max;
}

int main(int argc, char **argv) {
    /*int x = 10;
    float y = 1;
    graphe a = randomgraphe(x, y);
    dessiner("graphe", a);*/
    graphe g;
    g = randomgraphe(atoi(argv[2]), atof(argv[1]));
    float taille = log(composanteGeante(g));
    printf("%d %f\n", atoi(argv[2]), taille);
    return 0;
}