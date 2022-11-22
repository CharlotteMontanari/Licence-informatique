#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

typedef unsigned char uchar;
uchar Increment(uchar *a, uchar n, uchar b) {
    uchar i = 0;
    uchar somme = 0;
    while (a[i] + 1 >= b && i < n-1) {
        a[i] = (a[i]+1) % b;
        somme++;
        i++;
    } 
    a[i] = a[i] + 1;
    somme++;
    i++;
    return somme;
}

/*int main() {
    uchar tab[4] = {9, 9, 4, 5};
    //tab = {1, 2, 3, 4};
    uchar a = Increment(tab, 4, 10);
    printf("nombre de modifications = %hhu\n", a);
    //for (int i=0; i<4; i++)
        //printf("%hhu, ", tab[i]);
}*/

typedef unsigned long long ullong;
ullong test(uchar n, uchar b) {
    uchar a[n];
    ullong somme = 0;
    int i = 0;
    while (i < pow(b, n)) {
        somme += Increment(a, n, b);
        i++;
    }
    return somme;
}

/*int main() {
    ullong x = test(4, 10);
    printf("%llu\n", x);
}*/

typedef enum {False = 0, True = 1} tbool;
tbool EstPrefixe(char *pre, char *mot) {
    int i = 0;
    int n = strlen(mot);
    while (i < n) {
        if ((pre[0] == mot[i]) && (pre[1] == mot[i+1]))
            return True;
        i++;
    }
    return False;
}

/*int main() {
    int a = EstPrefixe("ch", "charlotte");
    printf("%d\n", a);
    return 0;
}*/

tbool BienParenthesee(char * expr) {
    int nbre_parentheses = 0;
    for (int i=0; i < strlen(expr); i++) {
        if (nbre_parentheses < 0)
            return False;
        if (expr[i] == '(')
            nbre_parentheses++;
        else
            nbre_parentheses -= 1;
    }
    if (nbre_parentheses == 0)
        return True;
    else
        return False;
}

/*int main() {
    char *expression = ")((";
    int a = BienParenthesee(expression);
    printf("%d\n", a);
}//*/

