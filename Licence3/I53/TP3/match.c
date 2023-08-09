#include <regex.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*typedef struct {
    regoff_t rm_so;
    regoff_t rm_eo;
} regmatch_t;*/

int main(int argc, char *argv[]) {
    regex_t regex;
    size_t nmatch = 1;
    regmatch_t match[nmatch];
    if (regcomp(&regex, argv[1], REG_EXTENDED) != 0)
        return 1;
    if (regexec(&regex, argv[2], nmatch, match, 0) == 0) {
        printf("motif trouve !\n\n");
        for (int i=0; i<nmatch; i++)
            printf("Début: %lld\t Fin: %lld\n", match[i].rm_so, match[i].rm_eo);
    }
    else
        printf("motif non trouve !\n");
    regfree(&regex);
    return 0;
}
