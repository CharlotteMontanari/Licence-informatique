#include "polynome.h"
#include <iostream>

polynome::polynome() {
    deg = -1;
    coeff = NULL;
}

polynome::polynome(int a, float *b) {
    deg = a;
    coeff = new float[deg+1];
    for (int i=0; i<deg+1; i++)
        coeff[i] = b[i];
}

polynome::polynome(const polynome &a) {
    deg = a.deg;
    coeff = new float[deg+1];
    for (int i=0; i<deg+1; i++)
        coeff[i] = a.coeff[i];
}

polynome::~polynome() {
    std::cout << "Destruction" << std::endl;
}