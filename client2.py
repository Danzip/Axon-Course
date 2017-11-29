import socket
import json


## Constants
my_name = 'ohad'

server_ip = '127.0.0.1'
server_port = 3030
server_addr = (server_ip, server_port)

OK = 'OK'
GOODBYE = 'GOODBYE'
ALL = '*'
ERROR = 'ERROR'
UNKNOWN_COMMAND = 'Unknown command'
COMMANDS = {}


## Commands
def uname():
    import platform
    system, node, release, version, machine, processor = platform.uname()
    return {'system': system,
            'node': node,
            'release': release,
            'version': version,
            'machine': machine,
            'processor': processor}
COMMANDS['OS_NAME'] = uname

def whoami():
    import getpass
    username = getpass.getuser()
    return {'username': username}
COMMANDS['USERS'] = whoami


## The Client
def log(text):
    print text


def main():
    # create a tcp socket (SOCK_STREAM) over ip protocol (AF_INET)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect to the server
    log('Trying connecting to {}:{}'.format(*server_addr))
    client.connect(server_addr)
    log('Connected!')

    # send my name
    data = json.dumps({'name': my_name})
    log("Sending {} to server".format(data))
    client.sendall(data)

    # wait for response
    response = client.recv(4096)
    if response != OK:
        log("Got error: {}".format(response))
        return
    log("Got {}".format(OK))

    # send my commands
    json_encoded = json.dumps(COMMANDS.keys())
    log("Sending {} to server".format(json_encoded))
    client.sendall(json_encoded)

    # start receiving commands from server
    log("Waiting for commands from server")
    command = client.recv(4096)
    while command != GOODBYE:
        log('Got commnad: {}'.format(command))

        if command in COMMANDS:
            data = {command: COMMANDS[command]()}
        elif command == ALL:
            data = {command: COMMANDS[command]() for command in COMMANDS}
        else:
            data = {ERROR: UNKNOWN_COMMAND}

        json_encoded = json.dumps(data)
        log('Send response: {}'.format(json_encoded))
        client.sendall(json_encoded)

        log("Waiting for commands from server")
        command = client.recv(4096)

    log("Got goodbye from server. Close connection!")
    client.close()


if __name__ == '__main__':
    main()
