# importing bunch of stuff here
import socket
from _thread import *
import sys

# taking server and port
server = "localhost"
port = 5555

#--- CREATING A SOCKET---
# AF_INET is an address family that is used to designate the type of addresses that your socket can communicate with (in this case, Internet Protocol v4 addresses). When you create a socket, you have to specify its address family,
# SOCK_STREAM means that it is a TCP socket.
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# binding server and port no. to the socket
try:
    s.bind((server,port))
except socket.error as e:
    str(e)

# accepting incoming connections from clients, it only accepts 2 connections as we specified
s.listen(2)
# printing waiting for connections
print("Waiting for connections")

# function that convert positon string into a tuple
# for example "23,24" to (23,24)
def read_pos(str):
    # spliting the string from ","
    str = str.split(",")
    # returning tuple
    return int(str[0]), int(str[1])

# function to convert position tuple into a string
# reverse of read_pos()
def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])

# list that contains positions of player
pos = [(0,0),(100,100)]

def threaded_client(conn,player):
    # encoding and sending position of current player to the Network object
    conn.send(str.encode(make_pos(pos[player])))
    
    # reciveing and sending data between server and client
    while True:
        try:
            # revieving and converting pos into tuple
            data = read_pos(conn.recv(2048).decode())
            pos[player] = data

            # checking if server is recieving data or not
            if not data:
                # if server is not recieving data than printing disconnected and breaking from loop 
                print("Disconnected")
                break
            else:
                # sending player 1 pos. if current player is player no. 2
                if player == 1:
                    reply = pos[0]
                # sending player 2 pos. if current player is player no. 1
                else:
                    reply = pos[1]

                # printing recived reply
                print("Recieved", data)
                # printing sending reply
                print("sending..", reply)
            
                # encoding and sending the reply back to client
            conn.sendall(str.encode(make_pos(reply)))
        except:
            break
    print("Lost Connection")
    conn.close()

# no. of current players
currentplayer = 0

# creating a infinite loop so that clients can connect to server
while True:
    # Accept a connection. The socket must be bound to an address and listening for connections. The return value is a pair (conn, address) where conn is a new socket object usable to send and receive data on the connection, and address is the address bound to the socket on the other end of the connection.
    conn, addr = s.accept()
    # printing address of a client
    print("connected to:",addr)
    # creating a new thread to run "threaded_client" function in parallel and passing conn as an argument
    start_new_thread(threaded_client,(conn,currentplayer))
    # adding 1 player
    currentplayer += 1