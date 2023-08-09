import socket
import sys
import datetime

#je rentre l'adresse ip (ici, mon local host) vers laquelle j'écoute
HOST = '127.0.0.1'
#j'ai utilié également un port non utilisé et non connu afin de m'y connecter
PORT = 4567

#ici, dans la varible sock, j'établie une connexion ipv4 sur le port TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#dans le try, on met notre serveur en attente de la connexion 
#du host qu'on a rentré plus haut et du port
try:
    sock.bind((HOST, PORT))
#dans le except, on renvoie un message d'erreur si la connexion a échoué
except socket.error:
    print("La liaison du socket à l'adresse choisie a échoué")
    sys.exit()

#pour un affichage plus clair, j'affiche ce message afin d'attendre la connexion
print("Serveur en attente d'une connexion client...")
#ici, on autorise 6 connexions successives avant de couper la connexion
sock.listen(6)
#avec ces deux variables, je recupère l'adresse ip et le port avec laquelle la machine s'est connecté
call, connexion = sock.accept()
print("Un client s'est connecté avec l'adresse IP {} sur le port {}\n".format(connexion[0], 
                                                                            connexion[1]))

#on envoie notre première question que l'on encode
#pour les réponses qui nous seront envoyées par le client
#on les stocks dans trois variables: jour, mois et annee afin de faciliter le calcul de l'age
call.send("Bonjour, quelle est votre date de naissance ?\n".encode('UTF-8'))
#dans jour, on récupère le jour de naissance avec une possibilité de 1024 octects pour recevoir le message
jour = call.recv(1024)
#on décode à chaque fois
jour = jour.decode('UTF-8')
#et on affiche dans le terminal la conversation
print('Client: Jour: ', jour, '\n')

mois = call.recv(1024)
mois = mois.decode('UTF-8')
print('Client: Mois: ', mois, '\n')

annee = call.recv(1024)
annee = annee.decode('UTF-8')
print('Client: Année: ', annee)
#et on continue avec mois et année
#on reçoit, on décode, on affiche

#afin de faire le calcul de l'age, on stock ce qu'on a récupéré 
#on le transtype ensuite vers un int pour faire les calculs
j = int(jour)
m = int(mois)
a = int(annee)

#grace au module time, on récupère la date du jourqu'on stock dans d
d = datetime.date.today()
#on test d'abord que l'on soit "nait", si ce n'est pas le cas, l'age est égale à 0
if d.year < a:
    age = 0
else:
    #sinon, si le mois actuel est inférieur au mois de naissance
    #c'est que ce n'est pas notre anniversaire
    if d.month < m:
        #on faire donc l'année actuelle - celle de naissance et le tout -1
        age = (d.year - a) - 1
    #si par contre, on est sur le mois de notre anniversaire, on va donc tester si le jour est bon
    elif d.month == m:
        #si le jour actuel est supérieur à notre jour d'anniversaire, il est donc passé
        if d.day >= j:
            #on fait donc bien l'année actuelle - celle de notre naissance
            age = d.year - a
        else:
            #sinon, c'est que le jour n'est pas encore passé
            age = (d.year - a) - 1
    else:
        #si on est supérieur au mois actuel, on a passé notre anniversaire
        age = d.year - a

#en avant dernière étape, on envoie donc le calcul de l'age
call.send("\nVous avez {} ans\n".format(age).encode('UTF-8'))

#on finit enfin par fermer toutes les connexions
call.close()
sock.close()