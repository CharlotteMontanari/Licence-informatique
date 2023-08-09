#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>
#include <errno.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <sys/ipc.h>
#include <sys/sem.h>
#include <sys/shm.h>

//creation memoire partagee
struct sembuf operation[1];

union {
	int val ;
	struct semid_ds *buf ;
	ushort array[3] ; 
} arg ;

#define CLE 1
#define CLE_MEM1 2
#define CLE_MEM2 1
int semid;
int shmid1;
int shmid2;
int *nbre_passagers_arrivants;
int *nbre_passagers_partants;
char *chemin = "DM.c";

void piste_aeroport_decollage(int nbre_decollage) {
    srand(time(NULL)*getpid());  //initiation random

    int waiting_time = 1 + (rand()%10);  //temps d'attente aleatoire pour savoir qui va commencer
    int temps_decollage = 5;

    sleep(waiting_time);
    
    int nbre_passagers = 1 + (rand()%256);

    printf("Vol numero %d de %d passagers souhaite decoller\n", getpid(), nbre_passagers);
    //prise du jeton pour decollage
    operation[0].sem_num = 0;
	operation[0].sem_op = -1;
	operation[0].sem_flg = SEM_UNDO; //l'oreration s'annule si le processus se termine

    //test si erreur sur le semaphore
    if (semop(semid, operation, 1) == -1)
		perror("Erreur d'opération sur le sémaphore prise decollage\n");
    printf("\tVol numero %d de %d passagers en phase de decollage\n", getpid(), nbre_passagers);
    sleep(temps_decollage);

    //remise jeton decollage
    operation[0].sem_num = 0;
	operation[0].sem_op = 1;
	operation[0].sem_flg = SEM_UNDO;
    printf("\t\tPiste libérée par vol numero %d\n", getpid());

    if (semop(semid, operation, 1) == -1)
		perror("Erreur d'opération sur le sémaphore prise nbre passager partant\n");
    //compter le nbre de passager partant
    operation[0].sem_num = 1;
	operation[0].sem_op = -1;
	operation[0].sem_flg = SEM_UNDO;
    //on stock dans nbre de passager dans passager partants
    *nbre_passagers_partants = *nbre_passagers_partants + nbre_passagers;

    if (semop(semid, operation, 1) == -1)
		perror("Erreur d'opération sur le sémaphore rend nbre passager partant\n");
    //remise du jeton du nbre de passager partant
    operation[0].sem_num = 1;
	operation[0].sem_op = 1;
	operation[0].sem_flg = SEM_UNDO;

}

void piste_aeroport_atterrissage(int nbre_atterrissage) {
    srand(time(NULL)*getpid());  //initiation random

    int waiting_time = 1 + (rand()%10);
    int temps_atterrissage = 3;

    sleep(waiting_time);
    
    int nbre_passagers = 1 + (rand()%256);

    printf("Vol numero %d de %d passagers souhaite atterrir\n", getpid(), nbre_passagers);
    //prise du jeton pour atterrissage
    operation[0].sem_num = 0;
	operation[0].sem_op = -1;
	operation[0].sem_flg = SEM_UNDO; //l'oreration s'annule si le processus se termine

    //test des erreurs sur le semaphore
    if (semop(semid, operation, 1) == -1)
		perror("Erreur d'opération sur le sémaphore prise atterrissage\n");
    printf("\tVol numero %d de %d passagers en phase d'atterrissage\n", getpid(), nbre_passagers);
    sleep(temps_atterrissage);

    //remise jeton atterrissage
    operation[0].sem_num = 0;
	operation[0].sem_op = 1;
	operation[0].sem_flg = SEM_UNDO;
    printf("\t\tPiste libérée par vol numero %d\n", getpid());

    if (semop(semid, operation, 1) == -1)
		perror("Erreur d'opération sur le sémaphore prise nbre passager arrivant\n");
    //compter le nbre de passager arrivant
    operation[0].sem_num = 2;
	operation[0].sem_op = -1;
	operation[0].sem_flg = SEM_UNDO;
    //on stock le nbre de passager arrivant dans passager arrivant
    *nbre_passagers_arrivants = *nbre_passagers_arrivants + nbre_passagers;

    if (semop(semid, operation, 1) == -1)
		perror("Erreur d'opération sur le sémaphore rend nbre passager arrivant\n");
    //remise du jeton du nbre de passager arrivant
    operation[0].sem_num = 2;
	operation[0].sem_op = 1;
	operation[0].sem_flg = SEM_UNDO;
    
}

