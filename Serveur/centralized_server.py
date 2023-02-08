import socket
import threading
import logging


class Centralized_Server:
    # initialise le serveur
    def __init__(self):
        port = 60000
        #logging.info('Initializing Server')
        #self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #self.sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.sock.bind(("127.0.0.1", port))
        #self.sock.bind(("", port))

    # ecoute le client
    def listen_server(self):
        self.sock.listen()
        while True:
            c, address = self.sock.accept()
            #c, address = self.sock.recvfrom(1024)
            print ("Server connected ip:<" + str(address) + ">\n")
            m = c.recv(1024).decode()
            m_split = m.split(" ")
            #print(m_split)
            if int(m_split[0]) == 1001 :
                print("Code Statut 1001 : Serveur centralisé reçoit les infos utilisateurs.\n")
                print("On stock l'utilisateur :",m_split[1],"\net son mdp :",m_split[2])
            #print((m_split))
            elif int(m_split[0]) == 4001 :
                print("Code Statut 4001 : Serveur centralisé reçoit les fichiers")
                m_notsplit = m_split[2:len(m)]
                m_notsplit = " ".join(m_notsplit)
                print("Fichier reçu : ",m_split[1], "\n",m_notsplit)
            #logging.info('Received data from client %s: %s', address, c)
        #t = threading.Thread(target=self.talkToClient, args=(address, c,))
        #t.start()

    def talk_toClient(self, msg, ip):
        if '|' not in msg:
            # print "We got connection from " , ip
            self.sock.sendto("You are connected\n", ip)
        else:
            print("ok fin du talk to client\n")

    def get_password():
        return password


if __name__ == '__main__':
    # Make sure all log messages show up
    logging.getLogger().setLevel(logging.DEBUG)
    server = Centralized_Server()
    server.listen_server()
