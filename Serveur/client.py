import socket
import select

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

username =  input("Rentrez votre username " )
username=username+" "
password = input("Rentrez votre password ")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(username.encode())
    s.sendall(password.encode())

#print(f"Received {data!r}"