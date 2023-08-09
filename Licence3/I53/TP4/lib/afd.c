#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

#include "afd.h"

/*
 * FUNCTION: afd_init
 * ------------------
 * initialise et retourne un AFD dont les états sont numérotés de 0 à `Q`
 * 
 * param: 
 *        Q  - plus grandétat de l'automate
 *        q0 - état inital    
 *        nbFinals - nombre d'états finals
 *        listFinals - tableau de `nbFinals` entiers représentant les états finals
 *        Sigma - alphabet de l'automate
 * 
 * return:
 *        un AFD dont la tableau de transition est allouée mais vide
 */
AFD  afd_init(int Q, int q0, int nbFinals, int *listFinals, char *Sigma){
	AFD A; 
	if ((A = malloc(sizeof(struct AFD))) == NULL){
		printf("malloc error A");
		exit(1);
	}
	A->Q = Q;
	A->q0 = q0;
	A->lenF = nbFinals;
	if ((A->F = malloc(sizeof(int)*nbFinals)) == NULL){
		printf("malloc error A->F");
		exit(1);
	}

	for(int i=0; i<nbFinals; i++) 
		A->F[i] = listFinals[i];

	A->lenSigma = strlen(Sigma);
	if ((A->Sigma = malloc(sizeof(char)*(A->lenSigma+1))) == NULL){
		printf("malloc error A->Sigma");
		exit(1);
	}
	strcpy(A->Sigma,Sigma);
	for(int i=0; i<MAX_SYMBOLES; i++) 
		A->dico[i] = -1;
	for(int i=0; i<A->lenSigma; i++) 
		A->dico[Sigma[i]-ASCII_FIRST] = i;

	if ((A->delta = malloc(sizeof(int**)*(Q+1))) == NULL) {
		printf("malloc error A->Sigma");
		exit(1);
	}
	for (int q=0; q<A->Q+1; q++) {
		if((A->delta[q] = malloc(sizeof(int*) * A->lenSigma)) == NULL){
			printf("malloc error A->Sigma[%d]", q);
			exit(1);
		}
		for (int s=0; s<A->lenSigma; s++)	
			A->delta[q][s]=-1;
	}
	return A;
}

/*
 * FUNCTION: afd_ajouter_transition
 * --------------------------------
 * ajoute la transition  `q1` -- `s` --> `q2` à l'automate `A`
 * 
 * param: 
 *        A  - un AFD
 *        q1 - état de départ de la transition    
 *        s  - étiquette de la transition
 *        q2 - état d'arrivée de la transition    
 */
void afd_ajouter_transition(AFD A, int q1, char s, int q2){
	A->delta[q1][A->dico[s-ASCII_FIRST]] = q2;
}

/*
 * FUNCTION: afd_print
 * -------------------
 * affiche l'AFD `A`
 * 
 * param: 
 *        A  - un AFD
 */

void afd_print(AFD A){
	printf("Q = {0,..,%d}\n", A->Q);
	printf("q0 = %d\n", A->q0);
	printf("F = {");
	for (int i=0; i<A->lenF; i++) 
		printf("%d,", A->F[i]);
	printf("\b}\n");
	int cellsize = (int)(ceil(log10((double)A->Q))) + 1;
	int first_column_size = cellsize >= 5 ? cellsize + 2 : 7;
	int padding = (cellsize>=5)? (cellsize-5) / 2+1: 1;
	int line_length = first_column_size+1+(cellsize+2)*A->lenSigma;
	char *line = malloc(sizeof(char)*(line_length+2));
	for (int i=0; i<=line_length; i++) 
		line[i] = '-';
	line[line_length+1] = '\0';

	printf("%s\n",line);
	printf("|%*sdelta |", padding, "");
	for (int i=0; i<A->lenSigma; i++)   
		printf("%*c |", cellsize, A->Sigma[i]); printf("\n");
	printf("%s\n",line);
  

	for (int q=0; q<A->Q+1; q++){
		printf("|%*d |", padding+5, q);
		for (int i=0; i<A->lenSigma; i++){
			int s = A->dico[A->Sigma[i]-ASCII_FIRST];
			if (A->delta[q][s] !=-1)
				printf("%*d |", cellsize, A->delta[q][s]);
			else
				printf("%*s |", cellsize, "");
		}    
		printf("\n");
		printf("%s\n",line);
	}
	free(line);
}

