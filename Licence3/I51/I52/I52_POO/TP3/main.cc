#include <iostream>
#include <fstream>
#include "complexe.h"

int main() {
    /*unsigned short n = 3;
    complexe y[3];
    VecteurComplexe vc1(y, n);
    for (int i=0; i<n; i++)
        y[i].afficher();
    */
    std::ifstream file("test.txt");
    VecteurComplexe vc(file);
    vc.afficher_vecteur();
    return 0;
}