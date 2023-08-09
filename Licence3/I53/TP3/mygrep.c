#include <regex.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// "([0-9]{1,3}\.){3}[0-9]{1,3}" format d'une adresse ip

int main(int argc, char *argv[]) {
    FILE *file = fopen("file.txt", "r");
    regex_t regex;
    size_t nmatch = 1;
    regmatch_t match[nmatch];
    int taille_max = 100;
    char ligne[taille_max];
    if (regcomp(&regex, argv[1], REG_EXTENDED) != 0)
        return 1;
    while (fgets(ligne, taille_max, file) != NULL) {
        char *ptr = ligne;
        if (regexec(&regex, ptr, nmatch, match, 0) == 0)
            printf("%s", ptr);
        while (regexec(&regex, ptr, nmatch, match, 0) == 0) {
            for (int i=0; i<match[0].rm_eo; i++) {
                if (i >= match[0].rm_so && i < match[0].rm_eo) 
                    printf("^");
                else
                    printf(" ");
            } 
            ptr = ptr + match[0].rm_eo;
        }
    }
    printf("\n");
    fclose(file);
    return 0;
}