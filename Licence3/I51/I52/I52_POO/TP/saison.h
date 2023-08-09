#ifndef _SAISON
#define _SAISON

#include "episode.h"

class Saison {
	private :
		int nbEpisodes;
		Episode * liste;
	public:
	//Constructeurs
		Saison();
		Saison(int);//construction d'une instance dont le nombre d'épisodes est fourni en argument
		Saison(int , Episode*);
		Saison(const Saison &);
	//Destructeur
		~Saison();

	//Accesseurs
		int get_nbEpisodes(){return nbEpisodes;};

	//surcharge de l'opérateur =
		Saison operator=(const Saison &);

	// Surcharge de l'opérateur + : saison + episode
		Saison operator+(const Episode &)const;

	// Surcharge de l'opérateur + : episode + saison
		friend Saison operator+(const Episode &, Saison &);

	// Surcharge de l'opérateur []
		Episode operator[](int i){return liste[i];};// retourne l'épisode de rang i dans la liste des épisodes.

	//Méthode
		//Saison sitcom();// retourne une instance de Saison qui contient une saison d'un sitcom  
		
};

#endif
