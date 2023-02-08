import socket
import os
import glob
import time
import threading
import sys 
import errno
import select



class Server:
    def tcp_server_thread(self,port):
        host = "127.0.0.1"
        port = 65432
        t = threading.Thread(target=self.tcp_server, args=(host, port))
        t.start()

    def login(self,msg):
        host = "127.0.0.1"
        #host = ""
        port = 60000
        self.s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s1.connect((host,port))
        self.s1.send(b"1001 ") #statut code pour envoyer les infos utilisateur
        msg[0] = msg[0]+" "
        self.s1.send(msg[0].encode())
        self.s1.send(msg[1].encode())
        self.s1.close()
    

    def tcp_server(self, host, port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((host, port))
        self.s.listen()
        while True:
            conn, address = self.s.accept()
            print("Code Statut 2001 : Serveur lancé.\nLe client peut envoyer des recherches")
            print ("client connected ip:<" + str(address) + ">")
            m = conn.recv(1024).decode()
            m_split = m.split(" ")

            for i in range(len(m)):
                if m[i] == " " :
                    message1 = m.split()  
            print("Username reçu :",m_split[0],"\nPassword reçu :",m_split[1])

            
            self.login(m_split)
            print("Authentification réussie(pas encore il manque le cryptage)")
            sub_dir = os.getcwd()+"/Repertoire/"
            fileName = input("Entrez le nom du fichier : ")
            self.envoyer_fichier(sub_dir,fileName)
            print("Serveur a envoyé le fichier : ",fileName)
            #self.s.close()
            #t1 = threading.Thread(target=self.login,args=(m_split,))
            #t1.start()
    
    def envoyer_fichier(self,filePath,fileName):
        #print(os.getcwd()+"/Repertoire/")
        #print("\n\nLa liste des fichiers dispos : \n",os.listdir(filePath))
        host = "127.0.0.1"
        port = 60000
        self.s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s1.connect((host,port))
        self.s1.send(b"4001 ")#statut code pour envoyer les descriptions de fichiers
        fn = fileName+" "
        self.s1.send(fn.encode()) 
        #if os.path.isFile(filePath+fileName):
        txt = open(filePath+fileName, 'rb')
        data = txt.read(1024)
        while data:
            self.s1.send(data)
            data = txt.read(1024)
        pv = ";"
        self.s1.send(pv.encode())
        self.s1.close()
  


if __name__ == '__main__' :
    #print("TODO : \n","utiliser classe file_to_share si possible pr l'envoi de fichier \nStocker les infos utilisateur du serveur centralise dans un dict ou list\n")
    #msg = "hello"
    tcp=Server()
    #tcp.login(60000,msg)
    tcp.tcp_server_thread(65432)
    #opt = input("Appuyez 3 pour fermer le server")
    #if(opt==3):
        
