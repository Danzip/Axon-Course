from socket import *
import json
OK = 'OK'
GOODBYE = 'GOODBYE'
ALL = '*'
ERROR = 'ERROR'
UNKNOWN_COMMAND = 'Unknown command'
COMMANDS = {}
class Client:

    def __init__(self,socket=None,info_types=None,name=None):
        self.info_types=info_types
        self.socket=socket
        self.name=name
        if self.socket is None:
            self.create_socket()

    def add_info_type(self,infoType,value):
        self.info_types[infoType]=value

    def add_info_dict(self,infoDict):
        self.info_types.update(infoDict)


    def send_response(self,response):
        packed_response=json.dumps(response)
        print "packed response is {} type is {}".format(packed_response,type(packed_response))
        self.socket.send(packed_response)
        # response = self.receive()
        # if response!= OK:
        #     print "server issue"
        #     self.socket.close()
        #     return


    def handle_command(self, command_dict):
        if command_dict["command"]==["info_types"]:
           self.send_response({"info_types":self.info_types.keys()})
        elif command_dict["command"] in self.info_types.keys():
            print
            self.send_response({command_dict["command"] : self.info_types[command_dict["command"]]})
        elif command_dict == "*":
            self.send_response(self.info_types)
        elif command_dict== "disconnect":
            self.send_response({'disconnect':'OK'})
            return True
        else:
            self.send_response(['command invalid'])
        return False


    def create_socket(self,domain=AF_INET,type=SOCK_STREAM):
        new_socket=socket(domain,type)
        print new_socket
        self.socket=new_socket
        print self.socket

    def receive(self):
        response_packed=self.socket.recv(1024)
        return json.loads(response_packed)

    def send(self,data):
        self.socket.send(data)


    def connect(self,server_address):
        self.socket.connect(server_address)

    def handle_connection(self):
        server_address=('127.0.0.1',3030)
        self.connect(server_address)
        self.send_response({"name":self.name})
        response=self.socket.recv(1024)
        if response != OK:
            print "error{}".format(response)
            return
        print "{}".format(response)


        self.send_response(self.info_types.keys())

        while True:
            command=self.receive()
            #print server_command_packed
            #unpacked_command=json.loads(server_command_packed)
            quit_connection=self.handle_command(command)
            if quit_connection:
                self.socket.close()
                break
        pass

info_types={"os_type": "Linux Ubuntu 16.04.1",
  "users": ["bob"],
  "processes": ["python", "chrome"],
  "ports": ["8000","12345"],
  "storage_usage": "2.5T",
  "gpu_type": ["GeForce GTX 1080 Ti", "GeForce GTX 1080 Ti"]}
name="Daniel2"
#address='10.35.77.221',port=3030


c=Client(info_types=info_types,name=name)

c.handle_connection()








