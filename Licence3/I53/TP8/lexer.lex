%{
#include <string.h>
#include "parser.h" 
%}
  
%option nounput
%option noinput

CHIFFRE         [0-9]+
LETTRE          [a-zA-Z]+
RETOUR_LIGNE    [ \n\t]
COMMENTAIRE     [#].*
%%

"DEBUT"  	    {return DEBUT;}
"FIN"       	{return FIN;}
"AFFICHER"	    {return AFFICHER;}
"VAR"      	    {return VAR;}
"LIRE"			{return LIRE;}


"SI"        	{return SI;}
"ALORS"         {return ALORS;}
"SINON"         {return SINON;}
"FSI"     	    {return FSI;}
"TQ"  		    {return TQ;}
"FAIRE"         {return FAIRE;}
"FTQ"           {return FTQ;}


"<-"       {return AFFECTATION;}
"<="       {return INFERIEUR_EGAL;}
">="       {return INFERIEUR_EGAL;}
"<"        {return INFERIEUR;}
">"        {return SUPERIEUR;}
"!="       {return DIFFERENT;}
"="        {return EGAL;}

"("       {return yytext[0];}
")"       {return yytext[0];}
";"       {return yytext[0];}
"+"       {return yytext[0];}
"-"       {return yytext[0];}
"/"       {return yytext[0];}
"*"       {return yytext[0];}
"%"       {return yytext[0];}
","       {return yytext[0];}


{COMMENTAIRE}  	 {printf("%s\n", yytext);}
{CHIFFRE}        {yylval.nb = atoi(yytext); return NB;}
{LETTRE}         {strcpy(yylval.nom,yytext); return ID;}
{RETOUR_LIGNE}	
.               {fprintf(stdout, "[err lexer] caractere inconnu %c\n", yytext[0]); return 1;}

%%
