import numpy as np

class Sports:
    
    
    def __init__(self,Sports,Type=""):
        self.Type = Type
        self.legends=[]
    
    def addLegends(self):
        lname=input("Enter the player name: ")
        isPlaying=input(" Is the player currently active (Y/N)")
        if isPlaying=='Y':
            isPlaying="Active"
        else:
            isPlaying="Retired"
        self.legends.append([lname,isPlaying])
        print("")
            
    def showLegends(self):
        print(self.legends)
        
    def showDetails(self):
        print("Game Type :",self.Type)
        print("Legends :",self.legends)
        
class Indoors(Sports):
    
    def __init__(self,name,playersReq,equipment,countryOfOrigin,Type="Indoors",time_duration=np.Inf):
    
        
        self.name = name
        self.time_duration = time_duration
        self.playersReq = playersReq
        self.equipment=equipment
        self.countryOfOrigin=countryOfOrigin
        super().__init__(self,Type)
    
    def showDetails(self):
        print("Game Type :",self.Type)
        print("Sport Name :",self.name)
        print("Legends :",self.legends)
        print("Country Of Origin :",self.countryOfOrigin)
        
        
        
class Outdoors(Sports):
    
    def __init__(self,name,playersReq,equipment,countryOfOrigin,Type="Outdoors",time_duration=np.Inf):
    
        Sports.__init__(self,Type)
        self.name = name
        self.time_duration = time_duration
        self.playersReq = playersReq
        self.equipment=equipment
        self.countryOfOrigin=countryOfOrigin
    
    def showDetails(self):
        print("Game Type:",self.Type)
        print("Sport Name :",self.name)
        print("Legends :",self.legends)
        print("Country Of Origin :",self.countryOfOrigin)
        
class Cricket(Outdoors):
    def __init__(self,overs,equipment,countryOfOrigin,name="Cricket",playersReq=22,Type="Outdoors",time_duration=np.Inf):
        
        Outdoors.__init__(self,name,playersReq,equipment,countryOfOrigin,Type,time_duration)
        self.time_duration = time_duration
        self.playersReq = playersReq
        self.equipment=equipment
        self.countryOfOrigin=countryOfOrigin
        self.overs=overs
        
    def showDetails(self):
        print("Game Type :",self.Type)
        print("Sport Name :",self.name)
        print("Legends",self.legends)
        print("Country Of Origin :",self.countryOfOrigin)
        print("Players Required :",self.playersReq)
    
        
class T20(Cricket):
    def __init__(self,equipment,countryOfOrigin,overs=20,name="Cricket",playersReq=22,Type="Outdoors",time_duration=3):
        Cricket.__init__(self,overs,equipment,countryOfOrigin,name,playersReq,Type,time_duration)
        
    def showDetails(self):
        print("Game Type :",self.Type)
        print("Sport Name :",self.name)
        print("Legends",self.legends)
        print("Overs : 20")
        print("Time Duration : 3 hours")
        print("Country Of Origin :",self.countryOfOrigin)
        print("Players Required :",self.playersReq)
    
class OneDay(Cricket):
    def __init__(self,equipment,countryOfOrigin,overs=50,name="Cricket",playersReq=22,Type="Outdoors",time_duration=8):
        Cricket.__init__(self,overs,equipment,countryOfOrigin,name,playersReq,Type,time_duration)
    
    def showDetails(self):
        print("Game Type :",self.Type)
        print("Sport Name :",self.name)
        print("Legends",self.legends)
        print("Overs : 50")
        print("Time Duration : 8 hours")
        print("Country Of Origin :",self.countryOfOrigin)
        print("Players Required :",self.playersReq)
        
class TestMatch(Cricket):
    def __init__(self,equipment,countryOfOrigin,overs=90,name="Cricket",playersReq=22,Type="Outdoors",time_duration=30):
        Cricket.__init__(self,overs,equipment,countryOfOrigin,name,playersReq,Type,time_duration)

    def showDetails(self):
        print("Game Type :",self.Type)
        print("Sport Name :",self.name)
        print("Legends",self.legends)
        print("Overs : 90")
        print("Time Duration : 5 days (6 hrs/day)")
        print("Country Of Origin :",self.countryOfOrigin)
        print("Players Required :",self.playersReq)

t20match=T20(equipment=['bat','ball','wickets'],countryOfOrigin="England")
print(t20match.overs)
t20match.addLegends()
t20match.showDetails()
print("")
chess=Indoors(name="Chess",playersReq=2,equipment=['chess board','chess coins'],countryOfOrigin='India',Type="Indoors",time_duration=np.Inf)
chess.addLegends()
chess.showDetails()