#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <signal.h>

//le buffer se vide lorsqu'il rencontre un retour à la ligne
//buffer: mémoire temporaire où sont stockées les messages

//Le type pid_t correspond à un entier

/*int main() {
  printf("Hello world");
  sleep(5);
  printf("\nBye Bye\n");
  return 0;
}*/

/*int main() {
  printf("Hello world");
  fflush(stdout);
  sleep(5);
  printf("\nBye Bye\n");
  return 0;
}*/

/*int main() {
  printf("Hello world\n");
  sleep(5);
  printf("\nBye Bye\n");
  return 0;
}*/

/*int main() {
    int i;
    printf("Je suis seul\n");
    for (i = 10; i > 0; i--) {
        printf("%d ", i);
        fflush(stdout);
        sleep(1);
    }
    printf("\nNous sommes deux maintenant\n");
    int x = fork();
    if (x == 0)
        printf("Je suis le père, mon fils a pour PID: %d\n", getppid());
    if (x != 0)
        printf("Je suis le fils, mon père a pour PID: %d\n", getpid());
    //while(1);
}*/

/*int main() {
    int n = 0;
    pid_t x = fork();
    if (x == 0) {
        n++;
        printf("Fils:%d %p\n", n, &n);
    }
    if (x != 0) {
        wait(NULL);
        printf("Père: %d %p\n", n, &n);
    }
}*/

/*void reception() {
    printf("PID fils: %d\n", getppid());
}*/

/*int main() {
    pid_t pid = fork();
    if (pid != 0) {
        signal(SIGUSR1, reception);
        wait(NULL);
    } else {
        sleep(1);
        kill(getppid(), SIGUSR1);
    }
}*/

/*int main() {
    pid_t x = fork();
    if (x != 0) {
        signal(SIGUSR1, traitersignal);
        pause();
        printf("PID fils: %d\n", x);
    }
    if (x == 0) {
        sleep(5);
        kill(getpid(), SIGUSR1);
    }
}*/

/*int i = 0;

void recu() {
    i = 0;
    printf("Signal recu\n");
}*/

/*int main() {
    pid_t pid = fork();
    if (pid != 0) {
        signal(SIGUSR1, recu);
        while(1);
    } 
    else {
        while (i < 10) {
            sleep(1);
            i++;
        }
        kill(getppid(), SIGTERM);
    }
}*/

/*int main(int argc, char** argv) {
    int i = 1;
    while (i < argc) {
        pid_t x = fork();
        if (x == 0) {
            execlp(argv[i], argv[i], NULL);
            return 0; //si une erreur est rencontrée comme un mot qui n'est pas une commande, 
                      //il ne s'exécute pas et passe à la commande d'après
        }
        else
            wait(NULL);
        i++;
    }
}*/

/*int main(int argc, char** argv) {
    for (int i = 1; i<argc; i++) {
        pid_t x = fork();
        if (x == 0)
            execlp(argv[i], argv[i], NULL);
        else
            wait(NULL);
    }
}*/

