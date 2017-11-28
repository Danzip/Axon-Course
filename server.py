from socket import *
import thread
import json

OK = 'OK'
GOODBYE = 'GOODBYE'
ALL = '*'
ERROR = 'ERROR'
UNKNOWN_COMMAND = 'Unknown command'
COMMANDS = {}


class Client(object):
    def __init__(self,name=None,commands={},client_socket=None,next_command=None):
        self.name=name
        self.commands=commands
        #self.ip=ip
        #self.port=port
        self.client_socket=client_socket
        self.next_command=next_command

    def add_name(self,name):
        self.name=name

    def add_commands(self,commands):
        self.commands=commands

    def assign_command(self,command):
        self.next_command=command




class Server(object):
    def __init__(self,address='10.35.77.221',port=3030,server_socket=None,clients={}):
        self.port=port
        self.address=address
        self.server_socket=server_socket
        self.clients=clients
        #self.run_server()

    def add_client(self,clientDict):
        self.clients.update(clientDict)

    def create_socket(self, domain=AF_INET, type=SOCK_STREAM):
        new_socket = socket(domain, type)
        new_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        print new_socket
        self.server_socket = new_socket
        print self.server_socket


    def bind(self):

        self.server_socket.bind((self.address,self.port))

    def accept(self):
        print "accepting connection"
        while True:
            client_socket,client_address = self.server_socket.accept()
            print client_socket
            new_client=Client(client_socket=client_socket)
            #self.clients.append(new_client)
            thread.start_new_thread(self.handle_connection,(new_client,))

    def listen(self, backlog=5):
        self.server_socket.listen(backlog)

    def send_response(self, response,client):
        packed_response = json.dumps(response)
        client.client_socket.send(packed_response)

    def recieve_response(self, client):
        packed_response = client.client_socket.recv(1024)
        print "packed response is {} type is {}".format(packed_response,type(packed_response))
        unpacked_response=json.loads(packed_response)
        print  "unpacked response is {} type is {}".format(unpacked_response,type(unpacked_response))
        return unpacked_response


    def handle_connection(self,new_client):
        print "handling connection"
        name=self.recieve_response(new_client)
        #print name
        new_client.add_name(name)
        #print new_client.name
        self.send_response(OK,new_client)
        commands=self.recieve_response(new_client)
        print commands
        self.send_response(OK, new_client)
        #print commands
        new_client.add_commands(commands)
        #print new_client.commands
        #print new_client.name
        self.add_client({name:new_client})
        print (self.clients[new_client.name].name)
        while new_client.next_command!=GOODBYE:
            if new_client.next_command!=None:
                print "sending command:{}".format(new_client.next_command)

                self.send_response({"command":new_client.next_command},new_client)
                new_client.next_command=None
        new_client.socket.close()

        #write I/O

    def handleIO(self):
        while True:
            print "handling IO"
            for client in self.clients:

                print "clients to interact with {}".format(self.clients[client].name)
            client_name=raw_input("choose a client to interact with x for exit\n")
            if client_name in self.clients.keys():
                print "client exists"
                client=self.clients[client_name]

                print "client commands are{}".format(client.commands)
                for command in client.commands.keys():
                    print "{}".format(command)
                chosen_command=raw_input("choose command to send to {}".format(client_name))
                if chosen_command in client.commands.keys():
                    print "assigning command"
                    client.assign_command(chosen_command)
            elif client_name =='x':
                break



            #
            # clientCommandDict= raw_input("Enter client name and command in dictionary format")
            # name=clientCommandDict.keys()
            # if len(clientCommandDict)==1 and name in self.clients and clientCommandDict[name] in self.clients[name]:



    def run_server(self):
        self.create_socket()
        self.bind()
        self.listen()
        thread.start_new_thread(self.handleIO,())
        thread.start_new_thread(self.accept())


        #   my_recv()
server=Server()
try:
    server.run_server()
except KeyboardInterrupt:
    print "asd"
    server.server_socket.close()





#def my_recv():
 #   pass
