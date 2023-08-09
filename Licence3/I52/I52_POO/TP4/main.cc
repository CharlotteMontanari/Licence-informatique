#include <iostream>
#include "heritage.h"
#include <string>

int main () {
    //Personne
    unsigned int a = 20;
    std::string b = "Montanari";
    std::string c = "Charlotte";
    Personne p1(a, b, c);
    //p1.affichage();
    //std::cout << "****************" << std::endl;
    //p1.vieillir();
    //p1.affichage();

    //Professeur
    unsigned int h = 35;
    unsigned int h2 = 10;
    Professeur p2(a, b, c, h);
    /*p2.affichage();
    std::cout << "****************" << std::endl;
    p2.travail(h2);
    p2.affichage();*/

    //Etudiant1
    unsigned int n = 10;
    unsigned int notes1[] = {12, 14, 7, 8, 3, 16, 17, 20, 10, 15};
    Etudiant1 e1(a, b, c, n);
    /*e1.ajouterNotes(notes1);
    e1.affichage();
    e1.moyenne();
    //faire surcharge operateur =*/

    unsigned int nbre = 4;
    Matiere m[4] = {Matiere("Français", 3), Matiere("Math", 9), Matiere("Histoire", 5), Matiere("Sport", 2)};
    Etudiant2 e2(a, b, c, nbre, m);
    e2.affichage();
}