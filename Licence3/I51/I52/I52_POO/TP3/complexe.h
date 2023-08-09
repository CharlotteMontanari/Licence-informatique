#ifndef _COMPLEXE_H
#define _COMPLEXE_H
#include <fstream>

class complexe {
    private:
        float re;
        float im;
    public:
        complexe(); //constructeur
        complexe(float, float); //constructeur
        complexe(const complexe &); //constructeur
        ~complexe();    //destructeur
        void afficher_complexe();
        complexe operator+(complexe);
        complexe operator-(complexe);
        complexe operator*(complexe);
        complexe operator/(complexe);
};

class VecteurComplexe {
    private:
        complexe *vecteur; //instance de la classe complexe
        unsigned short taille;
    public:
        VecteurComplexe(const complexe*, unsigned short);
        VecteurComplexe(std::ifstream&);
        ~VecteurComplexe();
        void afficher_vecteur();
};

#endif