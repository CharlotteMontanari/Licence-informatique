%{
  
  #include <stdio.h>
  #include <ctype.h>
  #include <stdlib.h>
  
  int yylval;
  int yylex();
  int yyerror(char *msg);
  int myexp(int x, int n);
  int TAB[26];
  
%}


%token NB PLUS MOINS MUL DIV PUIS PO PF MEM AFFECT FIN
%left PLUS MOINS
%left DIV MUL
%right PUIS
%left PO PF
%right AFFECT

%start PROG

%%

PROG : PROG EXP FIN { printf("%d\n", $2 ) ;}
| 
;
EXP  : NB { $$ = $1 ;} 
| EXP PLUS EXP { $$ = $1 + $3 ;}
| EXP MOINS EXP { $$ = $1 - $3 ;}
| EXP DIV EXP { $$ = $1 / $3 ;}
| EXP MUL EXP { $$ = $1 * $3 ;}
| EXP PUIS EXP { $$ = myexp($1, $3) ;}
| PO EXP PF { $$ = $2 ;}
| MEM { $$ = TAB[$1]; }
| MEM AFFECT EXP { $$ = $3; TAB[$1] = $3; }
;
%%

int main( void ) {
  yyparse() ;
  return 0;
}

int yylex( ){
  int car;
  car = getchar() ;
  while ((car == ' ' || car == '\t') && car != EOF) 
    car = getchar() ;
  if ( car == EOF ) return 0 ;
  if ( isdigit(car) ) {
    yylval = car - '0';
    car = getchar();
    while (isdigit(car)) {
      yylval = yylval*10 + car - '0';
      car = getchar();
    }
    ungetc(car, stdin);
    return NB;
  }
  if ((car > 64) && (car < 92)) {
    yylval = car - 65;
    return MEM;
  }
  switch ( car ) {
  case '+' : return PLUS;
  case '-' : return MOINS;
  case '*' : 
    car = getchar();
    if (car == '*')
      return PUIS;
    ungetc(car, stdin);
    return MUL;
  case '/' : return DIV;
  case '(' : return PO;
  case ')' : return PF;
  case '=' : return AFFECT;
  case '\n': return FIN;
  }
  return -1;
}
 
int yyerror(char *msg) {
  printf("\n%s\n", msg);
  return 1;
}

int myexp( int x, int n) {
  int resultat = 0;
  if (n == 0) return 1;
  int i = 0;
  while (i < n) {
    resultat = resultat * x;
    i++;
  }
  return resultat;
}