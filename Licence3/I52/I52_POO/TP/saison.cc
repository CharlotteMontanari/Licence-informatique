#include "saison.h"

/*
int nbEpisodes;
Episode * liste; */

Saison::Saison() {
	this->nbEpisodes = 0;
	this->liste = new Episode[nbEpisodes];
}

Saison::Saison(int nbEpisodes) {
	this->nbEpisodes = nbEpisodes;
	this->liste = new Episode[nbEpisodes];
}

Saison::Saison(int nbEpisodes, Episode *liste) {
	this->nbEpisodes = nbEpisodes;
	this->liste = new Episode[nbEpisodes];
	for (int i=0; i<this->nbEpisodes; i++)
		this->liste[i] = liste[i];
}

Saison::Saison(const Saison &s) {
	this->nbEpisodes = s.nbEpisodes;
	this->liste = new Episode[nbEpisodes];
	for (int i=0; i<this->nbEpisodes; i++)
		this->liste[i] = s.liste[i];
}

Saison::~Saison() {
	delete [] liste;
}

//surcharge de l'opérateur =
Saison Saison::operator=(const Saison &s) {
	if (this != &s) {
		this->nbEpisodes = s.nbEpisodes;
		delete [] this->liste;
		this->liste = new Episode[nbEpisodes];
		for (int i=0; i<this->nbEpisodes; i++)
			liste[i] = s.liste[i];
	}
	return *this;
}

// Surcharge de l'opérateur + : episode + saison
Saison Saison::operator+(const Episode &e)const {
	Saison sa(nbEpisodes + 1);
	for (int i=0; i<this->nbEpisodes; i++)
		sa.liste[i] = liste[i];
	sa.liste[nbEpisodes] = e;
	return sa;
}

// Surcharge de l'opérateur + : saison + episode
Saison operator+(const Episode &a, Saison &s) {
	Saison sa(s.nbEpisodes + 1);
	for (int i=0; i<s.nbEpisodes; i++)
		sa.liste[i] = s.liste[i];
	sa.liste[s.nbEpisodes] = a;
	return sa;
}

//Saison Saison::sitcom() {} //je n'ai pas compris ce que faisait cette fonction
