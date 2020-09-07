import socket
from Thread import *
import sys

server = "localhost"
port = 5555

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    s.bind((server,port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for connections")

def threaded_client(conn):
    conn.send(str.encode("connected"))
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                print("Recieved", reply)
                print("sending..", reply)
            
            conn.sendall(str.encode(reply))
        except:
            break
    print("Lost Connection")
    conn.close()


while True:
    conn, addr = s.accept()
    print("connected to:",addr)

    start_new_thread(threaded_client,(conn,))