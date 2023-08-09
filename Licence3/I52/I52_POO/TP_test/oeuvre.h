#ifndef _OEUVRE_H
#define _OEUVRE_H

#include <string>
#include <iostream>
using namespace std;

class Oeuvre {
	private : 
		string titre;
		string artiste;
		int annee;
		string art;
	public:
	//Constructeur
		Oeuvre();
		Oeuvre(string, string, int, string);
		Oeuvre(const Oeuvre &);

	//accesseurs
		string get_titre()const;
		string get_artiste()const;
		int get_annee()const;
		string get_art()const;

	//methode
		void cartel()const;	 	
};
#endif
	 
