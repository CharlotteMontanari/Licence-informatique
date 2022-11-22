# Écrivez un jeu qui permet à un client de deviner un nbre aléatoire choisi par le serveur
# Le client indique le nombre maximum au serveur. 
# Le serveur demande un nombre au client et répond « plus » ou « moins ». 
# La connexion est terminée lorsque le nombre est trouvé.

import socket
import sys

HOST = '127.0.0.1'
PORT = 2003

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.connect((HOST, PORT))
except socket.error:
    print("La liaison du socket à l'adresse choisie a échoué")
    sys.exit()

#on décode ce qu'on reçoit
start = sock.recv(1024)
start = start.decode("UTF-8")
print(start)

#on envoi la limite
limit = input("Saissir une limite: ")
sock.send(limit.encode("UTF_8"))

start = sock.recv(1024)
start = start.decode("UTF-8")
print(start + "\n")

while start.strip() != "Bravo! Vous avez trouvé!\n":
    number_to_find = input("Nombre: ")
    sock.send(number_to_find.encode("UTF-8"))
    start = sock.recv(1024)
    start = start.decode("UTF-8")
    print(start)

sock.close()