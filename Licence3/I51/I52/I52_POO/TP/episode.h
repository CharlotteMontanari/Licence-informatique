#ifndef _EPISODE
#define _EPISODE

#include "serie.h"
#include <iostream>

using namespace std;

class Episode : public Serie {
	private :
		string titreEpisode; //titre de l'épisode
		int numEpisode; //numéro de l'épisode
		int numSaison; //numéro de la saison
		float duree; // durée d'un épisode exprimé en minutes
	public :
	// Constructeurs
		Episode();
		Episode(string, bool, string, int, bool, string, int, int, float);
		Episode(const Episode &);

	//Polymorphisme
		bool shortcom();//comédie tournée sans public dont la durée d'un épisode inférieure à 10mn
		bool sitcom();//comédie tournée en public dont la durée d'un épisode est inférieure à 30 mn

	//surcharge de << 

	friend ostream &operator<<(ostream &, const Episode);

};

#endif
