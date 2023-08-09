#include <stdio.h>
#include <stdlib.h>
#include "graphe.h"

graphe LireGraphe(char *nom) {
	graphe res;
	char ligne[1024];
	int n, i, j;
	FILE *source;
	source = fopen(nom, "r");
	if (source == NULL) {
		perror("Lire graphe");
		exit(1);
	}
	while (!feof(source)) {
		fgets(ligne, 1024, source);
		switch(ligne[0]) {
			case 'n':
				if (sscanf(ligne, "nbs = %d", &n))
					res = creergraphe(n);
				break;
			default:
				if (sscanf(ligne, "%d %d", &i, &j))
					res.mat[i][j] = res.mat[j][i] = 1;
		}
	}
	fclose(source);
	return res;
}

void dessiner(char *nom, graphe g) {
	FILE *dst;
	char name[20];
	char cmd[128];
	sprintf(name, "/tmp/%s.dat", nom);
	dst = fopen(name, "w");
	fprintf(dst, "graph %s {\n", nom);
	for (int i=0; i<g.nbs; i++) {
		for (int j=i+1; j<g.nbs; j++) {
			if (g.mat[i][j])
				fprintf(dst, "%d--%d;\n", i, j);
		}
	}
	fputs("}", dst);
	fclose(dst);
	sprintf(cmd, "dot -Tpng %s -o %s.png", name, nom);
	system(cmd);
}
