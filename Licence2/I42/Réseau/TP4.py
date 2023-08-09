import socket
import sys

#dans la variable host, on rentre notre localhost
HOST = '127.0.0.1'
#on utilise le port 2003 qui n'est défini nul part
PORT = 2003

#créer une connexion tcp et ipv4
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#ici, le serveur attend une connection avec le client
try:
    #bind permet d'établir une connexion entre une adresse ip et un port
    mySocket.bind((HOST, PORT))
except socket.error:
    print("La liaison du socket à l'adresse choisie a échoué.")
    sys.exit()

while 1:
    print("serveur simple en attente...")
    #listen permet de mettre le socket en attente de connexion
    mySocket.listen(5)

    #accept permet la connexion d'un appel entrant
    connexion, adresse = mySocket.accept()
    print("Un client est connecté depuis l'adresse IP {} et le port {}".format(
           adresse[0], adresse[1]))

    connexion.send(("Vous êtes connecté au serveur " + HOST + ":" + str(PORT) +
                    ".\n").encode('UTF-8'))

    while 1:
        # envoi de la question au client
        connexion.send("Votre message ?\n".encode('UTF-8'))
        # attente de la reponse
        msgClient = connexion.recv(1024)
        # le message est converti d'une tableau d'octets en chaine de caractères
        msgClient = msgClient.decode("utf-8")

        # si la reponse est FIN ou un ligne vide, le dialogue d'arrête.
        if msgClient.upper().strip() == "FIN" or msgClient.strip() == "":
            break

        # traitement de la réponse
        # le serveur affiche sur sa console
        print("reçu du client>"+msgClient+"<")
        # et envoi un echo au client
        connexion.send(("ECHO : " + msgClient).encode('UTF-8'))

    connexion.send("Good Bye.".encode('UTF-8'))
    print("Connexion interrompue.")
    # Le serveur ferme la connexion
    connexion.close()

    ch = input("Attendre un autre client ? R(ecommencer)/T(erminer) ? ")
    if ch.upper() == 'T':
        break