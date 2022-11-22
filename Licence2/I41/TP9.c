#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <math.h>
#include <time.h>
#include <stdbool.h>

typedef struct tjeton {
    float nombre;
    char op;
    enum {operateur_unaire, operateur_binaire, nombre} type;
} tjeton;

typedef tjeton *texpr;

typedef struct pile {
    tjeton jeton;
    struct pile *next;
} pile;

typedef pile *tpile;

tjeton Chaine2Jeton(char *chaine) {
    tjeton j;
    if (strcmp(chaine, "+") == 0) {
        j.type = operateur_binaire;
        j.op = '+';
        j.nombre = 0;
    }
    else if (strcmp(chaine, "-") == 0) {
        j.type = operateur_binaire;
        j.op = '-';
        j.nombre = 0;
    }
    else if (strcmp(chaine, "*") == 0) {
        j.type = operateur_binaire;
        j.op = '*';
        j.nombre = 0;
    }
    else if (strcmp(chaine, "/") == 0) {
        j.type = operateur_binaire;
        j.op = '/';
        j.nombre = 0;
    }
    else if (strcmp(chaine, "_") == 0) {
        j.type = operateur_binaire;
        j.op = '-';
        j.nombre = 0;
    }
    else {
        j.type = nombre;
        j.op = '\0';
        j.nombre = atof(chaine);
    }
    return j;
}

texpr Arg2Expr(char **arguments, int n) {
    texpr liste = malloc(sizeof(tjeton)*n);
    for (int i=0; i<n; i++) {
        liste[i] = Chaine2Jeton(arguments[i]);
    }
    return liste;
}

void affiche(texpr t, int n) {
    for (int i=0; i<n; i++) {
        printf("%.1f | ", t[i].nombre);
    }
    printf("\n");
}

tpile Empiler(tpile piles, float nombres) {
    tpile p = malloc(sizeof(pile)); 
    tjeton j;
    j.nombre = nombres;
    j.op = '\0';
    j.type = nombre;
    p -> jeton = j;
    if (piles != NULL) {
        p -> next = piles;
    } else 
        p -> next = NULL;
    piles = p;
    return piles;
}

tpile Depiler(tpile pile, float *nombre) {
    tpile p = pile;
    if ((pile != NULL)) {
        if (pile->next != NULL) {
            pile = p -> next;
        }
        else 
            pile = NULL;
        *nombre = p->jeton.nombre;
        free(p);
    }
    return pile;
}

void AfficherPile(tpile pile) {
    tpile p = pile;
    if (pile == NULL)
        return;
    while (p != NULL) {
        printf("%.2f\n", p->jeton.nombre);
        printf("-----\n");
        p = p -> next;
    }
}

float Operer(float x, float y, char op) {
    float resultat = 0;
    if (op == '+') {
        resultat = x + y;
        printf("%.2f + %.2f = %.2f\n", x, y, resultat);
    }
    else if (op == '-') {
        resultat = x - y;
        printf("%.2f - %.2f = %.2f\n", x, y, resultat);
    }
    else if (op == '*') {
        resultat = x * y;
        printf("%.2f * %.2f = %.2f\n", x, y, resultat);
    }
    else if (op == '/') {
        resultat = x / y;
        printf("%.2f / %.2f = %.2f\n", x, y, resultat);
    }
    return resultat;
}

tpile Evaluer(texpr expr, int n) {
    tpile p = NULL;
    float x = 0;
    float y = 0;
    for (int i=0; i<n; i++) {
        x = 0;
        y = 0;
        if (expr[i].type == operateur_binaire) {
            p = Depiler(p, &x);
            p = Depiler(p, &y);
            y = Operer(y, x, expr[i].op);
            p = Empiler(p, y);
        }
        else if (expr[i].type == operateur_unaire) {
            p = Depiler(p, &x);
            y = Operer(x, y, expr[i].op);
            p = Empiler(p, y);
        } else
            p = Empiler(p, x);
    }
    return p;
}

int main() {
    //tjeton t = Chaine2Jeton("2.25");
    tpile p = NULL;
    //p = Empiler(p, 2.25);
    //float x = 2.25;
    //p = Depiler(p, &x);
    //printf("%.2f\n", p->jeton.nombre);
    //affiche(&t, 1);
    //AfficherPile(p);
    //float f = Operer(2.0, 2.0, '/');
    //printf("%f\n", f);
    char *chaine[4] = {"2", "3", "+", "-"};
    texpr tex = Arg2Expr(chaine, 4);
    p = Evaluer(tex, 4);
    AfficherPile(p);
    return 0;
}