#include "oeuvre.h"
#include "tableau.h"
#include "exposition.h"

int main () {
	////////// test classe Oeuvre
	Oeuvre o0;
	Oeuvre o1("Sagrada familia", "Antoni Gaudi", 1882,"Architecture"); 
	Oeuvre o2("Les trois grâces", "Niki de Saint Phalle", 1999,"Sculpture");
	Oeuvre o3(o2);

	cout<< "Test de cartel pour la classe Oeuvre"<<endl;
	o1.cartel();
	o3.cartel();
	cout<<endl<<endl;

	//////////// test de la classe Tableau
	cout<<"Test de la classe Tableau"<<endl<<endl;

	Tableau t1("Guernica","Pablo Picasso",1937, 349, 777,"Huile sur toile",true );
	Tableau t2("La liberté guidant le peuble","Eugène Delacroix", 1930, 260, 325,"Huile sur toile", true);
	Tableau t3("Femme au chapeau", "Henri Matisse", 1905, 81,60, "huile sur toile", true);
	Tableau t4("les deux Frida", "Frida kalho",1939, 175,175.5,"huile sur toile",true );
	Tableau t5("La machine à gazouiller", "Paul Klee", 1922,41 , 30.6,"huile et aquarelle", true);

	cout<<"Test de la surcharge de cartel"<<endl;
	t1.cartel();

	cout<<"Surcharge de << pour la classe "<<endl<<t2<<endl<<endl;
	// Test de la surcharge de >
	cout<<"Surcharge de >"<<endl;
	if (t3>t4)
		cout<<t3.get_titre() << " est plus grand que "<<t4.get_titre()<<endl;
	else
		cout<<t3.get_titre() << " est plus petit que "<<t4.get_titre()<<endl;

	//////////// test de la classe exposition
	Tableau toiles[4]={t1,t2,t3,t4};
	Exposition monExpo(toiles,4), tonExpo(2), sonExpo(monExpo);

	//Surcharges = et +
	cout<< "Surcharge de = "<<endl;

	tonExpo = monExpo;

	cout<< "Surcharge de + "<<endl;

	sonExpo = tonExpo + t5 ;

	for (int i=0;i<5;i++)
		cout<<sonExpo[i]<<endl;

	cout<<"Le plus grand tableau de l'exposition :" <<endl<<sonExpo.GrandFormat()<<endl;

	return 0;
}
