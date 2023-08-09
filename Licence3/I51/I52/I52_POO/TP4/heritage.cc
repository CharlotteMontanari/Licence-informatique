#include <iostream>
#include "heritage.h"

Personne::Personne(unsigned int age, std::string nom, std::string prenom) {
    this->age = age;
    this->nom = nom;
    this->prenom = prenom;
}

Personne::~Personne() {
    //std::cout << "Destruction" << std::endl;
}

void Personne::affichage() {
    std::cout << "Nom: " << nom << "\n";
    std::cout << "Prénom: " << prenom << "\n";
    std::cout << "Age: " << age << std::endl;
}

void Personne::vieillir() {
    age++;
}

Professeur::Professeur(unsigned int age, std::string nom, std::string prenom, unsigned int heure):
Personne(age, nom, prenom) {
    this->statut = "Professeur";
    this->heure = heure;
}

void Professeur::affichage() {
    Personne::affichage();
    std::cout << "Statut: " << statut << "\n";
    std::cout << "Heure: " << heure << std::endl;
}

void Professeur::travail(unsigned int heures) {
    this->heure += heures;
}

Etudiant1::Etudiant1(unsigned int age, std::string nom, std::string prenom, unsigned int nb):
Personne(age, nom, prenom) {
    this->nb = nb;
    this->notes = new unsigned int[this->nb];
    for (unsigned int i=0; i<this->nb; i++)
        this->notes[i] = 0;
}

/*Etudiant1::Etudiant1(const Etudiant1 &a):
Etudiant1(a) {}*/

Etudiant1::~Etudiant1() {
    delete [] this->notes;
}

void Etudiant1::ajouterNotes(unsigned int *tab) {
    for (unsigned int i=0; i<this->nb; i++)
        this->notes[i] = tab[i];
}

void Etudiant1::affichage() {
    Personne::affichage();
    std::cout << "Notes: ";
    std::cout << "| ";
    for (unsigned int i=0; i<this->nb; i++)
        std::cout << this->notes[i] << " | ";
    std::cout << "\n";
}

int Etudiant1::moyenne() {
    unsigned int somme = 0;
    for (unsigned int i=0; i<this->nb; i++)
        somme += this->notes[i];
    std::cout << "Moyenne: " << somme / this->nb << std::endl;
    return somme / this->nb;
}

//Etudiant1 Etudiant1::operator=(Etudiant1) {}

Matiere::Matiere() {
    this->nom = "";
    this->coeff = 0;
}

Matiere::Matiere(std::string nom, unsigned int coeff) {
    this->nom = nom;
    this->coeff = coeff;
}

void Matiere::affichage() {
    std::cout << "Matière: " << this->nom << "\n";
    std::cout << "Coefficient: " << this->coeff << std::endl;
}

std::string Matiere::getNom() {
    return this->nom;
}

unsigned int Matiere::getCoef() {
    return this->coeff;
}

Etudiant2::Etudiant2(unsigned int age, std::string nom, std::string prenom, unsigned int nb, Matiere *e): 
Etudiant1(age, nom, prenom, nb) {
    for (unsigned int i=0; i<this->nb; i++)
        this->m[i] = e[i];
    std::cout << "constructeur parametre" << std::endl;
}

/*Etudiant2::Etudiant2(const Etudiant2 &a):
Etudiant1(a) {}*/

Etudiant2::~Etudiant2() {
    delete [] this->m;
    std::cout << "destruction etud2" << std::endl;
}

void Etudiant2::affichage() {
    Personne::affichage();
    for (unsigned int i=0; i<this->nb; i++)
        std::cout << "À obtenu " << this->notes[i] << "en " << this->m[i].getNom() << std::endl;
}

unsigned int Etudiant2::moyenne() {
    int somme = 0;
    int somme_coeff;
    for (int i=0; i<this->nb;i++) {
        somme += this->notes[i] * this->m[i].getCoef();
        somme_coeff += this->m[i].getCoef();
    }
    return somme / somme_coeff;   
}

//Etudiant2 Etudiant2::operator=(Etudiant2) {}
