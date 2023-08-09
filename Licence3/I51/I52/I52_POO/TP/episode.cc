#include "episode.h"

/*
string titreEpisode; 
int numEpisode; 
int numSaison; 
float duree; */

Episode::Episode():
Serie() {
	this->titreEpisode = "";
	this->numEpisode = 0;
	this->numSaison = 0;
	this->duree = 0.0;
}

Episode::Episode(string titreSerie, bool comedie, string genre, int nbSaison, bool enPublic, string titreEpisode, int numEpisode, int numSaison, float duree):
Serie(titreSerie, comedie, genre, nbSaison, enPublic) {
	this->titreEpisode = titreEpisode;
	this->numEpisode = numEpisode;
	this->numSaison = numSaison;
	this->duree = duree;
}

Episode::Episode(const Episode &e):
Serie(e) {
	this->titreEpisode = e.titreEpisode;
	this->numEpisode = e.numEpisode;
	this->numSaison = e.numSaison;
	this->duree = e.duree;
}

bool Episode::shortcom() { //comédie tournée sans public dont la durée d'un épisode inférieure à 10mn
	if (Serie::shortcom() and this->duree < 10)
		return true;
	else
		return false;
}

bool Episode::sitcom() { //comédie tournée en public dont la durée d'un épisode est inférieure à 30 mn
	if (Serie::sitcom() and this->duree < 30)
		return true;
	else
		return false;
}

ostream &operator<<(ostream &o, const Episode e) {
	o << "Titre de la série: " << e.Get_titreSerie() << endl;
	o << "Numéro de la saison: " << e.numSaison << endl;
	o << "Episode " << e.numEpisode << ", de l'épisode " << e.titreEpisode << endl;
	return o;
}
