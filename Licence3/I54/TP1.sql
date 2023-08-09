CREATE TABLE Departement(
    DID varchar(2),
    Libelle varchar(20),
    PRIMARY KEY (DID)
);

CREATE TABLE Employe(
    EID integer CHECK (EID < 100),
    Nom varchar(20),
    Dept varchar(2),
    PRIMARY KEY (EID),
    FOREIGN KEY(Dept) REFERENCES Departement(DID)
);

INSERT INTO Departement VALUES(
    83, 'Var'
);

-- Le premier rollback ne fait rien: "there is no transaction in progress"

BEGIN TRANSACTION;
INSERT INTO Departement VALUES(
    12, 'Marseille'
);
ROLLBACK;

-- Le ROLLBACK  a annuler l'action

BEGIN TRANSACTION;
INSERT INTO Departement VALUES(
    12, 'Marseille'
);
COMMIT;

-- Le COMMIT valide l'action

BEGIN TRANSACTION;
INSERT INTO Departement VALUES(
    06, 'Nice'
);
COMMIT;
SELECT * FROM Departement;
ROLLBACK;
SELECT * FROM Departement;

-- Le ROLLBACK ne peut pas avoir lieu car la transaction a été validé par le COMMIT

-- Dans le BEGIN TRANSACTION, s'il n'y a ni COMMIT, ni ROLLBACK, rien n'est validé
-- donc en fermant le terminal, rien n'est ajouter dans la table
-- en revanche, sans le BEGIN TRANSACTION, l'information aurait été ajouté dans la table

BEGIN TRANSACTION;
DELETE FROM Departement;
ROLLBACK;

-- Le ROLLBACK a annulé le DELETE des données

BEGIN TRANSACTION;
DELETE FROM Departement;
COMMIT;

-- Le COMMIT a validé le DELETE des données

-------------------------------------------------------

INSERT INTO Departement VALUES(
    'C1', 'Info'
);
INSERT INTO Employe VALUES(
    01, 'Quentin', 'C1'
);

INSERT INTO Departement VALUES(
    'C1', 'Informatique'
);

-- On ne peut pas faire ce INSERT car dans les deux cas, on a la même clé primaire, 
-- ce qui n'est pas possible

INSERT INTO Employe VALUES(
    02, 'Gregoire', 'C2'
);

-- Ce n'est pas possible car C2 ne figure pas dans la table Departement

DELETE FROM Departement
WHERE DID = 'C1';

-- On ne peut pas supprimer C1, car il est référencé dans la table Employe

ALTER TABLE Employe
DROP CONSTRAINT Dept;

-- On constate que dans la table Employe, ça a supprimé la clé étrangère
-- Par contre, rien ne s'est passé dans la table Departement

DELETE FROM Departement;
DELETE FROM Employe;

ALTER TABLE Employe
ADD CONSTRAINT Dept_fk 
FOREIGN KEY (Dept)
REFERENCES Departement(DID)
ON DELETE CASCADE;
INSERT INTO Departement VALUES(
    'C1', 'Informatique'
);
INSERT INTO Employe VALUES(
    01, 'Quentin', 'C1'
);

DELETE FROM Departement
WHERE DID = 'C1';

-- On constate qu'il a tout supprimer

INSERT INTO Departement VALUES(
    'C1', 'Informatique'
);
INSERT INTO Employe VALUES(
    01, 'Quentin', 'C1'
);

ALTER TABLE Employe
DROP CONSTRAINT Dept_fk;

ALTER TABLE Employe
ADD CONSTRAINT Dept_fk 
FOREIGN KEY (Dept)
REFERENCES Departement(DID)
DEFERRABLE; 

SET CONSTRAINTS Dept_fk
DEFERRED;

DELETE FROM Departement
WHERE DID = 'C1';

-- On constate qu'on ne peut pas supprimer la valeur car elle est toujours
-- référencé dans la table Employe

-------------------------------------------------------

-- psql -h sinfo1
-- SET SEARCH_PATH TP1_I54, public

INSERT INTO Departement VALUES(
    'C1', 'Informatique'
);
INSERT INTO Departement VALUES(
    'C2', 'Informatique'
);

-- On constate qu'il a bien ajouté les 2 valeurs C1 et C2
-- et qu'on voit les mêmes tables dans la session 1 et dans la session 2

BEGIN TRANSACTION;  -- dans la session 1
INSERT INTO Departement VALUES(
    12, 'Marseille'
);
BEGIN TRANSACTION;  -- dans la session 2
INSERT INTO Departement VALUES(
    83, 'Var'
);

