#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//Structures

typedef struct {
    unsigned int numero_rue;
    char* nom_voie;
    unsigned int code_postal;
    char* ville;
}adresse;

typedef struct {
    char* nom;
    char* prenom;
    unsigned short age;
    adresse* adresse_postale;
}personne;

/*int main() {
    personne perso = {"Montanari", "Charlotte", 19};
    printf("Nom: %s\nPrenom: %s\nAge: %hu\n\n", perso.nom, perso.prenom, perso.age);

    adresse adr = {12, "Avenue de la Resistance", 83200, "Toulon"};
    printf("Numero rue: %u\nNom voie: %s\nCode postal: %u\nVille: %s\n\n",
            adr.numero_rue, adr.nom_voie, adr.code_postal, adr.ville);
    return 0;
}*/

adresse* lireAdresse(void) {
    adresse* a = (adresse*)malloc(sizeof(adresse));
    a -> nom_voie = (char*)malloc(255*sizeof(char));
    a -> ville = (char*)malloc(255*sizeof(char));

    printf("Numero rue/Nom voie/code postal/ville\n");
    scanf("%u %s %u %s", &(a->numero_rue), a->nom_voie, &(a->code_postal), a->ville);
    return a;
}

personne* lirePersonne(void) {
    personne* p = (personne*)malloc(sizeof(personne));
    p -> nom = (char*)malloc(255*sizeof(char));
    p -> prenom = (char*)malloc(255*sizeof(char));

    printf("Nom/Prenom/Age\n");
    scanf("%s %s %hu", p->nom, p->prenom, &(p->age));
    p -> adresse_postale = lireAdresse();
    return p;
}

/*int main() {
    personne* perso = lirePersonne();
    printf("Nom: %s\n", perso->nom);
    printf("Prenom: %s\n", perso->prenom);
    printf("Age: %hu\n", perso->age);

    adresse* adr = lireAdresse();
    printf("Num rue: %u\n", adr->numero_rue);
    printf("Nom voie: %s\n", adr->nom_voie);
    printf("Code postal: %u\n", adr->code_postal);
    printf("Ville: %s\n", adr->ville);

    return 0;
}*/

int ecrireAdresse(adresse* a) {
    printf("%u %s %u %s", a->numero_rue, a->nom_voie, a->code_postal, a->ville);
    return 0;
}

int ecrirePersonne(personne* p) {
    printf("%s %s %hu ", p->nom, p->prenom, p->age);
    printf("%u %s %u %s\n", p->adresse_postale->numero_rue, p->adresse_postale->nom_voie, 
                            p->adresse_postale->code_postal, p->adresse_postale->ville);

    return 0;
}

/*int main() {
    personne* perso = lirePersonne();
    ecrirePersonne(perso);
}*/

int memeAdresse(personne* a, personne* b) {
    if ((a->adresse_postale->numero_rue) == (b->adresse_postale->numero_rue) 
    && (strcmp((a->adresse_postale->nom_voie), (b->adresse_postale->nom_voie))) == 0
    && (a->adresse_postale->code_postal) == (b->adresse_postale->code_postal)
    && (strcmp((a->adresse_postale->ville), (b->adresse_postale->ville))) == 0)
        return 1;
    return 0;
}

/*int main() {
    personne* perso1 = lirePersonne();
    personne* perso2 = lirePersonne();
    int a = memeAdresse(perso1, perso2);
    printf("%d\n", a);
    return 0;
}*/

//Listes chainees

typedef struct {
    personne* perso;
    voisin* gauche;
    voisin* droite;
}voisin;

typedef struct {
    voisin* droite;
    voisin* gauche;
}rue;

rue* population(void) {
    int dem_voisin = 1;
    voisin* ancien = NULL;
    voisin* new;
    
    while (dem_voisin == 1) {
        printf("Voulez vous ajouter du voisinage ?");
        scanf("%d", &dem_voisin);
        
    }
    return printf("Fin du voisinage");
    
}