from socket import *
import thread
import json

def handle_connection(socket):
    while True:
        command=json.dumps({"command": ["info_types"]})

        socket.send(command)
        r=socket.recv(1024)
        print r
 #   my_recv()


server_socket=socket(AF_INET,SOCK_STREAM)
server_socket.bind((gethostname(),5656))
server_socket.listen(5)
client_sockets=[]
while True:
    (client_socket,address)=server_socket.accept()

    thread.start_new_thread(handle_connection,(client_socket,))




#def my_recv():
 #   pass
