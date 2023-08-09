#include "complexe.h"
#include <iostream>
#include <cmath>

//destructeur
complexe::~complexe() {
    std::cerr << "Erreur" << std::endl;
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

complexe somme(const complexe &x, const complexe &y) {
    float a = x.getRe() + y.getRe();
    float b = x.getIm() + y.getIm();
    return complexe(a, b);
}

complexe produit(const complexe &x, const complexe &y) {
    float a = (x.getRe() * y.getRe()) - (x.getIm() * y.getIm());
    float b = (x.getIm() * y.getRe()) + (x.getRe() * y.getIm());
    return complexe(a, b);
}

float cmodule(const complexe &x) {
    return sqrt(x.getRe() * x.getRe() + x.getIm() * x.getIm());
}

complexe conjugue(const complexe &x) {
    return complexe(x.getRe(), -x.getIm());
}


float complexe::getRe() const {   // partie reelle du complexe
    return re;
} 

float complexe::getIm() const {   // partie imaginaire du complexe
    return im;
} 

void complexe::Print() const {  // affichage sur stdout des valeurs du complexe
    std::cout << "re: " << re;
    std::cout << "im: " << im << std::endl;
} 

void complexe::Sum(const complexe &x) {   // ajout d'un complexe au complexe courant
    re = re + x.getRe();
    im = im + x.getIm();
} 

bool complexe::Identical(const complexe &x) {   // comparaison d'un complexe et du complexe courant
    return re == x.getRe() && im == x.getIm();
} 
