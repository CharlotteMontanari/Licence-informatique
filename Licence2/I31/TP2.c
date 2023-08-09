#include <stdio.h>
#include <math.h>

/*int main() {
    char op;
    int a, b;

    printf("Choisir a, op, b: ");
    scanf("%d %c %d", &a, &op, &b);

    switch(op) {
        case '+': 
            printf("%d %c %d = %d\n", a, op, b, a+b);
            break;
        case '-': 
            printf("%d %c %d = %d\n", a, op, b, a-b);
            break;
        case '*': 
            printf("%d %c %d = %d\n", a, op, b, a*b);
            break;
        case '/': 
            printf("%d %c %d = %d\n", a, op, b, a/b);
            break;
        case '%': 
            printf("%d %c %d = %d\n", a, op, b, a%b);
            break;
        default:
            printf("Rien n'a été saisie");
    }
} */

/*int main() {
    int i = 1;
    int nbre;

    printf("Saisir un nbre: ");
    scanf("%d", &nbre);

    while (i * i < nbre) {
        i++;
    }
    printf("Le plus petit carré supérieur à %d est %d\n", nbre, i * i);
        return 0;
} */

/*int main() {
    int nbre;
    int i = 0;

    printf("Saisir un nbre: ");
    scanf("%d", &nbre);
    int valeur = nbre;

    do {
        nbre = nbre / 10;
        i++;
    } while (nbre != 0);
        printf("Le nbre de chiffre qui compose %d est %d\n", valeur, i);
    
} */

/*int main() {
    int n, i = 1, somme = 0; 

    printf("Saisir un nbre: ");
    scanf("%d", &n);

    for (i = 1; i<=n; i++) {
        somme = somme + i*i;
    }
    printf("La somme de i a n est %d\n", somme);
} */

/*int main() {
    int i = 0, n, note = 0, somme = 0;

    printf("Saisir le nbre de copie: ");
    scanf("%d", &n);

    while (i < n) {
        printf("Saisir une note: ");
        scanf("%d", &note);
        somme += note;
        i++;
    }
    printf("La moyenne de toutes les notes est %d\n", somme / i);
} */

/*void main(){
    int n,cpt = 0;
    float moy = 0, var = 0;

    printf("Combien de valeur voulez-vous saisir :");
    scanf("%d",&n);

    int *t;
    t = (int*)malloc(sizeof(int)*n);

    while(cpt<n)
    {
        scanf("%d", &t[cpt]);
        moy += t[cpt];
        cpt++;
    }

    moy = moy/n;
    printf("La moyenne est égal à %f\n", moy);

    cpt = 0;
    while(cpt<n)
    {
        var += (t[cpt]-moy)*(t[cpt]-moy);
        cpt++;
    }

    var = var/n;
    printf("La variance empirique est égal %f\n",var);
}*/

/*int factorielle(n) {
    int i = 2;
    int fact = 1;
    for (i = 2; i <= n; i++) {
        fact = i * fact;
    }
    return fact;
}*/

/*int power(int x, int n) {
    int p = 1;
    while (n != 0) {
        if (n % 2 == 1)
            p = p * x;
        x = x * x;
        n = n / 2;
    }
    return p;
}*/

/*float coef(int n, int k) {
    return (factorielle(n) / ((factorielle(k)) * (factorielle(n - k))));
}*/

/*int main() {
    int k = 0, n, y, x, somme = 0;

    printf("Saisir n, y, x: ");
    scanf("%d %d %d", &x, &y, &n);

    while (k <= n) {
        somme += coef(n, k) * (power(x, n-k) * power(y, k));
        k++;
    }
    printf("La somme de la formule de Newton est %d\n", somme);
} */
