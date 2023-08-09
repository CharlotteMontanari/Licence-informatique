#include <iostream>
#include <string>

class Personne {
    private:
        unsigned int age;
        std::string nom;
        std::string prenom;
    public:
        Personne(unsigned int, std::string, std::string);    //constructeur
        ~Personne();
        void affichage();   //methode
        void vieillir();    //methode
};

class Professeur: public Personne {
    private:
        std::string statut;
        unsigned int heure;
    public:
        Professeur(unsigned int, std::string, std::string, unsigned int);
        void affichage();   //methode
        void travail(unsigned int);
};

class Etudiant1: public Personne {
    protected:
        unsigned int nb;
        unsigned int *notes;
    public:
        Etudiant1(unsigned int, std::string, std::string, unsigned int);
        Etudiant1(const Etudiant1 &);   //constructeur par copie
        ~Etudiant1();   //destructeur
        void ajouterNotes(unsigned int *);
        void affichage();
        int moyenne();
        Etudiant1 operator=(Etudiant1);
};

class Matiere {
    private:
        std::string nom;
        unsigned int coeff;
    public:
        Matiere();
        Matiere(std::string, unsigned int);
        void affichage();
        std::string getNom();
        unsigned int getCoef();
};

class Etudiant2: public Etudiant1 {
    private:
        Matiere *m;
    public:
        Etudiant2(unsigned int, std::string, std::string, unsigned int, Matiere *);
        Etudiant2(const Etudiant2 &);   //constructeur par copie
        ~Etudiant2();   //destructeur
        void affichage();
        unsigned int moyenne();
        Etudiant2 operator=(Etudiant2);
};
/*un constructeur avec 5 paramètres
un constructeur par copie
un destructeur
une méthode Affic qui ache le nom, le prénom, le nom de chaque matière suivi de la note obtenue dans cette matière
une méthode Moyenne qui retourne la moyenne de l'étudiant chaque matière étant aectée de son coecient
la surcharge de l'opérateur d'aectation*/