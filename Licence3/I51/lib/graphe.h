#ifndef GRAPHE_H
#define GRAPHE_H

typedef unsigned char uchar;

typedef struct {
	int nbs;
	uchar **mat;
	int* clr;
	int* tour;
	liste* adj;
} graphe;


typedef struct liste{
	int val;
	struct liste* suivant;
} enrliste, *liste;


graphe creergraphe(int);
graphe randomgraphe(int, float);
graphe LireGraphe(char *);
void dessiner(char *, graphe);

#endif