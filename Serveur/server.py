import socket
import os
import glob
import time
import threading


class Server:
    def tcp_server_thread(self,port):
        # host="127.0.0.1"
        # port=port+100
        host = "127.0.0.1"
        port = 65432
        t = threading.Thread(target=self.tcp_server, args=(host, port))
        t.start()

    def tcp_server(self, host, port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((host, port))
        self.s.listen()
        print ("Server Started.")
        while True:
            conn, address = self.s.accept()
            print ("client connected ip:<" + str(address) + ">")
            #t1 = threading.Thread(target=self.)
            data = conn.recv(1024)
            print(data)


if __name__ == '__main__' :
    tcp=Server()
    tcp.tcp_server_thread(65432)
    #opt = input("Appuyez 3 pour fermer le server")
    #if(opt==3):
        


"""
HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
"""