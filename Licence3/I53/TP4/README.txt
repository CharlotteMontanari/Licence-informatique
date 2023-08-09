Mon fichier I53_TP4 contient 3 sous fichiers: data, lib et essai.
Le fichier data contient tous les fichiers textes.
Le fichier essai contient les exécutables
Et le fichier lib contient tous les fichiers .c et .h ainsi que les .o
Ce qui nous donne ceci:
.
├── README.txt
├── data
│   ├── afd.txt
│   ├── afn.txt
│   └── grammaire.txt
├── essai
├── lib
│   ├── af.c
│   ├── afd.c
│   ├── afd.h
│   ├── afn.c
│   ├── afn.h
│   ├── compregex.c
│   ├── compregex.h
│   ├── mygrep.c
│   ├── postfix_to_af.c
│   └── postfix_to_af.h
└── makefile

En ce qui concerne les tests pour les fonctions, j'ai laissé dans le fichier af.c 
tous mes tests. Et pour le fichier mygrep., en voici:
./mygrep "a.(a+b)" "aab"
./mygrep "(a+b)" "b"
./mygrep "(a+b)" "aaccc"