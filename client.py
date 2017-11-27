from socket import *
import json

class Client:

    def __init__(self,socket=None,info_types=None):
        self.info_types=info_types
        self.socket=socket
        if socket is None:
            self.socket=self.create_socket()

    def add_info_type(self,infoType,value):
        self.info_types[infoType]=value

    def add_info_dict(self,infoDict):
        self.info_types.update(infoDict)


    def send_response(self,response):
        packed_response=json.dumps(response)
        self.socket.send(packed_response)


    def handle_command(self, command_dict):
        if command_dict["command"]==["info_types"]:
           self.send_response({"info_types":self.info_types.keys()})
        elif command_dict in self.info_types.keys():
            self.send_response({command_dict : self.info_types[command_dict]})
        elif command_dict == "*":
            self.send_response(self.info_types)
        elif command_dict== "disconnect":
            self.send_response({'disconnect':'OK'})
            return True
        else:
            self.send_response(['command invalid'])
        return False


    def create_socket(self,domain=AF_INET,type=SOCK_STREAM):
        self.socket=socket(domain,type)

    def receive(self):
        return self.socket.recv(1024)

    def send(self,data):
        self.socket.send(data)


    def connect(self,address=gethostname(),port=5656):
        self.socket.connect((address,port))

    def handle_connection(self,address=gethostname(),port=5656):
        self.connect(address,port)
        while True:
            server_command_packed=self.receive()
            unpacked_command=json.loads(server_command_packed)
            quit_connection=self.handle_command(unpacked_command)
            if quit_connection:
                self.socket.close()
        pass

info_types={"os_type": "Linux Ubuntu 16.04.1",
  "users": ["bob"],
  "processes": ["python", "chrome"],
  "ports": ["8000","12345"],
  "storage_usage": "2.5T",
  "gpu_type": ["GeForce GTX 1080 Ti", "GeForce GTX 1080 Ti"]}

c=Client(info_types=info_types)
c.handle_connection()








