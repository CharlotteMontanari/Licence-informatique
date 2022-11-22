#include <stdio.h>
#include <stdlib.h>

/*FILE* f;
int main() {
    f = fopen("TP4.txt", "r");
    if (f == NULL)
        return 1;
    
    char c = fgetc(f);
    while (c != EOF) {
        c = fgetc(f);
    }
    fclose(f);
} */ //lire les caractere d'un fichier

/*FILE* f;
int main() {
    f = fopen("mes_caracteres.txt", "w");
    
    char c;
    printf("Saisir une phrase: ");
    c = fgetc(stdin);
    while (c != '\n') {
        c = fputc(c, f);
        c = fgetc(stdin);
    }
    fclose(f);
}*/

/*FILE* f1;
FILE* f2;

int main() {

    f1 = fopen("entree.txt", "w");
    f2 = fopen("sortie.txt", "w");

    char c;
    printf("Saisir une phrase: ");
    c = fgetc(stdin);
    while (c != '\n') {
        c = fputc(c, f1);
        c = fputc(c, f2);
        c = fgetc(stdin);
    }
    fclose(f1);
}*/

/*int main() {
    FILE* f;
    FILE* clavier;

    f = fopen("mon_texte.txt", "w");

    int nbrelignes = 5;
    int nbrecar = 3;
    int nl = 0;
    int nc = 0;
    
    clavier = stdin;
    char c;
    c = fgetc(clavier);
    while (c != '*') {
        fputc(c, f); 
        c = fgetc(clavier);
    }
    fclose(f);

    f = fopen("mon_texte.txt", "r");
    c = fgetc(f);
    while ((c != EOF) && (nl < nbrelignes)){
        if (c == '\n') {
            nl += 1;
            nc = 0;
            printf("%c", c);
        } else if (nc < nbrecar) {
            nc += 1;
            printf("%c", c);
        }
        c = fgetc(f);
    }
    fclose(f);
}*/

/*int main() {
    FILE* f;

    char nom[6] = "";
    char prenom[3] = "";
    char numero_tel[10] = "";
    char adresse_mail[18] = "";

    f = fopen("Annuaire.txt", "r");
    if (f != NULL) {
        fscanf(f, "%s %s %s %s", &nom, &prenom, &numero_tel, &adresse_mail);
        printf("Nom: %s\nPrenom: %s\nNumero telephone: %s\nAdresse mail: %s\n", 
                nom, prenom, numero_tel, adresse_mail);

        fclose(f);
    }
    return 0;
}*/

