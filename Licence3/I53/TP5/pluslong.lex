%{
  /*Prologue*/
  #include <stdio.h>
  #include <string.h>
  int longmax = 0;
  char motlepluslong[256];
  int ligne = 1;
  int colonne = 1;
  int line = 0;
  int column = 1;
  int somme = 0;
%}
%option nounput
%option noinput
/*Définitions*/
ESPACE [ ]
TABULATION [\t]
LIGNE [\n]
LETTRE [a-zA-Z]
MOT {LETTRE}+
CHIFFRE [0-9]
NOMBRES {CHIFFRE}+

%%

{LETTRE} {
  colonne++;
}

{MOT} { colonne = colonne + yyleng;
    if (yyleng > longmax){
    longmax = yyleng;
    strcpy(motlepluslong, yytext);
    line = ligne;
    column = colonne - yyleng;
    printf("\n%s",yytext);
  }
}

{CHIFFRE} {
  colonne++;
  somme = somme + atoi(yytext);
}

{NOMBRES} {
  somme = somme + atoi(yytext);
}

{LIGNE} {
  ligne++;
  colonne = 1;
}

{TABULATION} {
  colonne = colonne + 2;
}

{ESPACE} {colonne++;}

. {
  colonne++;
}

%%
int main(int argc, char **argv) {
  if (argc < 1)
    return 0;
  yyin = fopen(argv[1], "r");
  yylex();
  printf("\nMot le plus long: %s, de longueur: %d, à la ligne %d et colonne %d\n", motlepluslong, longmax, line, column);
  printf("Somme de tous les entiers: %d\n", somme);
  return 0;
} 
