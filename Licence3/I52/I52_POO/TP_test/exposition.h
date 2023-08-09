#ifndef _EXPOSITION_H
#define _EXPOSITION_H
#include "tableau.h"

class Exposition  {
	private :
		Tableau* salle;
		int nb;
	public:
		//constructeurs
		Exposition();
		Exposition(Tableau*, int);
		Exposition(int);
		Exposition(const Exposition &);
		~Exposition();
		//Surcharge de l'opérateur =
		Exposition &operator=(const Exposition &);
		//Surcharge de +
		Exposition operator+(const Tableau &)const;
		//Surcharge de l'opérateur [] : retourne le Tableau de rang i de la salle 
		Tableau &operator[](int)const;
		// Methode GrandFormat retourne le tableau de plus grande surface 
		Tableau GrandFormat()const;
};

#endif
