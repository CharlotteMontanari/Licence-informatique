# Écrivez un jeu qui permet à un client de deviner un nbre aléatoire choisi par le serveur
# Le client indique le nombre maximum au serveur. 
# Le serveur demande un nombre au client et répond « plus » ou « moins ». 
# La connexion est terminée lorsque le nombre est trouvé.

import socket
import sys
import random

HOST = '127.0.0.1'
PORT = 2003

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.bind((HOST, PORT))
except socket.error:
    print("La liaison du socket à l'adresse choisie a échoué")
    sys.exit()

print("Serveur en attente d'une connexion client...")
sock.listen(6)
call, connexion = sock.accept()
print("Un client s'est connecté avec l'adresse IP {} sur le port {}".format(connexion[0], connexion[1]))

#Début de la discussion
call.send("Commençons le jeu !\nQuel est la limite ?\n".encode("UTF-8"))
msg = call.recv(1024)
msg = msg.decode("UTF-8")
print(msg)

#On récupère le nombre qui a été envoyé
limit = int(msg)
number_to_find = random.randint(1, limit)

#On dit au client que le nombre est trouvé
call.send("Le jeu peut commencer !\n".encode("UTF-8"))

msg = call.recv(1024)
msg = msg.decode("UTF-8")
print(msg)

while int(msg) != number_to_find:
    if int(msg) > number_to_find:
        call.send("MOINS\n".encode("UTF-8"))
    else:
        call.send("PLUS\n".encode("UTF-8"))
    msg = call.recv(1024)
    msg = msg.decode("UTF-8")

#le nombre a été trouvé
call.send("Bravo! Vous avez trouvé!\n".encode("UTF-8"))
print("Fin du jeu")
call.close()