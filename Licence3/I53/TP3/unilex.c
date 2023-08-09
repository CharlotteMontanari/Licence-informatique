#include <regex.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    regex_t regex;
    char name [32];
} unilex_t;

unilex_t creer_unliex_table() {
    FILE *unilex = fopen("unilex.txt", "r");
    FILE *date = fopen("date.txt", "r");
    
    fclose(unilex);
    fclose(date);
}

int main(int argc, char **argv) {
    return 0;
}