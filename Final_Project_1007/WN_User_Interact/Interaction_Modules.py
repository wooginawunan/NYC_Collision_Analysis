#!/usr/local/bin/python2.7
# encoding: utf-8
'''
WN_User_Interact.Interaction_Modules -- shortdesc

WN_User_Interact.Interaction_Modules is a description

It defines classes_and_methods

@author:     user_name

@copyright:  2016 organization_name. All rights reserved.

@license:    license

@contact:    user_email
@deffield    updated: Updated
''' 

from CheckandError.Check import InputCheck,DateCheck
#from .CollisionSituation import CollisionSituation
from WN_struct_building import StructureBuilding
from Methods.Methods_BY_Level import MethodsMenu_Situation
from CheckandError.DefinedError import DATEEndBeforeBegin,InvalidDate,ExitALLProgram
def ProgramIntroduction():
    print('Welcome to NYC Motor Vehicle Collisions Observation System.')
    print('We provide an analysis of the historical trends and features of auto collision \n and other associated demographic and geographic information in NYC. \n There is also an interactive maps which may help you better observe \n the whole traffic collision situation in NYC.')
    print('DATA SOURCE:')
    print('DATA INTRODUCTION:')
    print("COPY RIGHT:")
    print("FUNCTIONS")
    print('EXIT WAY')
    print('HELP MENUAL')
    print("We have several perspectives for your to explore.They are in two categories:")
    print("Area: City; Borough; Precinct")
    print("Type of Roadways: Highway; Tunnel; Bridge; Road")
    print("There are available methods under the specific perspective.")
    print("Input Examples: ")
    print("...")
    print("Exit by input : Exit")
    print("Now you can begin with it.")
def SetTimeInterval():
    print("You can set the period.")
    while True:
        try:
            print("ALL DATA is in 201501-201612.")
            begintime=input('Please input the begining date (Format: YYYYMM, Example: 201501):')
            if begintime=='Exit':
                raise ExitALLProgram
            endtime=input('Please input the ending date (Format: YYYYMM, Example: 201501):')
            if endtime=='Exit':
                raise ExitALLProgram
            TimeBegin,TimeEnd=DateCheck(begintime, endtime)
            return TimeBegin,TimeEnd
        except DATEEndBeforeBegin:
            print("Begining date should not later than ending date!")
        except InvalidDate:
            print("Invalid Input!")
    
def Mainmenu():
    TimeBegin,TimeEnd = SetTimeInterval()
    NYC = StructureBuilding(TimeBegin,TimeEnd)
    #print(NYC.Borough_Dict)
    print("There are three types of information: \n 1-CollisionSituation \n 2-CollisionContributingFactors_Vehicle \n 3-CollisionSimulation")
    InformationType = input("You can choose one by input the number before the type above:")
    MenuInformation={-2:Mainmenu, 
                     -1:Mainmenu,
                     1:CollisionSituation,
                     2:CollisionContributingFactors_Vehicle,
                     3:CollisionSimulation}
    inputset=MenuInformation.keys()
    InformationType = InputCheck(inputset, InformationType)
    if InformationType>0:
        MenuInformation[InformationType](NYC)
    else:  
        MenuInformation[InformationType]()
    #MenuInformation[InformationType](NYC) if InformationType>0 else MenuInformation[InformationType]()
    
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
                   -1:Mainmenu }
        LevelFlow.update(dict.fromkeys([1,2,3,4,5,6,7],self.MethodMenu))
    
        LevelName={-2:[],1:'City',2:'Borough',3:'Precinct',4:'Highway',5:'Tunnel',6:'Bridge',7:'Road'}
        
        if Level==-1:
            LevelFlow[Level]()
        else:
            Level, Method, name, nameFlag=LevelFlow[Level](LevelName[Level])
        #LevelFlow[Level]() if Level==-1 else Level, Method, name, nameFlag=LevelFlow[Level](LevelName[Level])
        
        
        return Level, Method, name, nameFlag
       
    def MethodMenu(self,Level,Method=[],name=[],nameFlag=0):
        
        print("There are methods for this level:")
        print ('%s' % '\n'.join(self.menu.List[Level][nameFlag]))
        
        Method = input('Please input the number before the method you want to use:')
        Method = InputCheck(self.menu.AvailableSet[Level][nameFlag], Method)
        
        Flow0={-2:self.MethodMenu,
                       -1:self.Level_selection,
                       0:self.SpecificInsight}
        Flow0.update(dict.fromkeys([1,2,3,4,5,6],self.MethodPresent))
        Flow1={-2:self.MethodMenu, #with name
                       -1:self.MethodMenu} #back to no name
        Flow1.update(dict.fromkeys([1,2,3,4,5,6],self.MethodPresent))
        methodFlow={0:Flow0,1:Flow1}
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
        if InputName==-1:
            Level, Method, name, nameFlag=self.MethodMenu(Level)
        else:
            Level, Method, name, nameFlag=self.MethodMenu(Level,[],InputName,1)
            
        #Level, Method, name, nameFlag=self.MethodMenu(Level) if InputName==-1 else Level, Method, name, nameFlag=self.MethodMenu(Level,[],InputName,1)
            
        return Level, Method, name, nameFlag
    def MethodPresent(self,Level,Method=[],name=[],nameFlag=0):
        self.menu.FunctionINIT_Situation(self.data)
        self.menu.FunctionList[Method](Level,name)
        Level, Method, name, nameFlag=self.MethodMenu(Level,[],name,nameFlag)
        return Level, Method, name, nameFlag
        
def CollisionContributingFactors_Vehicle(NYC):
    pass
def CollisionSimulation(NYC):
    pass

    
    
    
    
    
    
    
    



