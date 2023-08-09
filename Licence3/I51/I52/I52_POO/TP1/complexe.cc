#include <cmath>
#include <ctime>
#include "complexe.h"

void afficher(const complexe &a) {
    std::cout << "Réel: " << a.re << "\n";
    std::cout << "Imaginaire: " << a.im << "\n";
    std::cout << "Ident: " << a.ident << std::endl;
}

complexe somme(const complexe &x, const complexe &y) {
    complexe z;
    z.re = x.re + y.re;
    z.im = x.im + y.im;
    return z;
}

complexe produit(const complexe &x, const complexe &y) {
    complexe z;
    z.re = (x.re * y.re) - (x.im * y.im);
    z.im = (x.im * y.re) + (x.re * y.im);
    return z;
}

float cmodule(const complexe &x) {
    return sqrt(x.re*x.re + x.im*x.im);
}

complexe conjugue(const complexe &x) {
    complexe z;
    z.re = x.re;
    z.im = -1 * x.im;
    return z;
}

void init(complexe &c) {
    static int i = 0;
    c.ident = i++;
    c.re = 0;   //a
    c.im = 0;   //b
}

void affiche_adress(complexe &x) {
    std::cout << "adresse x: " << &x << '\n';
    std::cout << "adresse x.re: " << &x.re << '\n';
    std::cout << "adresse x.im: " << &x.im << '\n';
    std::cout << "adresse x.ident: " << &x.ident << std::endl;
}

complexe bidon(complexe &c) {
    complexe aux;
    std::cout << &aux << &c.re << std::endl;
    std::cout << &aux << &c.im << std::endl;
    std::cout << &aux << &c.ident << std::endl;
    return aux;
}

void CreerComplexe(complexe **x) {
    *x = new complexe; 
    init(**x);
}

void CreerComplexe(ptComplexe &pc) {
    pc = new complexe;
    init(*pc);
}

complexe* CreerComplexe() {
    complexe *pc = new complexe;
    init(*pc);
    return pc;
}

complexe* CreerVecteurComplexes(unsigned int vec) {
    return NULL;
}