CREATE TABLE Spectacle(
    nomS VARCHAR(15) NOT NULL PRIMARY KEY,
    Nbplaces INTEGER NOT NULL,
    NbplacesLibres INTEGER NOT NULL,
    tarif DECIMAL(10,2) NOT NULL
);
CREATE TABLE Client(
    nomC VARCHAR(10) NOT NULL PRIMARY KEY,
    Solde integer NOT NULL
);
CREATE TABLE Reservation(
    nomC VARCHAR(10) NOT NULL references Client,
    nomS VARCHAR(15) NOT NULL references Spectacle,
    NbplacesReservees INT NOT NULL,
    PRIMARY KEY (nomC, nomS)
);


-- Pour que la base de données reste cohérente, il faut toujours que pour un spectacle donné, 
-- on est la propriété suivante :
--(1) sum(NbplacesReservees)=(NbPlaces−NbplacesLibres)

INSERT INTO Client VALUES ('Quentin', 50);
INSERT INTO Client VALUES ('Grégoire', 50);
INSERT INTO Spectacle VALUES ('Happy Potter', 250, 250, 20);

CREATE OR REPLACE FUNCTION miseajour_placesReservees() 
RETURNS TRIGGER AS $$
    BEGIN
        IF (new.NbplacesReservees > (select NbplacesLibres 
                                    from Spectacle 
                                    where Spectacle.nomS=new.nomS)) 
        THEN
            RETURN NULL;
        ELSE
            UPDATE Spectacle
            SET NbplacesLibres = NbplacesLibres - new.NbplacesReservees
            WHERE Spectacle.nomS = new.nomS;
        END IF;
             RETURN new;
        END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER TRIG_placesReservees
BEFORE INSERT OR UPDATE ON Reservation
FOR EACH ROW EXECUTE PROCEDURE miseajour_placesReservees();

BEGIN TRANSACTION;  -- dans le premier terminal
INSERT INTO Reservation VALUES ('Quentin','Happy Potter', 2);


BEGIN TRANSACTION;  --dans le deuxieme terminal
INSERT INTO Reservation VALUES ('Gregoire','Happy Potter', 5);

--la 2eme ligne est bloqué à cause du trigger
    

BEGIN TRANSACTION;  -- dans le premier terminal
SET SESSION transaction ISOLATION LEVEL READ committed;

INSERT INTO Reservation VALUES ('Quentin','Happy Potter', 2);


BEGIN TRANSACTION;  --dans le deuxieme terminal
SET SESSION transaction ISOLATION LEVEL READ committed;

INSERT INTO Reservation VALUES ('Gregoire','Happy Potter', 5);

