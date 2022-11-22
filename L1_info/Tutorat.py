import pocketgl as pg
import time

class Terrain:
    def __init__(self, n_lig, n_col):
        self.n_lig = n_lig
        self.n_col = n_col
        self.tableau = [['white'] * n_col for _ in range(n_lig)]
        #print(self.tableau)

    def affichage(self, dim=100):
        for i in range(self.n_lig):
            for j in range(self.n_col):
                #print(self.tableau[i][j])
                pg.current_color(self.tableau[i][j])
                dx = j*dim
                dy = i*dim
                pg.box(dx, dy, dx + dim, dy + dim)
                #print (dx, dy, dx + dim, dy + dim)

    def changer_couleur_case(self, x, y):
        if self.tableau[x-1][y-1] == "black":
            new_col= "white"
        else:
            new_col= "black"
        self.tableau[x-1][y-1] = new_col
        print ("Couleur changee:",new_col, "en: ", x, y)
        #print(self.tableau)

class Fourmis:
    droite = {
        'N':(1,0), 
        'E':(0,-1), 
        'S':(-1,0), 
        'O':(0,1)
        }
    gauche = {
        'N':(-1,0), 
        'E':(0,1), 
        'S':(1,0), 
        'O':(0,-1)
        }   

    def __init__(self, x, y, direction="O"):
        self.x = x
        self.y = y
        self.direction = direction
    
    def tourne_droite(self):
        if self.direction == "N":
            return 1, 0, "E"
        elif self.direction == "E":
            return 0, -1, "S"
        elif self.direction == "S":
            return -1, 0, "0"
        else:
            return 1, 0, "N"

    def tourne_gauche(self):
        if self.direction == "N":
            return 1, 0, "E"
        elif self.direction == "E":
            return 0, -1, "S"
        elif self.direction == "S":
            return -1, 0, "0"
        else:
            return 1, 0, "N"

    def deplacement(self, terr):
        couleur = terr.tableau[self.x-1][self.y-1]
        if couleur == 'black':
            new_x, new_y, new_direction = self.tourne_droite()
        else:
            new_x, new_y, new_direction = self.tourne_gauche()
        #print(self.x+new_x, self.y+new_y)
        
        # On teste si on sort pas de l'écran
        if self.x+new_x <= terr.n_col and self.x+new_x>= 0 and self.y+new_y <= terr.n_lig and self.y+new_y >= 0:
            terr.changer_couleur_case(self.x, self.y)
            print(f"on bouge vers {new_direction}")
            self.x = self.x + new_x
            self.y = self.y + new_y
            self.direction = new_direction
            return True
        else:
            print("on bouge plus")
            return False

n_col, n_lig = 3, 3
pg.init_window("Projet_tutorat", n_col * 100, n_lig * 100)

terr = Terrain(n_col, n_lig)
fourm = Fourmis(1,2)

on_continue = True
while on_continue:
    terr.affichage()
    on_continue = fourm.deplacement(terr)
    pg.refresh()
    time.sleep(2)

pg.main_loop()

