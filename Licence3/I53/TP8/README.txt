Mon fichier TP8 contient tous les fichiers:
.c, .h, .lex, .y, .output, .o, .txt, .txt_RAM et l'executable

En ce qui concerne les tests pour le compilateur, j'ai crée trois fichier textes différents: 
test1, test2, test3 dans le dossier data.

Dans le makfile, j'ai du mettre la librairie -ll car sur MacOS, il ne connait pas la librairie -lfl

Dans le fichier parser.y, j'ai également du commenter: %define parse.error verbose car il me faisait
planter mon programme (du a mon Mac).