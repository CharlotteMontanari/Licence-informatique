#include "acm.h"
#include "../lib/graphe.h"

int main() {
    points *pt = calloc(25, sizeof(points));
    int cpt = 0;
    for (int i=0; i<5; i++) {
        for (int j=0; j<5; j++) {
            pt[cpt].x = i;
            pt[cpt].y = j;
            cpt++;
        }
    }
    graphe g = acm(pt, 25);
    dessiner("coucou", g);
}