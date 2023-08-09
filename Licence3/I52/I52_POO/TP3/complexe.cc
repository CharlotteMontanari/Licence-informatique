#include "complexe.h"
#include <iostream>

complexe::~complexe() { //destructeur
    //std::cerr << "Destruction" << std::endl;
}

complexe::complexe() {  //constructeur
    re = 0;
    im = 0;
} 

complexe::complexe(float x, float y) {  //constructeur
    re = x;
    im = y;
}

complexe::complexe(const complexe &x) { //constructeur
    re = x.re;
    im = x.im;
} 

void complexe::afficher_complexe() {
    std::cout << "z = " << re << " + " << im << "i" << std::endl;
}

VecteurComplexe::VecteurComplexe(const complexe *a, unsigned short b) {
    vecteur = new complexe[b];
    taille = b;
    for (int i=0; i<taille; i++)
        vecteur[i] = a[i];
}

VecteurComplexe::VecteurComplexe(std::ifstream &afile) {
    float imaginaire, reel;
    afile >> taille;
    int i = 0;
    vecteur = new complexe[taille];
    while (!afile.eof()) {
        afile >> reel;
        afile >> imaginaire;
        complexe c(reel, imaginaire);
        vecteur[i] = c;
        i++;
    }
}

VecteurComplexe::~VecteurComplexe() {
    std::cerr << "Erreur" << std::endl;
}

void VecteurComplexe::afficher_vecteur() {
    for (int i=0; i<taille; i++)
        vecteur[i].afficher_complexe();
}

