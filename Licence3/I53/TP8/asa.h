#ifndef ASA_H
#define ASA_H

#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include "ts.h"

typedef enum
{
  typeNB,
  typeOP,
  typeID,
  typeAFFECT,
  typeINST,
  typeECRIRE,
  typeLIRE,
  typeDECLA,
  typeCOMP,
  typeCOND,
  typeTQ
} typeNoeud;

// Structure des noeuds
typedef struct {
  int val;
} feuilleNb;

typedef struct {
  char nom[32];
} feuilleID;

typedef struct {
  struct asa *noeud[2];
} noeudAFFECT;

typedef struct {
  int op;
  struct asa *noeud[2];
} noeudOp;

typedef struct {
  struct asa *noeud[2];
} noeudINST;

typedef struct {
  struct asa *noeud;
} noeudECRIRE;

typedef struct {
  struct asa *noeud;
} noeudDECLA;

typedef struct {
  struct asa *noeud[2];
  int comp;
} noeudCOMP;

typedef struct {
  struct asa *noeud[3];
} noeudCOND;

typedef struct {
  struct asa *noeud[2];
} noeudTQ;

typedef struct {
  struct asa *noeud;
} noeudLIRE;

typedef struct asa {
  typeNoeud type;
  int ninst;

  union
  {
    feuilleNb union_nb;
    noeudOp union_op;
    feuilleID union_id;
    noeudAFFECT union_aff;
    noeudINST union_inst;
    noeudECRIRE union_ecrire;
    noeudLIRE union_lire;
    noeudDECLA union_decla;
    noeudCOMP union_comp;
    noeudCOND union_cond;
    noeudTQ union_tq;
  };
} asa;

// fonction d'erreur utilisée également par Bison
void yyerror(const char *);

/*
  Les fonctions creer_<type> construise un noeud de l'arbre
  abstrait du type correspondant et renvoie un pointeur celui-ci
 */
asa *creer_feuilleNb(int);
asa *creer_noeudOp(int, asa *, asa *);

void free_asa(asa *);

// produit du code pour la machine RAM à partir de l'arbre abstrait
// ET de la table de symbole

asa *creer_feuilleID(char *);

asa *creer_noeudAFFECT(asa *, asa *);

asa *creer_noeudINST(asa *, asa *);

asa *creer_noeudECRIRE(asa *);

asa *creer_noeudDECLA(asa *);

asa *creer_noeudCOMP(int, asa *, asa *);

asa *creer_noeudCOND(asa *, asa *, asa *);

asa *creer_noeudTQ(asa *, asa *);

asa *creer_noeudLIRE(asa *);

void codegen(asa *);

extern FILE *fichier;
extern int sommet;
extern ts table;

#endif
