//Exercice 1
//#include <stdio.h>

//int main() {

   // printf("Hello World\n");
    //return 0;
//}


//Exercice 3.1
//#include <stdio.h>

//int main() {

//    char lettre = 'c';
//    printf("Le code ASCII de %c est %d\n", lettre, lettre);
//    return 0;
//}

//Exercice 3.3
//#include <stdio.h>

//int main() {

//    char lettre;

//    printf("Saisir un caractère: ");
//    scanf("%c", &lettre);
//    printf("Le code ASCII de %c est %d\n", lettre, lettre);
//    return 0;
//}

//#include <stdio.h>

//int main() {

//    int c;
//    printf("Saisir un caractere: ");
//    c = getchar();
//    printf("The ASCII code for the character %d is %d\n", c, c);
//    return 0;
//}

//Exercice 3.4
//#include <stdio.h>

//int main() {

//    char lettre;

//    printf("Saisir un caractère: ");
//    scanf("%c", &lettre);
//    printf("Le code ASCII de %c est %d\n", lettre, lettre);
//    printf("On a fait l exercice 2\n");
//    return 0;
//}

//Exercice 4
//#include <stdio.h>

//int main() {
//    int x = 1, y = 2;
//    int m;

//    if (x > y) {
//        m = x;
//        printf("%d\n", m);
//    } else {
//        m = y;
//        printf("%d\n", m);
//    }
//    return 0;
//}

//Exercice 4.3
//#include <stdio.h>

//int main() {

//    int x, y;

//    printf("Saisir x: ");
//    scanf("%d", &x);

//    printf("Saisir y: ");
//    scanf("%d", &y);

//    if (x > y) {
//        printf("Le maximum entre x = %d et y = %d est x = %d\n", x, y, x);
//    } else {
        
//        printf("Le maximum entre x = %d et y = %d est y = %d\n", x, y, y);
//    }
//    return 0;
//}

//Exercice 5
//#include <stdio.h>

//int main() {

//    int date;
//    printf("Saisir une date: ");
//    scanf("%d", &date);
//    int jour = date % 100;
//    date = date / 100;
//    int mois  = date % 100;
//    date = date / 100;
//    int annee = date;
//    printf("%d %d %d\n", jour, mois, annee);
//    return 0;
//}

//Exercice 6
#define TYPE char
#include <stdio.h>

void fonction(TYPE n) {

    TYPE i;
    int j, taille;
    taille = 8 * sizeof(TYPE);
    for (j = 0; j < taille; j++){
        i = 1 << (taille - j - 1);
        if (n & i) 
            printf("1");
        else    
            printf("0");
    }
    printf("\n");
}

//int main() {
//    fonction(12);
//    return 0;
//}

//Ecxercice 7
#include <stdio.h>

typedef union {int entier; float reel; }entreel;

int main() {
    entreel f;
    int signe, mantisse, exposant;
    printf("Saisir un nbre: ");
    scanf("%f", &f.reel);
    printf("%f\n", f.reel);
    printf("%d\n", f.entier);
    fonction(f.entier);
    signe = (f.entier >> 31) & 1;
    mantisse = (f.entier) & 0b11111111111111111111111;
    exposant = (f.entier >> 23) & 0b11111111;
    printf("%d %d %d\n", signe, mantisse, exposant);
}