/*
 * FUNCTION: afd_free
 * -------------------
 * libère la mémoire de l'AFD `A` initialisé par la fonction afd_init 
 * 
 * param: 
 *        A  - un AFD
 */
void afd_free(AFD A){
	free(A->F);
	free(A->Sigma);
	for (int q=0; q<A->Q+1; q++) 
		free(A->delta[q]);
	free(A->delta);
	free(A);  
}

/*
 * FUNCTION: afd_finit
 * ------------------
 * initialise et renvoie un AFD à partir du fichier `file` écrit au format:
 * 
 *  'nombre_etat
 *  'etat_initial
 *  'nombre_etats_finals
 *  'etat_final_1 etat_final_2 ... etat_final_n
 *  'alphabet
 *  'etat_i1 symbole_k1 etat_j1
 *  'etat_i2 symbole_k2 etat_j2
 *  '...
 *  'etat_in symbole_kn etat_jn 
 * 
 * param :
 *         file - un nom de fichier
 * return:
 *         un AFD complet
 */
AFD afd_finit(char *file) {
	FILE *fichier;
	fichier = fopen(file, "r"); //on ouvre le fichier afd qui contient nos donnees

	if (fichier == NULL) //si le fichier est vide, je renvoie une erreur
		printf("Erreur fichier AFD\n");

	int nbr_etat, init, nbr_final;
	fscanf(fichier, "%d", &nbr_etat);	//on recupere la 1ere ligne du fichier
	fscanf(fichier, "%d", &init);	//on recupere la 2eme ligne du fichier
	fscanf(fichier, "%d", &nbr_final);	//on recupere la 3eme ligne du fichier

	int *liste_final = malloc(sizeof(int) * nbr_final);	//on cree une liste qui contiendra les nbres finaux
	for (int i=0; i<nbr_final; i++)
		fscanf(fichier, "%d", &(liste_final[i]));	//on les lit dans le fichier et on les ajoute dans notre liste
	
	char alphabet[256];
	fscanf(fichier, "%s", alphabet);	//on lit ensuite notre alphabet
	AFD a = afd_init(nbr_etat, init, nbr_final, liste_final, alphabet); //on a toutes les donnees, on cree donc notre afd

	int q1, q2;
	char c;
	while (fscanf(fichier, "%d %c %d", &q1, &c, &q2) == 3){	//on lit les transitions, s'il n'y en a plus 3 par lignes, on a tout lu
		printf("%d %c %d\n",q1,c,q2);	//on recupere nos donnees
		afd_ajouter_transition(a, q1, c, q2);	//on met ces donnees dans notre tableau grace a la fonction ajouter transition
	}
	fclose(fichier);
	free(liste_final);
	return a;
}

/*
 * FUNCTION: afd_simuler
 * ---------------------
 * renvoie 1 si la chaine `s` est acceptée par l'AFD `A`, 0 sinon
 *
 * param:
 *        A - un AFD
 *        s - la chaine de caractères à analyser
 */
int afd_simuler(AFD A, char *s) {
	int i = 0;
	int flag = 0;
	int etat = A -> q0;
	while (A->delta[etat][A->dico[s[i]-ASCII_FIRST]] != -1 && s[i] != '\0') {	//tant qu'on lit une transition et qu'on n'est pas arrivee a la fin de notre mot
		etat = A->delta[etat][A->dico[s[i]-ASCII_FIRST]];	//on recupere l'etat dans lequel on est
		i++;
	}
	int j = 0;
	if (s[i] == '\0') {	//si on est sortit de la boucle parce que le mot est fini
		while (A->F[j] != A->F[A->lenF]) {	//on parcours la liste d'etat final
			if (etat == A->F[j])	//si notre etat est dans la liste d'etat final
				flag = 1;	//le mot est valide sinon, non
			j++;	
		}
	}
	if (flag == 0)
		printf("Chaine non acceptée\n");
	else
		printf("Chaine acceptée\n");
	return flag;
}
