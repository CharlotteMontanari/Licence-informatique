#ifndef ADHERENT_H
#define ADHERENT_H
#include <string>
#include <iostream>
using namespace std;

class Adherent
{
private:
    string identite;
    int point;

public:
    Adherent();
    Adherent(string, int);
    int get_point();
    void mod_point(int);
    friend ostream &operator<<(ostream &, Adherent);
};

#endif

Adherent::Adherent(string id, int pt)
{
    this->identite = id;
    this->point = pt;
}

void Adherent::mod_point(int pt)
{
    this->point = pt;
}

ostream &operator<<(ostream &o, Adherent a)
{
    o << "L'adherent a1 d'indentité " << a.identite << " a " << a.point << " points." << endl;
}

// Exercice 2

class Club
{
private:
    string nom;
    string categorie;

public:
    Club();
    Club(string, string);
    void affiche();
};

Club::Club(string n, string c)
{
    this->nom = n;
    this->categorie = c;
}

// Exercice 3

class ClubAd : public Club
{
private:
    int nb;
    Adherent *tab;

public:
    ClubAd();
    ClubAd(string, string, int, Adherent *);
    ClubAd(const ClubAd &);
    ~ClubAd();
    ClubAd &operator=(const ClubAd &);
    void affiche();
    void CalculCat();
    Adherent &Meilleur();
};

ClubAd::ClubAd(string nom, string categorie, int nb, Adherent *tab) : Club(nom, categorie)
{
    this->nb = nb;
    this->tab = new Adherent[this->nb];
    for (int i = 0; i < this->nb; i++)
        this->tab[i] = tab[i];
}

ClubAd& ClubAd::operator=(const ClubAd &c)
{
    if (this != &c)
    {
        delete[] this->tab;
        this->nb = c.nb;
        this->tab = new Adherent[this->nb];
        for (int i = 0; i < this->nb; i++)
            this->tab[i] = c.tab[i];
    }
    return *this;
}

//une méthode CalculCat qui calcule la moyenne des points des joueurs du club
//et met a jour la catégorie du club en lui attribuant la valeur " A'
//si la moyenne est strictement supérieure à 100, "B" si elle est comprise entre 50 (exclus) et 100 (inclus)
//et "C' si elle est inférieure ou égale à 50.
void ClubAd::CalculCat()
{
    int moyenne = 0;
    for (int i = 0; i < this->nb; i++)
        moyenne += this->tab[i].get_point();

    moyenne /= this->nb;
    if (moyenne > 100)
        this->categorie = "A";
    else if (50 < moyenne <= 100)
        this->categorie = "B";
    else if (moyenne <= 50)
        this->categorie = "C";
}

//une méthode Meilleur qui retourne une référence sur l'adhérent (du club)
//qui a le plus de points lorsque le club a des adhérents.
Adherent &ClubAd::Meilleur()
{
    if (this->tab != NULL)
    {
        Adherent meilleur = this->tab[0];
        for (int i = 0; i < this->nb; i++)
        {
            if (this->tab[i].get_point() > meilleur.get_point())
                meilleur = this->tab[i];
        }
        return meilleur;
    }
    Adherent rien;
    return rien;
}

int main()
{
    Adherent a1("Toto", 30), a2("Tata", 80);
    Adherent tab[2] = {a1, a2};
    ClubAd c2("Nom", "", 2, tab);
    c2.CalculCat();
    c2.Meilleur();
}