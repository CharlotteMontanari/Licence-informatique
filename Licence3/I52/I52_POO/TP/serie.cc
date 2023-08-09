#include "serie.h"

/*
string titreSerie;
bool comedie;
string genre;
int nbSaison;
bool enPublic; */

Serie::Serie() {
	this->titreSerie = "";
	this->comedie = true;
	this->genre = "";
	this->nbSaison = 0;
	this->enPublic = true;
}

Serie::Serie(string titreSerie, bool comedie, string genre, int nbSaison, bool enPublic) {
	this->titreSerie = titreSerie;
	this->comedie = comedie;
	this->genre = genre;
	this->nbSaison = nbSaison;
	this->enPublic = enPublic;
}

Serie::Serie(const Serie &s) {
	this->titreSerie = s.titreSerie;
	this->comedie = s.comedie;
	this->genre = s.genre;
	this->nbSaison = s.nbSaison;
	this->enPublic = s.enPublic;
}

string Serie::Get_titreSerie() const {
	return this->titreSerie;
}

int Serie::Get_nbSaison() const {
	return this->nbSaison;
}

bool Serie::shortcom() { //Série de genre comédie et tournée sans public 
	if (this->comedie == true and this->enPublic == false)
		return true;
	else
		return false;
}	

bool Serie::sitcom() { //Série de genre comédie et tournée avec un public 
	if (this->comedie == true and this->enPublic == true)
		return true;
	else
		return false;
}	

void Serie::affiche() {
	if (sitcom())
		cout << "Titre de la série comédie tournée en public: " << this->titreSerie << endl;
	else if (shortcom())
		cout << "Titre de la série comédie tournée sans public: " << this->titreSerie << endl;
	cout << "Genre: " << this->genre << endl;
	cout << "Nombres de saisons: " << this->nbSaison << endl;
}










































