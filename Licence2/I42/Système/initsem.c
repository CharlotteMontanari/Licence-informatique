#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <signal.h>
#include <time.h>
#include <sys/ipc.h>
#include <sys/sem.h>

/*union semun {
    int val; // value for SETVAL 
    struct semid_ds *buf; // buffer for IPC_STAT, IPC_SET
    unsigned short *array; // array for GETALL, SETALL 
    // tableau de taille egale au nombre de semaphores de l'ensemble 
    struct seminfo *__buf; // buffer for IPC_INFO 
}arg; */


int main() {
    union semun arg;
    arg.val = 1;
    printf("%d\n", semget(ftok(getenv("HOME"), 1), 4, 0));
    int x = semctl(semget(ftok(getenv("HOME"), 1), 4, 0), 2, SETVAL, arg);
    printf("%d\n", x);
    return 0;
}

