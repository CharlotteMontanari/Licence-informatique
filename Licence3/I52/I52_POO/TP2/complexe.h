#ifndef _COMPLEXE_H
#define _COMPLEXE_H

class complexe {
    private:
        float re;
        float im;
    public:
        complexe(); //constructeur
        complexe(float, float); //constructeur
        complexe(const complexe &); //constructeur
        ~complexe();    //destructeur

        complexe somme(const complexe &, const complexe &);
        complexe produit(const complexe &, const complexe &);
        float cmodule(const complexe &);
        complexe conjugue(const complexe &);

        float getRe() const;
        float getIm() const;
        void Print() const;
        void Sum(const complexe&);
        bool Identical(const complexe&);
};

#endif