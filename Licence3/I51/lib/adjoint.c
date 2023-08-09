#include "graphe.h"

graphe adjoint(graphe a){
    int **paire = calloc((a.nbs * a.nbs) / 2, sizeof(int*));
    int nbs = 0;
    for (int i=0; i<a.nbs; i++) {
        for (int j=i+1; j<a.nbs; j++) {
            if (a.mat[i][j]) {
                paire[nbs] = calloc(2, sizeof(int));
                paire[nbs][0] = i;
                paire[nbs][1] = j;
                nbs++;
            }
        }
    }
    graphe adj_a = creergraphe(nbs);
    for (int i=0; i<nbs; i++) {
        for (int j=i+1; j<nbs; j++) {
            if (paire[i][0] == paire[j][0])
                adj_a.mat[i][j] = adj_a.mat[j][i] = 1;
            if (paire[i][0] == paire[j][1])
                adj_a.mat[i][j] = adj_a.mat[j][i] = 1;
            if (paire[i][1] == paire[j][0])
                adj_a.mat[i][j] = adj_a.mat[j][i] = 1;
            if (paire[i][1] == paire[j][1])
                adj_a.mat[i][j] = adj_a.mat[j][i] = 1;
        }
    }
    free(paire);
    return adj_a;
}