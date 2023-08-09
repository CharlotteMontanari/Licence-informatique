#include "asa.h"
#include "parser.h"

asa *creer_feuilleNb(int val) {
  asa *p;

  if ((p = malloc(sizeof(asa))) == NULL)
    yyerror("echec allocation mémoire");

  p->type = typeNB;
  p->union_nb.val = val;
  p->ninst = 1; //on met la valeur union_nb dans l'accumulateur

  return p;
}

asa *creer_feuilleID(char *nom) {
  asa *p;

  if ((p = malloc(sizeof(asa))) == NULL)
    yyerror("echec allocation mémoire");

  p->type = typeID;
  p->ninst = 1; //on met la valeur union_id dans l'accumulateur
  strcpy(p->union_id.nom, nom);

  return p;
}

asa *creer_noeudOp(int op, asa *p1, asa *p2) {
  asa *p;

  if ((p = malloc(sizeof(asa))) == NULL)
    yyerror("echec allocation mémoire");

  p->type = typeOP;
  p->union_op.op = op;
  p->union_op.noeud[0] = p1;
  p->union_op.noeud[1] = p2;
  p->ninst = p1->ninst + p2->ninst + 2; // on charge les valeurs puis on les stocks, et on fait l'operation

  return p;
}

asa *creer_noeudAFFECT(asa *p1, asa *p2) {
  asa *p;

  if ((p = malloc(sizeof(asa))) == NULL)
    yyerror("echec allocation mémoire");

  p->type = typeAFFECT;
  p->union_aff.noeud[0] = p1;
  p->union_aff.noeud[1] = p2;
  p->ninst = p2->ninst + 1; // on charge p2 dans l'accumulateur

  return p;
}

asa *creer_noeudINST(asa *p1, asa *p2) {
  asa *p;

  if ((p = malloc(sizeof(asa))) == NULL)
    yyerror("echec allocation mémoire");

  p->type = typeINST;
  p->union_aff.noeud[0] = p1;
  if (p2 != NULL) {
    p->union_aff.noeud[1] = p2;
    p->ninst = p1->ninst + p2->ninst; // on additionne le nombre d'instruction de p1 et de p2
  }
  else
    p->ninst = p1->ninst;

  return p;
}

asa *creer_noeudECRIRE(asa *p1) {
  asa *p;

  if ((p = malloc(sizeof(asa))) == NULL)
    yyerror("echec allocation mémoire");

  p->type = typeECRIRE;
  p->union_ecrire.noeud = p1;
  p->ninst = p1->ninst + 1; // on met p1 dans l'accumulateur

  return p;
}

asa *creer_noeudLIRE(asa *p1) {
  asa *p;

  if ((p = malloc(sizeof(asa))) == NULL)
    yyerror("echec allocation mémoire");

  p->type = typeLIRE;
  p->union_lire.noeud = p1;
  p->ninst = 2; // on lit la valeur d'entree et on l'a stock

  return p;
}

asa *creer_noeudDECLA(asa *p1) {
  asa *p;

  if ((p = malloc(sizeof(asa))) == NULL)
    yyerror("echec allocation mémoire");

  p->type = typeDECLA;
  p->union_decla.noeud = p1;
  p->ninst = 2; // on met 0 dans l'accumulateur et l'a stock

  return p;
}

asa *creer_noeudCOMP(int op, asa *p1, asa *p2) {
  asa *p;

  if ((p = malloc(sizeof(asa))) == NULL)
    yyerror("echec allocation mémoire");

  p->union_comp.comp = op;
  p->type = typeCOMP;
  p->union_comp.noeud[0] = p1;
  p->union_comp.noeud[1] = p2;
  p->ninst = p1->ninst + p2->ninst + 2; // on charge les valeurs, on les stock, et on opere

  return p;
}

asa *creer_noeudCOND(asa *p1, asa *p2, asa *p3) {
  asa *p;

  if ((p = malloc(sizeof(asa))) == NULL)
    yyerror("echec allocation mémoire");

  p->type = typeCOND;
  p->union_cond.noeud[0] = p1;
  p->union_cond.noeud[1] = p2;
  p->ninst = p1->ninst + p2->ninst + 1;

  if (p3 != NULL) {
    p->ninst += p3->ninst + 1;
    p->union_cond.noeud[2] = p3;
  }

  if ((p1->union_comp.comp == INFERIEUR) || (p1->union_comp.comp == SUPERIEUR) || (p1->union_comp.comp == EGAL))
    p->ninst += 1;

  return p;
}

