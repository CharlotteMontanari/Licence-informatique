#1
SELECT nom, age
FROM Participant

#2
SELECT AVG(age)
FROM Participant

#3
SELECT count(sexe), sexe
FROM Participant
GROUP BY sexe

#4
SELECT count(danse), danse
FROM Cours
GROUP BY danse

#5
SELECT danse
FROM Cours, inscription
Where Cours.id_cours in (Select id_cours
                         FROM inscription)

#6
SELECT danse
FROM Cours, inscription
Where Cours.id_cours not in (Select id_cours
                             FROM inscription)

#7
SELECT i.nom
FROM Intervenant i, Atelier a
WHERE a.id_intervenant, i.id_intervenant
    AND a.id_cours not in (SELECT distinct id_cours
                           FROM inscription)

#8
(SELECT p.nom
FROM Participant p, inscription i, cours c
WHERE p.id_participant = i.id_participant
    AND i.id_cours = c.id_cours
    AND c.danse = 'salsa')
INSERT
    (SELECT p.nom
     FROM participant p, inscription i, cours
     WHERE p.id_participant = i.id_participant
        AND i.id_cours = c.id_cours
        AND c.danse = 'Rock')

#9
SELECT c.danse, count(i.intervenant)
FROM intervenant i, cours c, atelier a
WHERE c.id_cours = a.id_cours
    AND i.id_intervenant = i.id_intervenant
GROUP BY c.danse

#10
SELECT i.nom, c.id_cours, c.danse
FROM intervenant I, cours c, atelier a
WHERE i.id_intervenant = a.id_intervenant
	AND a.id_cours = c.id_cours

#11
SELECT id_participant, nom
FROM participant
WHERE age = (SELECT max(age)
		     FROM participant)

#12
SELECT danse
FROM cours
WHERE danse = (SELECT max(danse))

#13
SELECT id_cours
FROM atelier
GROUP BY id_cours
HAVING count(id_cours) = 1

#14
SELECT id_cours
FROM atelier
GROUP BY id_cours
HAVING count(id_cours) >= all (SELECT count(id_cours)
                               FROM atelier
                               GROUP BY id_cours)

#15
SELECT id_cours, count(id_participant)
FROM inscription
GROUP BY id_cours

#16
SELECT count(id_cours)
FROM atelier a, intervenant i
WHERE a.id_intervenant = i.id_intervenant
    AND nom = 'Gilles'

#17


#18

#19
SELECT danse
FROM cours c, atelier a, intervenant i
WHERE c.id_cours = a.id_cours
    AND atelier.id_intervenant = i.id_intervenant
    AND nom = 'Amandine'
GROUP BY danse

#20
SELECT c.id_cours, count(id_participant), nbr_eleve, danse
FROM cours c, atelier a, intervenant n, inscription i
WHERE c.id_cours = a.id_cours 
    AND a.id_intervenant = n.id_intervenant 
    AND c.id_cours = i.id_cours 
    AND nom = 'Amandine' 
GROUP BY c.id_cours, danse

#21
SELECT c.id_cours
FROM cours c, inscription i, participant p
WHERE c.id_cours = i.id_cours
    AND i.id_participant = p.id_participant
    AND nom = 'Henri'
INTERSECT (SELECT c.id_cours
           FROM cours c, inscription i, participant p
           WHERE c.id_cours = i.id_cours
               AND i.id_participant = p.id_participant
               AND nom = 'Melanie')

#22


#23
SELECT count(id_participant)
FROM participant p, inscription i, intervenant n, atelier a
WHERE p.id_participant = i.id_participant
    AND n.id_intervenant = a.id_intervenant
    AND i.id_cours = a.id_cours
    AND i.nom = 'Denis'
    AND i.nom = 'Amandine'

#24