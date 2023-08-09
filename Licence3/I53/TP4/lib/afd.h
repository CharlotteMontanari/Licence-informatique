#ifndef AFD_H
#define AFD_H

#define ASCII_FIRST 38
#define ASCII_LAST 127
#define MAX_SYMBOLES 90

struct AFD {
	int Q, q0, lenF, lenSigma;
	int *F;
	char *Sigma;
	char dico[MAX_SYMBOLES];
	int **delta;
};

typedef struct AFD *AFD;

AFD afd_init(int Q, int q0, int nbFinals, int *listFinals, char *Sigma);
void afd_ajouter_transition(AFD A, int q1, char s, int q2);
void afd_print(AFD A);
void afd_free(AFD A);

AFD afd_finit(char *file);
int afd_simuler(AFD A, char *s);

#endif
