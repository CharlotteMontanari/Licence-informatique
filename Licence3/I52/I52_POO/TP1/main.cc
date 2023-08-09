#include "echangiste.h"
#include <iostream>
#include <new>

//main pour echangiste
/*int main() {
    float x = 2;
    float y = 3;
    permuter(x, y);
    std::cout << x << ", " << y << std::endl;
    return 0;
}*/

//main pour les complexes
/*int main() {
    complexe a;
    a.re = 2;
    a.im = 3;

    complexe b;
    b.re = 4;
    b.im = 5;

    complexe w = somme(a, b);
    afficher(w);

    std::cout << "****************" << std::endl;

    complexe x = produit(a, b);
    afficher(x);

    std::cout << "****************" << std::endl;

    float m = cmodule(a);
    std::cout << "cmodule: " << m << std::endl;

    std::cout << "****************" << std::endl;

    complexe v = conjugue(a);
    afficher(v);
    return 0;
}*/

int main() {
    static complexe x;
    complexe &z = x;
    complexe c = bidon(x);
    complexe *pc;
    complexe *pc2;
    ptComplexe pt;

    std::cout << "Static" << std::endl;
    affiche_adress(x);

    std::cout << "***************" << std::endl;

    std::cout << "Bidon" << std::endl;
    affiche_adress(z);

    std::cout << "***************" << std::endl;

    std::cout << "Static" << std::endl;
    affiche_adress(c);

    std::cout << "***************" << std::endl;

    std::cout << "Complexe **" << std::endl;
    CreerComplexe(&pc);
    afficher(*pc);

    std::cout << "***************" << std::endl;

    std::cout << "Complexe &" << std::endl;
    CreerComplexe(pt);
    afficher(*pt);

    std::cout << "***************" << std::endl;
    
    std::cout << "Complexe ()" << std::endl;
    pc2 = CreerComplexe();
    afficher(*pc2);
    return 0;
}