asa *creer_noeudTQ(asa *p1, asa *p2) {
  asa *p;

  if ((p = malloc(sizeof(asa))) == NULL)
    yyerror("echec allocation mémoire");

  p->ninst = p1->ninst + p2->ninst + 2;
  p->type = typeTQ;
  p->union_tq.noeud[0] = p1;
  p->union_tq.noeud[1] = p2;

  if ((p1->union_comp.comp == INFERIEUR) || (p1->union_comp.comp == SUPERIEUR) || (p1->union_comp.comp == EGAL))
    p->ninst++;

  return p;
}

void free_asa(asa *p) {
  if (!p)
    return;

  switch (p->type)
  {
  case typeOP:
    free_asa(p->union_op.noeud[0]);
    free_asa(p->union_op.noeud[1]);
    break;

  case typeAFFECT:
    free_asa(p->union_aff.noeud[0]);
    free_asa(p->union_aff.noeud[1]);
    break;

  case typeINST:
    free_asa(p->union_inst.noeud[0]);
    free_asa(p->union_inst.noeud[1]);
    break;

  case typeECRIRE:
    free_asa(p->union_ecrire.noeud);
    break;

  case typeLIRE:
    free_asa(p->union_lire.noeud);
    break;

  case typeDECLA:
    free_asa(p->union_decla.noeud);
    break;

  case typeCOMP:
    free_asa(p->union_comp.noeud[0]);
    free_asa(p->union_comp.noeud[1]);
    break;

  case typeCOND:
    free_asa(p->union_cond.noeud[0]);
    free_asa(p->union_cond.noeud[1]);
    free_asa(p->union_cond.noeud[2]);
    break;

  case typeTQ:
    free_asa(p->union_tq.noeud[0]);
    free_asa(p->union_cond.noeud[1]);
    break;

  default:
    break;
  }
  free(p);
}

int nbr_lignes = 0; // Indice pour le JUMP

