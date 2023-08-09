#ifndef GEANTE_H
#define GEANTE_H

#include "graphe.h"

typedef unsigned char uchar;
//typedef uchar *clr;

typedef struct {
    int sommet;
    int taille;
} info;

typedef struct paires {
    int sommet;
    int taille;
    struct paire *suivant;
} emrpaire, *lpaire;

void ppr2(int, graphe, int *);
int geante(graphe);

#endif