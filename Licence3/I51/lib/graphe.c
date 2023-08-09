#include "graphe.h"
#include <stdlib.h>

typedef unsigned char uchar;
typedef unsigned int uint;

graphe creergraphe(int n ) {
	graphe res;
	res.nbs = n;
	res.mat = calloc(n, sizeof(uchar*));
	for (int i=0; i<n; i++)
		res.mat[i] = calloc(n, sizeof(uchar));
	return res;
}

graphe randomgraphe(int n, float p) {
	graphe g = creergraphe(n);
	int seuil;
	float prob = ((p+1)/(n-1));
	seuil = prob * RAND_MAX;
	for (uint i=0; i<n; i++) {
		for (uint j=i+1; j<n; j++) {
			if (rand() < seuil) {
				g.mat[i][j] = 1;
				g.mat[j][i] = 1;
			}
		}
	}
	return g;
}