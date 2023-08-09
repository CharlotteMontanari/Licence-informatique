#include <stdio.h>
#include <ctype.h>

int pgcd(int a, int b) {

    int aux;

    while (b != 0) {
        aux = a;
        a = b;
        b = aux % b;
    }
    return a;
}

int ppcm(int a, int b) {
    return (a * b) / pgcd(a, b);
}

char conversion_caractere(char x) {
    if (isupper(x))
        return tolower(x);
    return toupper(x);
}

/*int main() {
    char lettre = conversion_caractere('C');
    printf("%c\n", lettre);
}*/

int est_premier(int n) {
    int somme = 0;
    int div = 1;

    while (div <= n) {
        if (n % div == 0)
            somme += 1;
        div += 1;
    }
    if (somme == 2)
        return 1;
    else
        return 0;
}

/*int main() {
    int prog = est_premier(11);
    printf("%d\n", prog);
}*/

void premier_premier(int n) {
    int i = 0;
    int nbre = 0;
    printf("[");
    while (i <= n) {
        if (est_premier(nbre)) {
            printf("%d, ", nbre);
            i += 1;
        }
        nbre += 1;
    }
    printf("]\n");
}

/*int main() {
    premier_premier(20);
}*/

