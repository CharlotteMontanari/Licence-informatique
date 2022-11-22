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

msg = sock.recv(1024)
msg = msg.decode('UTF-8')
print('Serveur: ', msg)

x = input("Serveur: Saissir votre jour de naissance: ")
sock.send(x.encode('UTF-8'))

y = input("Serveur: Saissir votre mois de naissance: ")
sock.send(y.encode('UTF-8'))

z = input("Serveur: Saissir votre année de naissance: ")
sock.send(z.encode('UTF-8'))

age = sock.recv(1024)
age = age.decode('UTF-8')
print(age)

sock.close()