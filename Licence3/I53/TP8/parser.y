%{
 #include <stdio.h>
 #include <ctype.h>
 #include <unistd.h>
 #include "asa.h"
 extern int yylex(); 

 FILE *fichier;	// fichier d'ecriture
 int sommet = 0; // sommet de la pile
 ts table;	// table des symboles
 
%}

%union{
 int nb;
 struct asa * noeud;
 char nom[32];
 };

//%define parse.error verbose

%token <nb> NB 
%token SI ALORS SINON FSI TQ FAIRE FTQ DEBUT FIN AFFICHER LIRE VAR

%type <noeud> DECLARATION INSTS INST COMPARAISON EXP  
%token <nom> ID

%right AFFECTATION
%right EGAL DIFFERENT
%right SUPERIEUR_EGAL INFERIEUR_EGAL SUPERIEUR INFERIEUR 

%left '+' '-'
%left '/' '*' '%'
%left '(' ')'


%start PROG

%%
// Ensemble de production

// les programmes commencent par le mot DEBUT et finissent par le mot FIN
PROG : DEBUT INSTS FIN      					 { codegen($2); free_asa($2);}
;	

// On a plusieurs instructions ou une seule
INSTS : INSTS INST								{ $$ = creer_noeudINST($1, $2);}
| INST											{ $$ = creer_noeudINST($1, NULL);}
;

// Notre instruction peut etre une expression
INST : EXP ';'
| AFFICHER EXP 	';'								{$$ = creer_noeudECRIRE($2);}
| LIRE ID ';'									{$$ = creer_noeudLIRE(creer_feuilleID($2));}
| DECLARATION ';'
| ID AFFECTATION EXP	';'					  	{ $$ = creer_noeudAFFECT(creer_feuilleID($1), $3);} 
| SI COMPARAISON ALORS INSTS SINON INSTS FSI    { $$ = creer_noeudCOND($2, $4, $6);}
| SI COMPARAISON ALORS INSTS FSI 			    { $$ = creer_noeudCOND($2, $4, NULL);}
| TQ COMPARAISON FAIRE INSTS FTQ 			    { $$ = creer_noeudTQ($2, $4);}
;

// Pour une declaration, on peut avoir plusieurs variables ou une seule
DECLARATION : VAR ID 	{ $$ = creer_noeudDECLA(creer_feuilleID($2)); ts_ajouter_id(table, $2);}
| DECLARATION ',' ID 	{ $$ = creer_noeudINST($1, creer_noeudDECLA(creer_feuilleID($3))); ts_ajouter_id(table, $3);}
;

// Pour la comparaison, on compare 2 expressions
COMPARAISON : EXP SUPERIEUR_EGAL EXP	    { $$ = creer_noeudCOMP(SUPERIEUR_EGAL, $1, $3);}
| EXP SUPERIEUR EXP							{ $$ = creer_noeudCOMP(SUPERIEUR, $1, $3);}
| EXP INFERIEUR EXP							{ $$ = creer_noeudCOMP(INFERIEUR, $1, $3);}
| EXP INFERIEUR_EGAL EXP					{ $$ = creer_noeudCOMP(INFERIEUR_EGAL, $1, $3);}
| EXP EGAL EXP							    { $$ = creer_noeudCOMP(EGAL, $1, $3);}
| EXP DIFFERENT EXP			 				{ $$ = creer_noeudCOMP(DIFFERENT, $1, $3);}
;

// Une expression elle, peut etre un nombre, une operation, 
// une operation, une variable ou une expression entre parenthese
EXP : NB 								{ $$ = creer_feuilleNb(yyval.nb); }
| EXP '+' EXP 							{ $$ = creer_noeudOp('+', $1, $3);}						
| EXP '/' EXP    						{ $$ = creer_noeudOp('/', $1, $3);}
| EXP '-' EXP           				{ $$ = creer_noeudOp('-', $1, $3);}						
| EXP '*' EXP    	   					{ $$ = creer_noeudOp('*', $1, $3);} 	
| EXP '%' EXP 							{ $$ = creer_noeudOp('%', $1, $3);} 
| '-' EXP								{ $$ = creer_noeudOp('*', $2, creer_feuilleNb(-1));}
| ID									{ $$ = creer_feuilleID($1);}
| '(' EXP ')'						    { $$ = $2; }
;

%%

int main(int argc, char *argv[]) {
 
 extern FILE *yyin;
 if (argc == 1) {
  fprintf(stderr, "aucun fichier fournie\n");
  return 1;
 }
 yyin = fopen(argv[1], "r");
 
 char *name = strcat(argv[1], "_RAM");
 fichier = fopen(name, "w");
 table = ts_init_table("TABLE1");
 
 yyparse();
 fprintf(fichier, "STOP \n");
 ts_free_table(table);
 fclose(fichier);
 fclose(yyin);	
 printf("COMPILATION AVEC SUCCÈS : %s\n", name);
 return 0;
}
