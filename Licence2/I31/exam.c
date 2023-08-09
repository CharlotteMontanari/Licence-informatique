//Écrire un programme en langage C qui demande à l'utilisateur de saisir 3 nombres 
//et affiche le plus grand d'entre eux.

//#include <stdio.h>

/*int main() {
    int a, b, c;

    printf("Saisir trois nbre: ");
    scanf("%d %d %d", &a, &b, &c);

    if (a > b && a > c)
        printf("a est le plus grand: %d\n", a);
    else if (b > a && b > c)
        printf("b est le plus grand: %d\n", b);
    else
        printf("c est le plus grand: %d\n", c);
}*/

//Écrire un programme qui demande à l'utilisateur un numéro de mois (de 1 à 12) 
//et qui affiche le nombre de jours de ce mois en utilisant if ... else. 
//Le nombre total de jours dans un mois est donné par:
//Janvier, Mars, Mai, Juillet, Aout, Octobre, Décembre: 31 jours
//Février: 28 jours
//Avril, Juin, Septembre, Novembre: 30 jours

/*#include <stdio.h>

int main() {
    int nbre;

    printf("Saisir un nbre qui correspond au mois en question: ");
    scanf("%d", &nbre);

    if (nbre == 2)
        printf("Ce mois comporte 28 jours\n");
    else if (nbre % 2 == 0)
        printf("Ce mois comporte 30 jours\n");
    else
        printf("Ce mois comporte 31 jours\n");
}*/

//Écrire un programme qui demande à l'utilisateur de saisir un nombre n affiche 
//ensuite tous les nombres entiers de 1 à n en utilisant une boucle for.

/*#include <stdio.h>

int main() {
    int nbre;

    printf("Saisir un nbre: ");
    scanf("%d", &nbre);

    for (int i=1; i <= nbre; i++)
        printf("%d\n", i);
}*/

//Écrire un programme qui demande à l'utilisateur de saisir deux nombres entiers x et n
//et qui calcule puis affiche x^n en utilisant une méthode récursive. 
//Par exemple si l'utilisateur saisit 2 pour 𝑥 et 3 pour 𝑛, 
//le programme calcule 2^3 et affiche le résultat.

/*#include <stdio.h>

int puissance(int x, int n) {
    if (n == 0)
        return 1;
    if (n == 1)
        return x;
    return x * puissance(x, n-1);
}

int main() {
    int x, n;

    printf("Saisir x et n: ");
    scanf("%d %d", &x, &n);

    int nbre = puissance(x, n);
    printf("%d\n", nbre);
}*/

//Écrire un programme qui calcule et affiche toutes les racines d'une équation quadratique.
//En algèbre, une équation quadratique est une équation sous la forme de 𝑎𝑥2+𝑏𝑥+𝑐=0
//Une équation quadratique peut avoir une ou deux racines réelles ou complexes 
//distinctes selon la nature du discriminant de l'équation. 
//Lorsque discriminant de l'équation quadratique est donné par Δ=𝑏2−4𝑎𝑐

/*#include <stdio.h>
#include <math.h>

int main() {
    int a, b, c;
    int x, y, z;
    float delta = b*b - 4.0*a*c;

    printf("Saisir a, b, c: ");
    scanf("%d %d %d", &a, &b, &c);

    if (delta > 0) {
        x = (-1.0*b + sqrt(delta)) / (2*a);
        y = (-1.0*b - sqrt(delta)) / (2*a);
        printf("x= %d\n", x);
        printf("y= %d\n", y);
    } else if (delta == 0)
        z = (-b) / (2*a);
    else {
        printf("solution1: %d + i%f\n", (-b)/(2*a), sqrt(-delta)/(2*a));
        printf("solution2: %d + i%f\n", (-b)/(2*a), sqrt(-delta)/(2*a));
    }
}*/


/*#include <stdio.h>
#include <stdlib.h>

typedef struct {
    char *nom;
    unsigned int age;
}personne;

typedef struct new new;
struct new {
    int val;
    new *next;
};

typedef struct {
    unsigned int size;
    new* first;
}stack;

stack* newStack() {
    stack *s = (stack*) malloc(sizeof(stack));
    s -> size = 0;
    s -> first = NULL;
    return s;
}

new* newPersonne(float val) {
    new *n = (new*)malloc(sizeof(new));
    n -> val = val;
    n -> next = NULL;
    return n;
}

int ajoute(stack *p, new *n) {
    if ((p == NULL) || (n == NULL)) 
        return 0;
    n -> next = p -> first;
    p -> first = n;
    p -> size += 1;
    return 1;
}

int sortir(stack *p, float v) {
    if (p == NULL) 
        return 0;
    return ajoute(p, newElement(v));
}

int main() {
    float valeur;
    stack *s = newStack();

    for (float f = 1; f < 5; f++){
        pushv(s, f);
        printf("Personne partie %f: %d ", f, s->size);
        print(s);
        printf("\n");
    }
}*/

