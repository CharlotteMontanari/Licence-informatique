#include "serie.h"
#include "episode.h"
#include "saison.h"
#include <iostream>
using namespace std;

int main() {

	//test classe Serie
	cout<<endl<<"******** Test de la classe Serie ********"<<endl;

	Serie S;
	Serie GoT("Game of Thrones",false, "fantaisie médiévale",8,false); 
	Serie TdF(GoT);
	TdF.affiche();
	cout<<endl;
	Serie K("Kaamelott",true, "fantasy historique",6,false);
	K.affiche();
	cout<<endl<<"******** Fin de test de la classe Serie ********"<<endl;

	//test classe Episode

	cout<<endl<<"-------- Test de la classe Episode --------"<<endl; 

	Episode e;
	string bbt="Big Bang Theory";
	Episode BBTE1S1(bbt,true,"comédie scientifique",12,true,"La Nouvelle Voisine des surdoués",1,1,22);
	Episode BBTE2S1(bbt,true,"comédie scientifique",12,true,"Des voisins encombrants",2,1,22);
	Episode BBTE3S1(bbt,true,"comédie scientifique",12,true,"Le Corollaire de pattes-de-velours",3,1,22);
	Episode BBTE4S1(bbt,true,"comédie scientifique",12,true,"Les Poissons Luminescents",4,1,22);
	Episode BBTE5S1(bbt,true,"comédie scientifique",12,true,"Le Postulat du hamburger",5,1,22);
	Episode BBTE6S1(bbt,true,"comédie scientifique",12,true,"Les Allumés d'Halloween",6,1,22);
	Episode BBTE7S1(bbt,true,"comédie scientifique",12,true,"Le Paradoxe du ravioli chinois",7,1,22);

	Episode KE2L1("Kaamelott",true, "fantasy historique",6,false, "Les Tartes aux myrtilles",2,1,3.5);

	// test de sitcom()
	if (BBTE1S1.sitcom())
		cout<<BBTE1S1.Get_titreSerie()<< " est un sitcom en "<<BBTE1S1.Get_nbSaison()<< " saison(s)"<<endl;

	cout<<endl;

	// test de shortcom()
	if (KE2L1.shortcom())
		cout<<KE2L1.Get_titreSerie()<< " est un shortcom en "<<KE2L1.Get_nbSaison()<< " saison(s)"<<endl;


	//surcharge de << 
	cout<<endl<<BBTE1S1<<endl<<KE2L1<<endl;;



	Episode tab[6]={BBTE1S1,BBTE2S1,BBTE3S1,BBTE4S1,BBTE5S1,BBTE6S1};


	cout<<endl<<"-------- Fin de test de la classe Episode --------"<<endl; 

	//test classe Saison

	cout<<endl<<"******** Test de la classe Saison ********"<<endl;

	// tests des constructeurs de la classe Saison
	Saison debBBT(6,tab), S1(2), NS;

	// test de la surcharge de = 

	NS= debBBT;

	// test de la surcharge de + et =
	NS = NS + BBTE7S1;

	// test de la deuxième surcharge de +
	NS= KE2L1 + NS;

	//test de sitcom
	//Saison  BBT;

	//BBT=NS.sitcom();


	/*cout<<endl<<"Les episodes d'un sitcom "<< " : "<<endl;

	for(int i=0; i<BBT.get_nbEpisodes();i++)
		cout<<BBT[i]<<endl;	//on utilise ici la surcharge de l'opérateur []*/

	cout<<endl<<"-------- Fin de test de la classe Saison --------"<<endl;

	return 0;
}
