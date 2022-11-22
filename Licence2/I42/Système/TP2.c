#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <signal.h>
#include <time.h>

/*int main(int argc, char **argv) {
    unsigned int n = atoi(argv[1]);
    srand(time(NULL));
    unsigned int *vect1 = malloc(sizeof(unsigned int)*n);
    unsigned int *vect2 = malloc(sizeof(unsigned int)*n);
    int somme = 0;
    for (int i=0; i<n; i++) {
        vect1[i] = rand()%10;
        vect2[i] = rand()%10;
    }
    int tube[2];
    pipe(tube);
    for (int j=0; j<n; j++) {
        if (!fork()) {
            unsigned int valeur = vect1[j] * vect2[j];
            printf("Processus %d a calculé: %d * %d = %d\n", j, vect1[j], vect2[j], valeur);
            write(tube[1], &valeur, sizeof(valeur));
            exit(0);
        }
    }
    unsigned int valeur;
    close(tube[1]);
    while (read(tube[0], &valeur, sizeof(unsigned int)))
        somme += valeur;
    printf("Résultat: %d\n", somme);
    return 0;
}*/

/*int main(int argc, char** argv) {
    int tube[2];
    pipe(tube);
    pid_t x = fork();
    if (x == 0) {
        close(tube[0]);
        dup2(tube[1], STDOUT_FILENO);
        execlp(argv[1], argv[1], NULL);
    }
    else {
        close(tube[1]);
        dup2(tube[0], STDIN_FILENO);
        execlp(argv[2], argv[2], NULL);
    }
}*/

/*int main(int argc, char **argv) {
    int tube[2];
    pipe(tube);
    for (int i=2; i<argc; i++) {
        if (!fork()) {
            close(tube[0]);
            dup2(tube[1], STDOUT_FILENO);
            execlp("grep", "grep", "-c", argv[1], argv[i], NULL);
        } 
    }
    close(tube[1]);
    char valeur;
    int somme = 0;
    while (read(tube[0], &valeur, sizeof(char)))
        somme += atoi(&valeur);
    printf("Résultat: %d\n", somme);
    return 0;
}*/

/*int main(int argc, char **argv) {
    int tube1[2]; int tube2[2]; int tube3[2];
    pipe(tube1); pipe(tube2); pipe(tube3);
    srand(time(NULL));
    int n = atoi(argv[1]);
    if (!fork()) {
        close(tube1[0]);
        close(tube3[0]);
        close(tube2[0]);
        close(tube2[1]);
        for (int i=0; i<n; i++) {
            int alea = rand()%100;
            int stock1 = alea;
            write(tube1[1], &stock1, sizeof(int));
            write(tube3[1], &stock1, sizeof(int));
        }  
    }
    else if (!fork()) {
        close(tube1[1]);
        close(tube2[0]);
        close(tube3[0]);
        close(tube3[1]);
        int constante = 2;
        int stock2;
        for (int i=0; i<n; i++) {
            read(tube1[0], &stock2, sizeof(int));
            stock2 += constante;
            write(tube2[1], &stock2, sizeof(int));
        }
    }
    else if (!fork()) {
        close(tube2[1]);
        close(tube3[1]);
        close(tube1[0]);
        close(tube1[1]);
        int stock3; int stock4;
        for (int i=0; i<n; i++) {
            read(tube2[0], &stock3, sizeof(int));
            read(tube3[0], &stock4, sizeof(int));
            int difference = stock3 - stock4;
            printf("Nombre1: %d\n", stock3);
            printf("Nombre2: %d\n", stock4);
            printf("Différence: %d\n\n", difference);
        }
    }
    else {
        close(tube1[0]);
        close(tube1[1]);
        close(tube2[0]);
        close(tube2[1]);
        close(tube3[0]);
        close(tube3[1]);
        wait(NULL);
        wait(NULL);
        wait(NULL);
    }
}*/
