#ifndef _SERIE
#define _SERIE

#include <string>
#include <iostream>

using namespace std;

class Serie{
	private :
		string titreSerie;
		bool comedie;
		string genre;
		int nbSaison;
		bool enPublic;
	 
	public :
	// Constructeurs
		Serie();
		Serie(string,bool, string, int,bool);
		Serie(const Serie &);

	//Accesseurs
		string Get_titreSerie() const;
		int Get_nbSaison() const; 
		
	//Polymorphisme
		bool shortcom();//Série de genre comédie et tournée sans public
		bool sitcom();//Série de genre comédie et tournée avec un public
		
	//Méthode
		void affiche();
};

#endif
