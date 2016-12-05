'''
Created on Dec 3, 2016

@author: apple
'''
from Methods.Methods_BY_Level import MethodsMenu_Situation
from WN_User_Interact.InputANDError import InputCheck
from WN_User_Interact.Interaction_Modules import Mainmenu
def CollisionSituation(NYC):
    Interaction=Situation_Interaction(NYC)
    Level,Method,name,nameFlag=Interaction.Level_selection()
    
class Situation_Interaction():
    def __init__(self,NYC):
        self.menu=MethodsMenu_Situation()
        self.data=NYC
    def Level_selection(self,Level=[],Method=[],name=[],nameFlag=0):
        print("Available Perspectives: \n 1-City \n 2-Borough \n 3-Precinct \n 4-Highway \n 5-Tunnel \n 6-Bridge \n 7-Road")
        Level = input('Please input the number before the perspective you want to explore:')
        Level = InputCheck(range(1,8), Level)
        LevelFlow={-2:self.Level_selection,
                   -1:Mainmenu,
                   (1,2,3,4,5,6,7):self.MethodMenu}
    
        LevelName={-2:[],1:'City',2:'Borough',3:'Precinct',4:'Highway',5:'Tunnel',6:'Bridge',7:'Road'}
    
        LevelFlow[Level]() if Level==-1 else Level, Method, name, nameFlag=LevelFlow[Level](LevelName[Level])
        
        
        return Level, Method, name, nameFlag
       
    def MethodMenu(self,Level,Method=[],name=[],nameFlag=0):
        
        print("There are methods for this level:")
        print ('%s' % '\n'.join(self.menu.List[Level][nameFlag]))
        
        Method = input('Please input the number before the method you want to use:')
        Method = InputCheck(self.menu.AvailableSet[Level][nameFlag], Method)
        
        methodFlow={0:{-2:self.MethodMenu,
                       -1:self.Level_selection,
                       0:self.SpecificInsight,
                       (1,2,3,4,5,6):self.MethodPresent},
                    1:{-2:self.MethodMenu, #with name
                       -1:self.MethodMenu, #back to no name
                       (1,2,3,4,5,6):self.MethodPresent}}
        if ((nameFlag==1) and (Method==-1)):
            Level, Method, name, nameFlag = methodFlow[nameFlag][Method](Level, Method, [], 0)
        else:
            Level, Method, name, nameFlag = methodFlow[nameFlag][Method](Level, Method, name, nameFlag)
        
        return Level, Method, name, nameFlag
    def SpecificInsight(self,Level,Method=[],name=[],nameFlag=0):
        SpecificMenu={'Borough':self.menu.Borough_Specific,
                      'Precinct':self.menu.Precinct_Specific,
                      'Highway':self.menu.Highway_Specific,
                      'Bridge':self.menu.Bridge_Specific,
                      'Tunnel':self.menu.Tunnel_Specific,
                      'Road':self.menu.Road_Specific}
        
        InputName=SpecificMenu[Level](self.data)
        Level, Method, name, nameFlag=self.MethodMenu(Level) if InputName==-1 else Level, Method, name, nameFlag=self.MethodMenu(Level,[],InputName,1)
            
        return Level, Method, name, nameFlag
    def MethodPresent(self,Level,Method=[],name=[],nameFlag=0):
        self.menu.FunctionINIT_Situation(self.data)
        self.menu.FunctionList[Method](Level,name)
        Level, Method, name, nameFlag=self.MethodMenu(Level,[],name,nameFlag)
        return Level, Method, name, nameFlag
        