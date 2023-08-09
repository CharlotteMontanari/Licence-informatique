#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <signal.h>
#include <time.h>
#include <sys/ipc.h>
#include <sys/sem.h>

/*int semget(key, nsems, semflg) {
    key_t key1 ; // cle de l'ensemble 
    int nsems1 ; // nombre de sémaphores 
    int semflg1; // Droits et options 
    return 0;
}*/

int main() {
    int x = semget(ftok(getenv("HOME"), 1), 4, IPC_CREAT | 3777);
    printf("%d\n", x);
    return 0;
}