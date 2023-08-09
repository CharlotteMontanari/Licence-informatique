#ifndef DISJOINT_H
#define DISJOINT_H
#include <stdio.h>
#include <stdlib.h>

typedef struct disjoint {
    int s;
    int rang;
    struct disjoint *route;
} enrdisjoint, *disjoint;

disjoint representant(int);
void reunion(disjoint, disjoint);
disjoint representant1(disjoint);
void init_disjoint(int);
void freeDisjoint(int);

#endif