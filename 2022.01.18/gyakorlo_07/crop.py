
from typing import List
from cropModel import CropModel

class Crop:
    def __init__(self):
        self.file_name= "termes.txt"
        self.crops=[]

    def read_content(self):
        fp=open(self.file_name,"r",encoding="utf-8")
        self.lines=fp.readlines()
        fp.close
        #print(lines)
    
    def convert_content(self):
        for line in self.lines[1:]:
            (id,name,place,size,cropyield,year)=line.split(":")
            #print(name)
            cropModel= CropModel(self,id,name,place,size,cropyield,year)
            self.crops.append(cropModel) 

    def more_than_three_hundred():
        for 
        pass


crop=Crop()

crop.read_content()
crop.convert_content()