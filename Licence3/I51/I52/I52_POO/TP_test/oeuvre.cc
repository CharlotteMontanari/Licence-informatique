#include "oeuvre.h"

/*
string titre;
string artiste;
int annee;
string art;*/

Oeuvre::Oeuvre() {
    this->titre = "";
    this->artiste = "";
    this->annee = 0;
    this->art = "";
}

Oeuvre::Oeuvre(string titre, string artiste, int annee, string art) {
    this->titre = titre;
    this->artiste = artiste;
    this->annee = annee;
    this->art = art;
}

Oeuvre::Oeuvre(const Oeuvre &o) {
    this->titre = o.titre;
    this->artiste = o.artiste;
    this->annee = o.annee;
    this->art = o.art;
}

string Oeuvre::get_titre()const {
    return this->titre;
}

string Oeuvre::get_artiste()const {
    return this->artiste;
}

int Oeuvre::get_annee()const {
    return this->annee;
}

string Oeuvre::get_art()const {
    return this->art;
}

void Oeuvre::cartel()const {
    cout << "Titre: " << this->titre << "\n";
    cout << "Artiste: " << this->artiste << "\n";
    cout << "Année: " << this->annee << "\n";
    cout << "Art: " << this->art << endl;
}
