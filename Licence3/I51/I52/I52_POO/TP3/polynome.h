#ifndef _POLYNOME_H
#define _POLYNOME_H

class polynome {
    private:
        int deg;
        float *coeff;
    public:
        polynome();
        polynome(int, float *);
        polynome(const polynome &);
        ~polynome();
};

#endif