int main(int argc, char **argv) {
    int pid = getgid();
    int decollage = atoi(argv[1]); //on recupere la valeur dans argv pour le decollage
    int atterrissage = atoi(argv[2]); //on recupere la valeur dans argv pour l'atterrissage
    int i = 0;
    int n = decollage + atterrissage; //on crée une variable n pour la somme totale de boucle

    //on test s'il n'y a pas d'erreur sur la création de semaphore
    if ((semid = semget(ftok(chemin, (key_t)CLE), 3, 0600 | IPC_CREAT)) == -1) {
        perror("Impossible de créer l'ensemble de semaphores");
        exit(1);
    }

    //initialisation du nombre de jetons
    //1 jeton pour la piste
    arg.val = 1; //piste
    if ((semctl(semid, 0, SETVAL, arg)) == -1){
		perror("Erreur d'initialisation pour piste");
		exit(1);
	}

    //1 jeton pour le nbre de passager arrivant
    arg.val = 1; //nbre passager arrivant
    if ((semctl(semid, 1, SETVAL, arg)) == -1) {
		perror("Erreur d'initialisation pour passager arrivant");
		exit(1);
	} 

    //1 jeton pour le nombre de passager partant
    arg.val = 1; //nbre passager partant
    if ((semctl(semid, 2, SETVAL, arg)) == -1) {
		perror("Erreur d'initialisation pour passager partant");
		exit(1);
	}

    //recuperation du shmid 1 
    if ((shmid1 = shmget(ftok(chemin, (key_t)CLE_MEM1), 4, IPC_CREAT | IPC_EXCL | SHM_R | SHM_W)) == -1) {
		perror("Echec de shmget 1");
		exit(1);
	}

    //recuperation du shmid 2
    if ((shmid2 = shmget(ftok(chemin, (key_t)CLE_MEM2), 4, IPC_CREAT | IPC_EXCL | SHM_R | SHM_W)) == -1) {
		perror("Echec de shmget 2");
		exit(1);
	}

    //attachement du processus à la zone de memoire
	//récuperation du pointeur sur la zone mémoire commune
    if ((nbre_passagers_arrivants = (int*)shmat(shmid1, 0, 0)) == (int*)-1) {
		perror("attachement nbre_passagers_arrivants impossible");
		exit(1);
	}

    if ((nbre_passagers_partants = (int*)shmat(shmid2, 0, 0)) == (int*)-1) {
		perror("attachement nbre_passagers_arrivants impossible");
		exit(1);
	}

    //execution fonction decollage
    *nbre_passagers_partants = 0;
    while (i < decollage) {
        pid = fork();
        if (pid == 0) {
            piste_aeroport_decollage(decollage);
            exit(0);
        }
        i++;
    }

    //execution fonction atterrissage
    i = 0;
    *nbre_passagers_arrivants = 0;
    while (i < atterrissage) {
        pid = fork();
        if (pid == 0) {
            piste_aeroport_atterrissage(atterrissage);
            exit(0);
        }
        i++;
    }

    for (int i=0; i<n; i++)
        waitpid(-1, NULL, 0);

    printf("Fin de journée\n");
    sleep(1);
    printf("Nombre de passagers arrivants: %d\n", *nbre_passagers_arrivants);
    sleep(1);
    printf("Nombre de passagers partants: %d\n", *nbre_passagers_partants);
    sleep(1);
    
    
    //detachement des segments
    if (shmdt(nbre_passagers_partants) == -1) {
        perror("Détachement impossible");
        exit(1);
    }

    if (shmdt(nbre_passagers_arrivants) == -1) {
        perror("Détachement impossible");
        exit(1);
    }

    //destruction du semaphore et de la mémoire partagee
    shmctl(shmid1, IPC_RMID, NULL);
    shmctl(shmid2, IPC_RMID, NULL);
    semctl(semid, 0, IPC_RMID, NULL);
    exit(0);
}