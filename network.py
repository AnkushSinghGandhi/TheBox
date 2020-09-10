# importing socket
import socket

# creating a network class
class Network:
    def __init__(self):
        # AF_INET is an address family that is used to designate the type of addresses that your socket can communicate with (in this case, Internet Protocol v4 addresses). When you create a socket, you have to specify its address family,
        # SOCK_STREAM means that it is a TCP socket.
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # seting server address (this is the address of server not of the client)
        self.server = "localhost"
        # setting port no. (should be same as of server)
        self.port = 5555
        # creating a tuple of server and port no.
        self.addr = (self.server, self.port)
        # connect methode defined below
        self.pos = self.connect()

    def getpos(self):
        return self.pos
    
    # connect methode to connect to server and recieve data
    def connect(self):
        try:
            # trying to connect to server
            self.client.connect(self.addr)
            # decoding and returning data that server send
            return self.client.recv(2049).decode()

        except:
            pass
    
    # send method to send data back to server
    def send(self, data):
        try:
            # trying to encode and send data 
            self.client.send(str.encode(data))
            # recieving decoding data and returning it
            return self.client.recv(2048).decode()
        except socket.error as e:
            # printing the excepted error if any
            print(e)
