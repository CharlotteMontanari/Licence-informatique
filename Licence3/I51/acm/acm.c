#include "acm.h"
#include "../disjoint/disjoint.h"

points *nuage(int n) {
    points *res;
    //srand(time(NULL));
    res = calloc(n, sizeof(points));
    for (int i=0; i<n; i++) {
        res[i].x = ((rand() - RAND_MAX/2)) / (RAND_MAX/2);
        res[i].y = ((rand() - RAND_MAX/2)) / (RAND_MAX/2);
    }
    return res;
}

graphe acm(points *pt, int n) {
    graphe res = creergraphe(n);
    arrete *a = calloc(n*(n-1)/2, sizeof(arrete));
    int i, j, k = 0;
    for (i=0; i<n; i++) {
        for (j=i+1; j<n; j++) {
            a[k].i = i;
            a[k].j = j;
            //a[k].w = sqrt((pt[i].x - pt[j].x) * (pt[i].x - pt[j].x) + (pt[i].y - pt[j].y) * (pt[i].y - pt[j].y));
            a[k].w = i+j;
            k++;
        }  
    }
    qsort(a, k, sizeof(arrete), compare);
    int p = n;
    init_disjoint(p);
    k = 0;
    while (p > 1) {
        int i = a[k].i;
        int j = a[k].j;
        disjoint ri = representant(i);
        disjoint rj = representant(j);
        if (ri != rj) {
            res.mat[i][j] = 1;
            res.mat[j][i] = 1;
            p--;
            reunion(ri, rj);
        }
        k++;
    }
    return res;
}

int compare(const void *p1, const void *p2) {
    float x = ((arrete*)p1) -> w;
    float y = ((arrete*)p2) -> w;
    if (x < y)  
        return -1;
    if (x > y)  
        return 1;
    return 0;
}

