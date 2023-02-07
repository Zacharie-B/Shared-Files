import socket
import threading
import logging


class Centralized_Server:
    # initialise le serveur
    def __init__(self):
        logging.info('Initializing Server')
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(("127.0.0.1", 65432))

    # ecoute le client
    def listen_client(self):
        while True:
            c = self.sock.recv(128)
            address = self.sock.recv(128)
            logging.info('Received data from client %s: %s', address, c)
            t = threading.Thread(target=self.talkToClient, args=(address, c,))
            t.start()

    def talk_toClient(self, msg, ip):
        if '|' not in msg:
            # print "We got connection from " , ip
            self.sock.sendto("You are connected\n", ip)
        else:
            # print "inside talk client loop"
            # msg, add = self.sock.recvfrom(128)
            print msg
            m2 = msg.split("\r\n")
            pack_seq = m2[len(m2)-1]
            m3 = m2[0].split("|")
            # print "####"+m2[0]
            client_name = m3[1]
            client_address[client_name] = ip
            """
            qtype = self.checkquery(msg)
            if qtype == '1':
                self.updatedict( msg, ip, pack_seq )
            elif qtype == '2':
                self.searchkey(msg, ip, pack_seq)
            elif qtype == '3':
                self.removeclient(client_name, ip, pack_seq)
            else:
                self.sock.sendto("400 | Bad request",ip)
                #print "invalid request"
            """
            print("ok fin du talk to client\n")

    def get_password():
        return password


if __name__ == '__main__':
    # Make sure all log messages show up
    logging.getLogger().setLevel(logging.DEBUG)
    # direct = dict()
    # size = dict()
    # client_address = dict()
    server = Centralized_Server()
    server.listen_client()
