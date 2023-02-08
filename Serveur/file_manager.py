# coding: utf-8
from file_to_share import File_To_Share
from file_description import File_Description

class File_Manager:
    # repertoire de file description
    directory = []
    
    # getter de file à partager
    """
    def download_fileshare(file_to_share):
        self.file_to_share = File_To_Share()
        return file_to_share
    """
    def get_directory(self):
        return self.directory

    def add_file_to_directory(self,file_share):
        self.directory.append(file_share)

    def add_fd_to_directory(self,file_description):
        self.directory.append(file_description)
    

#TEST
"""
x = File_Description("texte.txt") #on crée une description de fichier
y = File_To_Share(x.get_name(),x) #on crée un fichier à partager 

fm = File_Manager()
fm.add_fd_to_directory(x)
fm.add_file_to_directory(y)

repertoire = fm.get_directory()
repertoire[0].open_file_description()
print("ceci est une description de fichier")
print(repertoire[1].get_name(),"ceci est un fichier a partager")
"""