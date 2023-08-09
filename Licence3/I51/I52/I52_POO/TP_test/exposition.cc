#include "exposition.h"
#include "tableau.h"

/*
Tableau* salle;
int nb;*/

Exposition::Exposition() {
    this->nb = 0;
    this->salle = nullptr;
}

Exposition::Exposition(Tableau* salle, int nb) {
    this->nb = nb;
    this->salle = new Tableau[nb];
    for (int i=0; i<this->nb; i++)
        this->salle[i] = salle[i];
}

Exposition::Exposition(int nb) {
    this->nb = nb;
    this->salle = new Tableau[nb];
}

Exposition::Exposition(const Exposition &e) {
    this->nb = e.nb;
    this->salle = new Tableau[nb];
    for (int i=0; i<this->nb; i++)
        this->salle[i] = e.salle[i];
}

Exposition::~Exposition() {
    delete [] this->salle;
}

//Surcharge de l'opérateur =
Exposition &Exposition::operator=(const Exposition &e) {
    if (this != &e) {
        this->nb = e.nb;
        delete [] this->salle;
        this->salle = new Tableau[nb];
        for (int i=0; i<this->nb; i++)
            this->salle[i] = e.salle[i];
    }
    return *this;
}

//Surcharge de +
Exposition Exposition::operator+(const Tableau &t)const {
    Exposition ex(nb + 1);
    for (int i=0; i<this->nb; i++)
        ex.salle[i] = this->salle[i];
    ex.salle[this->nb] = t;
    return ex;
}

//Surcharge de l'opérateur [] : retourne le Tableau de rang i de la salle 
Tableau &Exposition::operator[](int i)const {
    return salle[i];
}

Tableau Exposition::GrandFormat()const {
    Tableau max;
    for (int i=0; i<nb; i++) {
        if (salle[i] > max)
            max = salle[i];
    }
    return max;
}
