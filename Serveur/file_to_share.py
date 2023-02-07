# coding: utf-8
from file_description import File_Description

class File_To_Share(File_Description):
    def __init__(self,name,file_description):
        self.name = name
        self.file_description = file_description
        #super().__init__(name,)
    
    def get_name(self):
        return self.name
    
    def get_file_description(self):
        return self.file_description


#TEST
"""
x = File_Description("texte.txt") #on crée une description de fichier
y = File_To_Share(x.get_name(),x) #on crée un fichier à partager 
ok = y.get_file_description() #on get la description de fichier
print(ok.open_file_description()) #on l'ouvre et on la lit
"""