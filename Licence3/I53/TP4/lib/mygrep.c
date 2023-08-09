#include "compregex.h"
#include "postfix_to_af.h"

int main(int argc, char *argv[]) {
    //argv[1] = "a.(a+b)" par exemple
    //argv[2] = "ab" par exemple
    if (argc < 2) {
        printf("Erreur argv\n");
        return 0;
    }
    char *p = parseur(argv[1]);
    char *alphabet = "abc";
    if (p != NULL) {
        AFN a = expr_to_af(p, alphabet);
        afn_simuler(a, argv[2]);
        afn_print(a);
        afn_free(a);
    }
    return 0;
}