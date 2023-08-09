#include "compregex.h"

///////////////
////GLOBAL////
char *expr; //expr contient une expression reguliere, ex: a.(a+a+b)
char *postfix;  //liste qui contient expr en postfixe
int indice = 0; //indice permet d'avancer dans expr
int i = 0; //i permet d'avancer dans postfix
/////////////

int E() {
    return T() && R();
}

int T() {
    return F() && P();
}

int F() {
    return G() && X();
}

int R() {
    if (expr[indice] == '+') {
        indice++;
        if (T()) {
            postfix[i] = '+';
            i++;
            return R();
        }  
        return 0;
    }
    return 1;
}

int P() {
    if (expr[indice] == '.') {
        indice++;
        if (F()) {
            postfix[i] = '.';
            i++;
            return P();
        }
            
        return 0;
    }
    return 1;
}

int G() {
    if (expr[indice] == '(') {
        indice++;
        if (E()) {
            if (expr[indice] == ')') {
                indice++;
                return 1;
            }
        }
    }
    else if (expr[indice] > 96 && expr[indice] < 123) {
        postfix[i] = expr[indice];
        i++;
        indice++;
        return 1;
    }
    return 0;
}

int X() {
    if (expr[indice] == '*') {
        indice++;
        postfix[i] = expr[indice-1];
        i++;
        return X();
            
    }
    return 1;
}

char *parseur(char *chaine) {
    expr = chaine;  //on recupere la chaine dans expr
    int taille = strlen(expr);
    postfix = malloc(sizeof(char) * taille);    //on alloue postfix de la longueur de expr
    if (E() && indice == taille) {  //on verifie que notre analyse est correct et qu'on soit arrivé au bout de la liste
        printf("Expression régulière acceptée\n");  //dans ce cas, l'expression reguliere est accepté
        return postfix;
    }
    printf("Expression régulière non acceptée\n");  //sinon, elle ne l'ai pas
    free(postfix);
    return NULL;
}
