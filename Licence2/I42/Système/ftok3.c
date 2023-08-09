#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <signal.h>
#include <time.h>
#include <sys/ipc.h>

int main() {
    int x = ftok(getenv("HOME"), 6);
    printf("%d\n", x);
    return 0;
}