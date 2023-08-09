#ifndef ANALEX_H
#define ANALEX_H

typedef struct list_symb {
    char *symb;
    int count;
    struct list_symb *suiv;
} list_symb;

int inserer(char *nom, list_symb *ptr);
void print_list(list_symb *ptr);

#endif