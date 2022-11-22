#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stddef.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <signal.h>
#include <sys/ipc.h>

typedef struct Personne {
    char nom[20];
    char prenom[20];
    unsigned short age;
} Personne;

typedef struct Adresse {
    unsigned int num_rue;
    char *nom_voie;
    unsigned int code_postale;
    char *ville;
} Adresse;

typedef struct Voisin {
    Personne pers;
    struct Voisin *gauche;
    struct Voisin *droite;
} Voisin;

typedef struct Rue {
    Voisin *p_voisin;
    Voisin *d_voisin;
} Rue;

Rue *population(int n) {
    int i = 0;
    Rue *liste = (Rue*)malloc(sizeof(Rue));
    Voisin *droite = NULL;
    Voisin *new = NULL;
    while (i < n) {
        Voisin *new = (Voisin*)malloc(sizeof(Voisin));
        printf("Nom: ");
        scanf("%s", new->pers.nom);
        
        printf("Prenom: ");
        scanf("%s", new->pers.prenom);
        
        printf("Age: ");
        scanf("%hd", &new->pers.age);
        
        new -> droite = droite;
        new -> gauche = NULL;
        if (i == 0) {
            liste -> p_voisin = new;
        } else
            droite -> gauche = new;
        droite = new;
        i++;
    }
    liste -> d_voisin = new;
    return liste;
}

int voisinAvant(Voisin *v) {
    Voisin *sauv = v;
    int somme = 0;
    while (sauv != NULL) {
        somme++;
        sauv = sauv -> gauche;
    }
    return somme;
}

int voisinApres(Voisin *v) {
    Voisin *sauv = v;
    int somme = 0;
    while (sauv != NULL) {
        somme++;
        sauv = sauv -> droite;
    }
    return somme;
}

int nouvelArrivant(Rue *r, Voisin *v, int num) {
    int i = 0;
    Voisin *aux = r->p_voisin;
    if (num == 0) {
        v->gauche = r -> p_voisin;
        v -> gauche -> droite = v;
        v->droite = NULL;
        r->p_voisin = v->droite;
    }
    else {
        while ((i < num) && (aux->gauche != NULL)) {
            aux = aux -> gauche;
            i++;
        }
        v -> gauche = aux;
    }
    if (i == num) {
        v -> gauche = aux;
        aux -> droite -> gauche = v;
        v -> droite = aux -> droite;
        aux -> droite = v;
    } else {
        v -> droite = aux;
        v -> gauche = NULL;
        aux -> gauche = v;
        r -> d_voisin = v;
    }
    return 1;
}

/*int main() {
    population(2);
    return 0;
}*/

#define N 2
int main() {
    int pid = 0, i = 0, pidinit = getpid();
    printf("Pere de pid init: %d\n", pidinit);
    while (fork()) {
        pid = fork();
        printf("boucle num %d, pid: %d\n", i, getpid());
        i++;
        if (i >= N)
            break;
    }
    if (!pid) {
        printf("\tje suis un fils, mon pid est de %d ou %d\n", getpid(), fork());
        exit(0);
    }
    while (wait(NULL) != -1);
    return 0;
}