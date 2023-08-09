#ifndef ACM_H
#define ACM_H
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#include "../lib/graphe.h"

typedef struct pts {
    float x;
    float y;
} points;

typedef struct arrete {
    int i;
    int j;
    float w;
} arrete;

points *nuage(int);
graphe acm(points*, int);
int compare(const void*, const void*);

#endif