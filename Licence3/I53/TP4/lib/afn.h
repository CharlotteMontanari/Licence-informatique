#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <unistd.h>

#ifndef AFN_H
#define AFN_H

#define ASCII_FIRST 38
#define ASCII_LAST 127
#define MAX_SYMBOLES 90

struct AFN{
	int Q, lenI, lenF, lenSigma;
	int *I, *F;
	char *Sigma;
	char dico[MAX_SYMBOLES];
	int ***delta;
};

typedef struct AFN * AFN;

AFN afn_init(int Q, int nbInitiaux, int * listInitiaux, int nbFinals, int * listFinals, char *Sigma);
void afn_print(AFN A);
void afn_free(AFN A);

void afn_ajouter_transition(AFN A, int q1, char s, int q2);
AFN afn_finit(char *file);
int *afn_epsilon_fermeture(AFN A, int *R);
int afn_simuler(AFN A, char *s);
AFN afn_char(char c, char *sigma);
AFN afn_union(AFN a, AFN b);
AFN afn_concatenation(AFN a, AFN b);
AFN afn_kleene(AFN a);

#endif
