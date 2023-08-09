#include "postfix_to_af.h"
#include "afn.h"
#include "compregex.h"

AFN expr_to_af(char *postfix, char *alphabet) {
    if (postfix != NULL) {  //on test bien que notre liste en postfix n'est pas vide, sinon on retourne null
        int taille = strlen(postfix);
        int i = 0;
        AFN *pile = malloc(sizeof(AFN) * strlen(postfix));  //j'alloue une pile pour empiler les afn
        int sommet = 0;
        AFN temp;
        while (i != taille) {
            if (postfix[i] > 96 && postfix[i] < 122) {  //si l'element dans postfix est un caractere
                pile[sommet++] = afn_char(postfix[i], alphabet);    //je cree un afn char du caractere
            }
            else if (postfix[i] == '.') {   //si l'element est un point
                temp = afn_concatenation(pile[sommet-2], pile[sommet-1]);   //je stock dans temp la concatenation des deux derniers element de la pile
                afn_free(pile[sommet-2]);
                afn_free(pile[sommet-1]);
                pile[sommet-2] = temp; //je reempile le nouvel element
                sommet--;
            }
            else if (postfix[i] == '*') {   //si mon element est un fois
                temp = afn_kleene(pile[sommet-1]);  //je stock dans temp l'etoile de kleene du dernier element
                afn_free(pile[sommet-1]);
                pile[sommet-1] = temp;  //je reempile le nouvel element
            }
            else if (postfix[i] == '+') {   //si mon element est un plus
                temp = afn_union(pile[sommet-2], pile[sommet-1]);   //je stock dans temp l'union des deux derniers elements de la pile
                afn_free(pile[sommet-2]);
                afn_free(pile[sommet-1]);
                pile[sommet-2] = temp;  //je reempile le nouvel element
                sommet--;
            }
            i++;
        }
        temp = pile[sommet-1];  //je stock dans temp de dernier resultat de mon operation
        free(pile); //et je lui libere la memoire
        free(postfix);
        return temp;
    }
    printf("Erreur postfix\n");
    return NULL;
}