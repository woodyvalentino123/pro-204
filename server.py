import socket
from threading import Thread

server = None
IP_ADDRESS = '127.0.0.1'
PORT = 6000

CLIENTS = {}


def acceptConnections():
    global CLIENTS
    global server

    while True:
        player_socket, addr = server.accept()

        # --------- Student code here
        player_name=player_socket.recv(1024).decode().strip()

        # --------- Student code here
        if(len(CLIENTS.keys())==0):
            CLIENTS[player_name]={'player_type':'player1'}
        else:
            CLIENTS[player_name]={'player_type':'player2'}
        
        CLIENTS[player_name]["player_socket"]=player_socket
        CLIENTS[player_name]["address"]=addr
        CLIENTS[player_name]["player_name"]=player_name
        CLIENTS[player_name]["turn"]=False

        print(f"Connection established with {player_name}:{addr}")

def setup():
    print("\n\t\t\t\t\t**** Welcome To The Tambola Game")


    global server
    global PORT
    global IP_ADDRESS



    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP_ADDRESS,PORT))

    server.listen(10)

    print("\t\t\t\tSERVER IS WAITING FOR INCOMING CONNECTIONS....\n")
    acceptConnections()

setup()
    



