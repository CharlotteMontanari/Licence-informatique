#include <stdio.h>
#include "afd.h"
#include "afn.h"

int main() {

	//PARTIE TEST AFD
	AFD  A;
	int Q = 3, q0 = 0, nbFinals = 2, listFinals[2] = {1, 3}, nbInitaux = 2, listInitiaux[2] = {0, 1};
	char Sigma[] = "abc";
	printf("\nAFD init\n");
	A = afd_init(Q, q0, nbFinals, listFinals, Sigma);

	afd_ajouter_transition(A, 0,'a',2);
	afd_ajouter_transition(A, 0,'b',1);
	afd_ajouter_transition(A, 0,'c',0);
	afd_ajouter_transition(A, 1,'a',2);
	afd_ajouter_transition(A, 1,'b',0);
	afd_ajouter_transition(A, 1,'c',3);
	afd_ajouter_transition(A, 2,'a',3);
	afd_ajouter_transition(A, 2,'b',1);
	afd_ajouter_transition(A, 2,'c',3);
	afd_ajouter_transition(A, 3,'a',2);
	afd_ajouter_transition(A, 3,'b',1);
	afd_ajouter_transition(A, 3,'c',3);

	int s = afd_simuler(A, "aab");
	printf("AFD simuler: %d\n", s);

	afd_print(A);
	afd_free(A);

	AFD C;
	printf("\nAFD finit\n");
	C = afd_finit("./data/afd.txt");
	afd_print(C);
	afd_free(C);

	//PARTIE TEST AFN

	AFN B;
	printf("\nAFN init\n");
	B = afn_init(Q, nbInitaux, listInitiaux, nbFinals, listFinals, Sigma);

	afn_ajouter_transition(B, 0,'a',2);
	afn_ajouter_transition(B, 0,'a',1);
	afn_ajouter_transition(B, 0,'a',0);
	afn_ajouter_transition(B, 1,'a',2);
	afn_ajouter_transition(B, 1,'b',0);
	afn_ajouter_transition(B, 1,'c',3);
	afn_ajouter_transition(B, 1,'&',1);
	afn_ajouter_transition(B, 2,'a',3);
	afn_ajouter_transition(B, 2,'b',1);
	afn_ajouter_transition(B, 2,'c',3);
	afn_ajouter_transition(B, 3,'a',2);
	afn_ajouter_transition(B, 3,'b',1);
	afn_ajouter_transition(B, 3,'c',3);
	
	afn_print(B);
	afn_simuler(B, "b");
	afn_free(B);

	AFN D;
	printf("\nAFN finit\n");
	D = afn_finit("./data/afn.txt");
	afn_print(D);
	afn_free(D);

	//DEUXIEME PARTIE

	AFN c1, c2, c3, d, e, f;
	printf("\nAFN char\n");
	c1 = afn_char('c', "abc");
	afn_print(c1);

	printf("************************\n");

	c2 = afn_char('b', "abc");
	afn_print(c2);

	printf("************************\n");

	c3 = afn_char('a', "abc");
	afn_print(c3);

	printf("\nAFN union\n");
	d = afn_union(c1, c2);
	afn_print(d);

	printf("\nAFN concatenation\n");
	e = afn_concatenation(c1, c2);
	afn_print(e);

	printf("\nAFN kleene\n");
	f = afn_kleene(c3);
	afn_print(f);

	afn_free(c1);
	afn_free(c2);
	afn_free(c3);
	afn_free(d);
	afn_free(e);
	afn_free(f);

	return 0;
}
