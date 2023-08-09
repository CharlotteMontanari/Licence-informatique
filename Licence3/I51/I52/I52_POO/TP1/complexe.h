#include <iostream>

struct complexe {
    float re, im;
    unsigned int ident;
};

typedef complexe* ptComplexe;

void afficher(const complexe &);

complexe somme(const complexe &, const complexe &);

complexe produit(const complexe &, const complexe &);

float cmodule(const complexe &);

complexe conjugue(const complexe &);

void init(complexe &);

void affiche_adress(complexe &);

complexe bidon(complexe &);

void CreerComplexe(complexe **);

void CreerComplexe(ptComplexe &);

complexe* CreerComplexe();

complexe* CreerVecteurComplexes(unsigned int);