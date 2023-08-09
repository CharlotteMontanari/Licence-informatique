# Bienvenue sur notre README

Ici, vous trouverez ce qui a été géré par nos conditions, et ce qui ne l'a pas été.
Vous y trouverez également quelques explications sur le code.

## Fonctionnalités non gérées

Pour commencer, voici l'ensemble des fonctionnalits que nous n'avons pas gérées, osit par choix, soit par manque de temps

### Choisir un programme pour chaque robot

Comme l'utilisateur choisis lui même le nombre de robots qui s'affronteront, nosu avons d'abord choisis de créer directement toutes les instances de Robots en chargeant aléatoirement un programme.
Ensuite, il nous a manqué du temps pour pouvoir implémenter la possibilité de donner le choix à l'utilisateur par Robot.

Cepandant, pour pouvoir tester un programme en particulier, il suffit de suivre la procédure suivante:

* Mettre un fichier .rbt dans le répertoire data
*-* Ouvrir le fichier window.py à la ligne 34 et entrer le nom du fichier .rbt  dans la liste qui contient les instructions

### Afficher une aide en ligne

Là aussi, le temsp nous a manqué pour implémenter cette fonctionnalité

### Charger un terrain depuis un fichier et avoir des dimensions personalisées

Nous n'avons pas donné la possibilité à l'utilisteur ed charger sa propre carte (à partir d'un formulaire), ni de changer les dimensions de la carte (30x20). Cependant, c'est possible de le faire manuellement avant de lancer le programme, en suivant les sinstructions suivantes:

* ouvrir le repertoire data
* deposer une carte au format .txt
* ouvrir window.py à la ligne 33 et saisir le nom de la carte

### Distinguer visuellement les robots

Pour l'affichage de la carte et ses objets, nous avons utilisé une Classe Enum, et de ce fait, un Robot n'est représenté que par une seule valeur, empêchant d'en attribuer une par robot.

### Relancer une partie

Pour relancer une partie, il faut fermer puis rouvrir le programme.

## Fonctionnalités gérées

### Gestion des instructions dans un fichier

Nous vérifions que toutes les instructions soient valides, qu'il y ait le bon nombre.
La première ligne est dédiée au commentaire et n'est donc pas interprétée.
La deuxième ligne est dédié à l'instruction de secours.
Les lignes suivantes font partie du programme.

### L'invisibilité

Un robot reste invisible 1 tour complet (une fois que tous les robots on joué leur instruction)
Il ne peut pas être touché ou détecté lorsqu'il est invisible.

### Affichage des instructions

Les instructions de chaque robot (et leur effet) sont affichées dans une Listbox dédiée pendant tout le déroulement de la partie.
Elles sont également affichées dans la console avec quelques informations supplémentaires (telles que la position, etc.)

### Représentation d'un tir

Les Tirs orizontaux ou Verticaux sont visuellement représentés par un carré jaune (au lieu d'un carré blanc quand une case est vide)
Lorsqu'un obstacle ou un robot est touché, il se change en couleur rouge pour illustrer l'impact.
Les mines, elles, disparaissent simplement.

### Mort d'un robot et Vainqueur

Lorsqu'un robot meurt, son apparence  est remplacée par une tête de mort
Le robot vainqueur est représenté par une couronne.

### Paramètres dynamiques

En deuxième page, l'utilisateur peut choisir 4 paramètres:

* le nombre de robots (entre 2 et 6)
* la distance de repérage (entre 4 et 6)
* le nombre de points de vie des robots
* la carte sur laquelle les robots s'affronteront

## Ce que nous aurions aimé gérer

* choisir un programme différent pour chaque robot
* mettre uez icone différente pour chaque robot
* générer un carte via un code
* relancer une nouvelle partie
* visionner à nouveau une partie terminée
