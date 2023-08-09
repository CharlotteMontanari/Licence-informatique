#include "disjoint.h"

disjoint *ed;

disjoint representant(int s) {
    disjoint aux;
    aux = ed[s];
    while (aux != aux->route)
        aux = aux->route;
    return aux;
}

void reunion(disjoint u, disjoint v) {
    if (u->rang == v->rang)
        v->rang++;
    if (u->rang < v->rang)
        u->route = v;
    else
        v->route = u;
}

disjoint representant1(disjoint s) {
    if (s->route == s)
        return s;
    return s->route = representant1(s->route);
}

disjoint singleton(int s) {
    disjoint res;
    res = malloc(sizeof(enrdisjoint));
    res->s = s;
    res->route = res;
    res->rang = 0;
    return res;
}

void init_disjoint(int n) {
    ed = calloc(n, sizeof(disjoint));
    for (int i=0; i<n; i++) {
        ed[i] = singleton(i);
    }
}

void freeDisjoint(int n) {
    for (int i=0; i<n; i++)
        free(ed[i]);
    free(ed);
}