void codegen(asa *p) {
  if (!p)
    return;
  switch (p->type) {
  case typeNB:
    fprintf(fichier, "LOAD #%d\n", p->union_nb.val);
    nbr_lignes += 1;
    break;

  case typeOP:
    codegen(p->union_op.noeud[1]);
    fprintf(fichier, "STORE %d\n", ++sommet);
    nbr_lignes += 1;
    codegen(p->union_op.noeud[0]);
    switch (p->union_op.op) {
      case '+':
        fprintf(fichier, "ADD %d\n", sommet--);
        break;

      case '-':
        fprintf(fichier, "SUB %d\n", sommet--);
        break;

      case '/':
        fprintf(fichier, "DIV %d\n", sommet--);
        break;

      case '*':
        fprintf(fichier, "MUL %d\n", sommet--);
        break;

      case '%':
        fprintf(fichier, "MOD %d\n", sommet--);
        break;

      default:
        printf("Err : %d\n", p->union_op.op);
        break;
    }

    nbr_lignes += 1;
    break;

  case typeID:
    if (ts_retrouver_id(table, p->union_id.nom) != -1) {
      fprintf(fichier, "LOAD %d\n", ts_retrouver_id(table, p->union_id.nom));
      nbr_lignes += 1;
    }
    else
      printf("ERREUR : VARIABLE '%s' N'EXISTE PAS\n", p->union_id.nom);

    break;

  case typeAFFECT:
    codegen(p->union_aff.noeud[1]);
    fprintf(fichier, "STORE %d\n", ts_retrouver_id(table, p->union_aff.noeud[0]->union_id.nom));
    nbr_lignes += 1;
    break;

  case typeINST:
    codegen(p->union_inst.noeud[0]);
    if (p->union_aff.noeud[1] != NULL)
      codegen(p->union_inst.noeud[1]);
    break;

  case typeECRIRE:
    codegen(p->union_ecrire.noeud);
    fprintf(fichier, "WRITE\n");
    nbr_lignes += 1;
    break;

  case typeLIRE:
    fprintf(fichier, "READ\n");
    fprintf(fichier, "STORE %d\n", ts_retrouver_id(table, p->union_lire.noeud->union_id.nom));
    nbr_lignes += 2;
    break;

  case typeDECLA:
    fprintf(fichier, "LOAD #0\n");
    fprintf(fichier, "STORE %d\n", ts_retrouver_id(table, p->union_decla.noeud->union_id.nom));
    nbr_lignes += 2;
    break;

  case typeCOMP:
    codegen(p->union_comp.noeud[1]);
    fprintf(fichier, "STORE %d\n", ++sommet);
    nbr_lignes += 1;
    codegen(p->union_comp.noeud[0]);
    fprintf(fichier, "SUB %d\n", sommet--);
    nbr_lignes += 1;
    break;

  case typeCOND:
    codegen(p->union_cond.noeud[0]);
    int jump = 0;
    if (p->union_cond.noeud[2] != NULL)
      jump++;
    switch (p->union_cond.noeud[0]->union_comp.comp) {
      case INFERIEUR:
        nbr_lignes += 2;
        fprintf(fichier, "JUMZ %d\n", p->union_cond.noeud[1]->ninst + nbr_lignes + jump);
        fprintf(fichier, "JUMG %d\n", p->union_cond.noeud[1]->ninst + nbr_lignes + jump);
        codegen(p->union_cond.noeud[1]);
        break;

      case SUPERIEUR:
        nbr_lignes += 2;
        fprintf(fichier, "JUMZ %d\n", p->union_cond.noeud[1]->ninst + nbr_lignes + jump);
        fprintf(fichier, "JUML %d\n", p->union_cond.noeud[1]->ninst + nbr_lignes + jump);
        codegen(p->union_cond.noeud[1]);
        break;

      case INFERIEUR_EGAL:
        nbr_lignes += 1;
        fprintf(fichier, "JUMG %d\n", p->union_cond.noeud[1]->ninst + nbr_lignes + jump);
        codegen(p->union_cond.noeud[1]);
        break;

      case SUPERIEUR_EGAL:
        nbr_lignes += 1;
        fprintf(fichier, "JUML %d\n", p->union_cond.noeud[1]->ninst + nbr_lignes + jump);
        codegen(p->union_cond.noeud[1]);
        break;

      case DIFFERENT:
        nbr_lignes += 1;
        fprintf(fichier, "JUMZ %d\n", p->union_cond.noeud[1]->ninst + nbr_lignes + jump);
        codegen(p->union_cond.noeud[1]);
        break;

      case EGAL:
        nbr_lignes += 2;
        fprintf(fichier, "JUML %d\n", p->union_cond.noeud[1]->ninst + nbr_lignes + jump);
        fprintf(fichier, "JUMG %d\n", p->union_cond.noeud[1]->ninst + nbr_lignes + jump);
        codegen(p->union_cond.noeud[1]);
        break;

      default:
        printf("Erreur : %d\n", p->union_cond.noeud[0]->union_comp.comp);
        break;
    }
    if (p->union_cond.noeud[2] != NULL) {
      fprintf(fichier, "JUMP %d\n", p->union_cond.noeud[2]->ninst + (++nbr_lignes));
      codegen(p->union_cond.noeud[2]);
    }

    break;

  case typeTQ:
    codegen(p->union_tq.noeud[0]);
    int jumpTQ = nbr_lignes - p->union_tq.noeud[0]->ninst;
    switch (p->union_tq.noeud[0]->union_comp.comp) {
      case INFERIEUR:
        nbr_lignes += 2;
        fprintf(fichier, "JUMZ %d\n", p->union_tq.noeud[1]->ninst + nbr_lignes + 1);
        fprintf(fichier, "JUMG %d\n", p->union_tq.noeud[1]->ninst + nbr_lignes + 1);
        codegen(p->union_tq.noeud[1]);
        break;

      case SUPERIEUR:
        nbr_lignes += 2;
        fprintf(fichier, "JUMZ %d\n", p->union_tq.noeud[1]->ninst + nbr_lignes + 1);
        fprintf(fichier, "JUML %d\n", p->union_tq.noeud[1]->ninst + nbr_lignes + 1);
        codegen(p->union_tq.noeud[1]);
        break;

      case INFERIEUR_EGAL:
        nbr_lignes += 1;
        fprintf(fichier, "JUMG %d\n", p->union_tq.noeud[1]->ninst + nbr_lignes + 1);
        codegen(p->union_tq.noeud[1]);
        break;

      case SUPERIEUR_EGAL:
        nbr_lignes += 1;
        fprintf(fichier, "JUML %d\n", p->union_tq.noeud[1]->ninst + nbr_lignes + 1);
        codegen(p->union_tq.noeud[1]);
        break;

      case DIFFERENT:
        nbr_lignes += 1;
        fprintf(fichier, "JUMZ %d\n", p->union_tq.noeud[1]->ninst + nbr_lignes + 1);
        codegen(p->union_tq.noeud[1]);
        break;

      case EGAL:
        nbr_lignes += 2;
        fprintf(fichier, "JUML %d\n", p->union_tq.noeud[1]->ninst + nbr_lignes + 1);
        fprintf(fichier, "JUMG %d\n", p->union_tq.noeud[1]->ninst + nbr_lignes + 1);
        codegen(p->union_tq.noeud[1]);
        break;

      default:
        printf("Erreur : %d\n", p->union_tq.noeud[0]->union_comp.comp);
        break;
    }
    fprintf(fichier, "JUMP %d\n", jumpTQ);
    nbr_lignes++;
    break;

  default:
    printf("Err : %d\n", p->type);
    break;
  }
}

void yyerror(const char *s) {
  fprintf(stderr, "%s\n", s);
  exit(0);
}
