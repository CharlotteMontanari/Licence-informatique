#include <stdio.h>
#include "connexe.h"

#define BLANC 0
#define NOIR 1

uchar* clr;

int ComposanteConnexe(graphe g){
	int p=0;
	sommet s;
	clr = calloc (g.nbs, sizeof(uchar));
	for (s=0; s<g.nbs; s++){
		if (clr[s] == 0){
			ParcoursProfondeurRecursif(s, g, clr);
			p = p+1;
		}
	}
	free(clr);
	return p;
}

void ParcoursProfondeurRecursif(int s, graphe g, uchar* clr){
	int t;
	clr[s] = NOIR;
	for (t=0; t<g.nbs; t++){
		if(g.mat[s][t] && (clr[t] == BLANC)){
			ParcoursProfondeurRecursif(t,g,clr);
		}
	}
	}

void PPR2(sommet s, graphe g){
	liste pile=NULL;
	liste aux;
	sommet t;
	empiler(s,&pile);
	clr[s]=NOIR;
	int cpt=1;
	int cpt_max=0;
	while (pile){
		s=depiler(&pile);
		aux=g.adj[s];
		while(aux){
			t=aux->val;
			if(g.clr[t]==BLANC){
			empiler(t,&pile);
			cpt=cpt+1;
			g.clr[t]=NOIR;
			}
			aux=aux->suivant;
		}
		if (cpt>cpt_max){
			cpt_max=cpt;
			//cpt_s=s;
		}
		cpt=0;
	}
}

void PPR3(int s, graphe g, int* cpt){
	int t;
	clr[s]=NOIR;
	*cpt = *cpt + 1;
	for (t=0; t<g.nbs; t++){
		if (g.mat[s][t] && clr[t]==0){
			PPR3(t, g, cpt);
		}
	}
}

void PPR4(int s, int* index, graphe g, int* res){ //pour avoir l'index du sommet
	int t;
	clr[s]=NOIR;
	res[*index] = s;
	*index = *index + 1;
	for (t=0; t<g.nbs; t++){
		if (g.mat[s][t] && clr[t]==0){
			PPR4(t, index, g, res);
		}
	}
}

void empiler(int s, liste *l){
	liste aux;
	aux=malloc(sizeof(enrliste));
	aux->suivant=*l;
	aux->val=s;
	*l=aux;
}

int depiler(liste* p){
	liste aux;
	aux=*p;
	int res=aux->val;
	*p=aux->suivant;
	free(aux);
	return res;
}

int* tournee(graphe* g, int s){
	int index = 0;
	int * res = calloc(g->nbs,sizeof(int));
	int * clr = calloc(g->nbs, sizeof(int));
	g->clr = clr;
	PPR4(s,&index,*g,res);
	g->tour = res;
	return res;
}

void afficher_tournee(int* tournee, graphe g){
	printf("%d",tournee[0]);
	for (int i=1; i<g.nbs; i++)
		printf("--%d",tournee[i] );

}

void dessiner_tournee(char *nom, points* nuage_point, graphe g, int* res_tournee){
	FILE* dst;
	char name[128], cmd[256];
	sprintf(name,"/etudiants/vnguyen261/github/GRAPHE/image/%s.dot",nom);
	dst = fopen(name,"w");
	fprintf(dst,"graph %s { \n",nom);
	for(int i = 0; i < g.nbs; i++){
			fprintf(dst,"%d [pos =\"%f,%f!\";\n]",i,
			nuage_point[i].x,nuage_point[i].y);
		}
	for(int i = 1; i < g.nbs; i++){
		fprintf(dst,"%d--%d;\n",res_tournee[i-1],res_tournee[i]);
	}
	fprintf(dst,"%d--%d;\n",res_tournee[g.nbs-1],res_tournee[0]);
	fputs("}",dst);
	fclose(dst);
	sprintf(cmd,"dot -Kfdp -n -Tpng %s -o %s.png",name,nom);
	system(cmd);
}
