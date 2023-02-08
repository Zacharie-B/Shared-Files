import socket
import select

"""
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

"""
class LocalClient:
    def __init__(self, port_number, ip_address="127.0.0.1"):
        self.ip_address = ip_address
        self.port_number = port_number

    def get_username(self):
        username = input("Rentrez votre username ")
        return username+" "

    def get_password(self):
        password = input("Rentrez votre password ")
        return password
        
    def get_port_number(self):
        return self.port_number

    def get_ip_address(self):
        return self.ip_address
    
    def connect(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.ip_address, self.port_number))
        usr = self.get_username()
        psw = self.get_password()
        self.s.sendall(usr.encode())
        self.s.sendall(psw.encode())

if __name__ == '__main__':
    port = 65432
    host = "127.0.0.1"
    client = LocalClient(port,host)
    client.connect()

    




#print(f"Received {data!r}
