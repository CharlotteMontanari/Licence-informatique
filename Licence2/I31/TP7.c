#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct date date;
struct date {
    unsigned int jour;
    unsigned int mois;
    unsigned int annee;
};

date saisie_date() {
    date d;
    printf("Saisir une date: ");
    scanf("%u %u %u", &d.jour, &d.mois, &d.annee);
    return d;
}

void affiche_date(date d) {
    printf("%u/%u/%u\n", d.jour, d.mois, d.annee);
}

int date_compare(date d1, date d2) {
    if (d1.jour > d2.jour)
        return 1;
    else if (d1.jour < d2.jour)
        return -1;
    return 0;

    if (d1.mois > d2.mois)
        return 1;
    else if (d1.mois < d2.mois)
        return -1;
    return 0;

    if (d1.annee > d2.annee)
        return 1;
    else if (d1.annee < d2.annee)
        return -1;
    return 0;
}

/*int main() {
    date d1 = saisie_date();
    date d2 = saisie_date();
    int x = date_compare(d1, d2);
    printf("%d\n", x);
    return 0;
}*/

typedef struct personne personne;
struct personne {
    char *nom;
    char *prenom;
    date date_naissance;
    date date_deces;
};

personne* saisie_personne() {
    personne *p = (personne *)malloc(sizeof(personne));
    p->prenom = (char*)malloc(sizeof(char));
    p->nom = (char*)malloc(sizeof(char));
    printf("Saisir un nom: ");
    scanf("%s", p->nom);

    printf("Saisir un prenom: ");
    scanf("%s", p->prenom);
    
    printf("Saisir une date de naissance: ");
    p->date_naissance = saisie_date();

    printf("Saisir une date de deces: ");
    p->date_deces = saisie_date();
    return p;
}

void affiche_personne(personne* p) {
    printf("%s\n", p->nom);
    printf("%s\n", p->prenom);
    printf("%u/%u/%u--", p->date_naissance.jour, p->date_naissance.mois, p->date_naissance.annee);
    printf("%u/%u/%u\n", p->date_deces.jour, p->date_deces.mois, p->date_deces.annee);
}

//retourne 1 si p1 = p2 cad meme nom, prenom, date de naissance
int meme_personne(personne* p1, personne* p2) {
    if (strcmp(p1->nom, p2->nom) == 0 && 
        strcmp(p1->prenom, p2->prenom) == 0 && 
        p1->date_naissance.jour == p2->date_naissance.jour &&
        p1->date_naissance.mois == p2->date_naissance.mois &&
        p1->date_naissance.annee == p2->date_naissance.annee)
        return 1;
    return 0;
}


/*int main() {
    personne *p = saisie_personne();
    affiche_personne(p);
    personne *a = saisie_personne();
    personne *b = saisie_personne();
    int x = meme_personne(a, b);
    printf("%d\n", x);
}*/

typedef struct membre_famille membre_famille;
struct membre_famille {
    personne *individu;
    membre_famille *pere;
    membre_famille *mere;
};

membre_famille* nouveau_membre(personne* i, membre_famille* p, membre_famille* m) {
    membre_famille *mf = (membre_famille*)malloc(sizeof(membre_famille));
    mf->individu = i;
    mf->pere = p;
    mf->mere = m;
    return mf;
}

typedef struct arbre arbre;
struct arbre {
    membre_famille *root;
};

arbre* nouvel_arbre(membre_famille* m) {
    arbre *a = (arbre*)malloc(sizeof(arbre));
    a->root = m;
    return a;
}

void detruire_famille(membre_famille *f) {
    if (f == NULL)
        return;
    if (f->pere != NULL)
        detruire_famille(f->pere);
    if (f->mere != NULL)
        detruire_famille(f->mere);
    free(f);
}

void detruire_arbre(arbre* a) {
    if (a == NULL || a->root == NULL)
        return;
    detruire_famille(a->root->pere);
    detruire_famille(a->root->mere);
    free(a->root);
}

//affecte p comme pere de m, retourne 1 si réussi, 0 sinon
int affecte_pere(membre_famille* c, membre_famille* p) {
    if (c == NULL || p == NULL || c->pere != NULL)
        return 0;
    c->pere = p;
    return 1;
}

int affecte_mere(membre_famille* c, membre_famille* m) {
    if (c == NULL || m == NULL || c->mere != NULL)
        return 0;
    c->mere = m;
    return 1;
}

/*int main() {
    membre_famille *in = nouveau_membre(saisie_personne(), NULL, NULL);
    arbre *tree = nouvel_arbre(in);

    membre_famille* p = nouveau_membre(saisie_personne(),NULL,NULL);
    membre_famille *m =  nouveau_membre(saisie_personne(),NULL,NULL);

    int x = affecte_pere(in, p);
    int y = affecte_mere(in, m);

    affiche_personne(p->individu);
    affiche_personne(m->individu);
}*/

membre_famille* rechercher(arbre *a, char *nom, char *prenom) {
    if (a == NULL || a->root == NULL)
        return NULL;
    membre_famille *racine = a -> root;
    if ((strcmp(racine->individu->nom, nom) == 0) && (strcmp(racine->individu->prenom, prenom)) == 0)
        return racine;
}

unsigned int countMembre(membre_famille* r) {
    if (r == NULL) 
        return 0;
    return 1 + countMembre(r->pere) + countNodes(r->mere);
}

membre_famille* ancetre_paternel(arbre* a) {
    if (a == NULL)
        return NULL;
    int l = ancetre_paternel(a->root->pere);
    int r = ancetre_paternel(a->root->mere);
    if (l > r)
        return l+1;
    return r+1;
}