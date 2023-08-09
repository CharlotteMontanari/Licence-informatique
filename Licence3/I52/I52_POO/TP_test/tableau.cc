#include "tableau.h"

/*
float hauteur;
float largeur;
string technique;	
bool expose;*/

Tableau::Tableau() {
    this->hauteur = 0.0;
    this->largeur = 0.0;
    this->technique = "";
    this->expose = true;
}

Tableau::Tableau(string titre, string artiste, int annee, float hauteur, float largeur, string technique, bool expose):
Oeuvre(titre, artiste, annee, "Peinture") {
    this->hauteur = hauteur;
    this->largeur = largeur;
    this->technique = technique;
    this->expose = expose;
}

Tableau::Tableau(const Tableau &t) {
    this->hauteur = t.hauteur;
    this->largeur = t.largeur;
    this->technique = t.technique;
    this->expose = t.expose;
}

void Tableau::cartel()const {
    Oeuvre::cartel();
    cout << "Hauteur: " << this->hauteur << "\n";
    cout << "Largeur: " << this->largeur << "\n";
    cout << "Technique: " << this->technique << endl;
}

//surcharge de l'opérateur <<
ostream &operator<<(ostream &o, Tableau t) {
    o << "Titre: " << t.get_titre() << "\n";
    o << "Artiste: " << t.get_artiste() << "\n";
    o << "Année: " << t.get_annee() << "\n";
    if (t.expose)
        o << "Expose = True" << endl;
    else
        o << "Expose = False" << endl;
    return o;
}

//Surcharge de >
bool Tableau::operator>(Tableau &t) {
    return ((this->hauteur * this->largeur) > (t.hauteur * t.largeur));
}
