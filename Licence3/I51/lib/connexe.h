#ifndef CONNEXE_H
#define CONNEXE_H

#include "graphe.h"
#include "acm.h"
typedef int sommet;

int ComposanteConnexe(graphe g);
void ParcoursProfondeurRecursif(int s, graphe g, uchar* clr);//g peut etre transmis par pointeur pour etre moins lourd plus tards
void PPR2(sommet s,graphe g);
void PPR3(int s, graphe g, int* cpt);
void PPR4(int s, int* index, graphe g, int* cpt);
void empiler(int s, liste* l);
int depiler(liste* p);
int* tournee(graphe* g, int s);
void afficher_tournee(int* tournee, graphe g);
void dessiner_tournee (char* nom, points* nuage_point, graphe g, int* res_tournee);
#endif
