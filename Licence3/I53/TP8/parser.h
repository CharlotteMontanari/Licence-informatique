/* A Bison parser, made by GNU Bison 2.3.  */

/* Skeleton interface for Bison's Yacc-like parsers in C

   Copyright (C) 1984, 1989, 1990, 2000, 2001, 2002, 2003, 2004, 2005, 2006
   Free Software Foundation, Inc.

   This program is free software; you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation; either version 2, or (at your option)
   any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program; if not, write to the Free Software
   Foundation, Inc., 51 Franklin Street, Fifth Floor,
   Boston, MA 02110-1301, USA.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* Tokens.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
   /* Put the tokens into the symbol table, so that GDB and other debuggers
      know about them.  */
   enum yytokentype {
     NB = 258,
     SI = 259,
     ALORS = 260,
     SINON = 261,
     FSI = 262,
     TQ = 263,
     FAIRE = 264,
     FTQ = 265,
     DEBUT = 266,
     FIN = 267,
     AFFICHER = 268,
     LIRE = 269,
     VAR = 270,
     ID = 271,
     AFFECTATION = 272,
     DIFFERENT = 273,
     EGAL = 274,
     INFERIEUR = 275,
     SUPERIEUR = 276,
     INFERIEUR_EGAL = 277,
     SUPERIEUR_EGAL = 278
   };
#endif
/* Tokens.  */
#define NB 258
#define SI 259
#define ALORS 260
#define SINON 261
#define FSI 262
#define TQ 263
#define FAIRE 264
#define FTQ 265
#define DEBUT 266
#define FIN 267
#define AFFICHER 268
#define LIRE 269
#define VAR 270
#define ID 271
#define AFFECTATION 272
#define DIFFERENT 273
#define EGAL 274
#define INFERIEUR 275
#define SUPERIEUR 276
#define INFERIEUR_EGAL 277
#define SUPERIEUR_EGAL 278




#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef union YYSTYPE
#line 14 "parser.y"
{
 int nb;
 struct asa * noeud;
 char nom[32];
 }
/* Line 1529 of yacc.c.  */
#line 101 "parser.h"
	YYSTYPE;
# define yystype YYSTYPE /* obsolescent; will be withdrawn */
# define YYSTYPE_IS_DECLARED 1
# define YYSTYPE_IS_TRIVIAL 1
#endif

extern YYSTYPE yylval;

