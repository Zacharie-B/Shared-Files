# coding: utf-8
import os


class File_Description:
    def __init__(self,name):
    #,description,size):
        self.name = name
        #self.description = description
        #self.size = size

    # fonction test
    """
    def get_description(self):
        return File_Description(self.name)
    """

    def get_name(self):
        return self.name

        
    # ouvrir un fichier et le lire
    def open_file_description(self):
        fil = open(self.name,'r')
        print(os.path.basename(self.name))
        for x in fil:
            print(x)
        fil.close()
    
""" 
x = File_Description("texte.txt")
x.open_file_description()
print(x.get_description())
""" 




