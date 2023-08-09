#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <signal.h>
#include <time.h>
#include <sys/ipc.h>

typedef int Semaphore[2];
Semaphore S;

void initSem(Semaphore s, int n) {
    pipe(s);
    char valeur = 'a';
    for (int i=0; i<n; i++) {
        write(s[1], &valeur, sizeof(valeur));
    }
}

void P(Semaphore s) {
    char lettre;
    read(s[0], &lettre, sizeof(lettre));
}

void V(Semaphore s) {
    char lettre = 'c';
    write(s[1], &lettre, sizeof(lettre));
}

void piste_aeroport(int decollage, int atterissage) {
    //decollage -> P
    //atterissage -> V
    initSem(S, 1);
    srand(time(NULL));
    for (int i=0; i<decollage; i++) {
        if (!fork()) {
            sleep(rand()%10);
            printf("Vol numero %d souhaite decoller\n", getpid());
            P(S);
            printf("\tVol numero %d en phase de decollage\n", getpid());
            sleep(5);
            printf("\t\tPiste libérée par vol numero %d\n", getpid());
            V(S);
            exit(1);
        }
        else
            wait(NULL);
    }
    for (int i=0; i<atterissage; i++) {
        if (!fork()) {
            sleep(rand()%10);
            printf("Vol numero %d souhaite atterrir\n", getpid());
            P(S);
            printf("\tVol numero %d en phase d'atterissage\n", getpid());
            sleep(3);
            printf("\t\tPiste libérée par vol numero %d\n", getpid());
            V(S);
            exit(1);
        }
        else
            wait(NULL);
    }
}

/*int main(int argc, char **argv) {
    piste_aeroport(atoi(argv[1]), atoi(argv[2]));
}*/

