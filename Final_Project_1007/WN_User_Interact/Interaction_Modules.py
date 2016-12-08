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
from Methods.Methods_BY_Level import MethodsMenu_Situation,MethodMenu_Contributing
from CheckandError.DefinedError import DATEEndBeforeBegin,InvalidDate,ExitALLProgram
from CheckandError.Check import NameCheck,FirstCheck
from CheckandError.DefinedError import GoingBack,InvalidFirst
import os
import shutil
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
    print("You can set a period for data loading and structure building.")
    print('ALL following analysis will be based on this period.')
    print('Results will be save in a folder named by this period under results folder.')
    print('Example:201501_201601')
    
    while True:
        try:
            savepath=os.getcwd()
            savepath=''.join([savepath,'/results/'])
            print("Longest Time Interval is 201501-201612.")
            begintime=input('Please input the beginning date (Format: YYYYMM, Example: 201501):')
            if begintime=='Exit':
                raise ExitALLProgram
            endtime=input('Please input the ending date (Format: YYYYMM, Example: 201501):')
            if endtime=='Exit':
                raise ExitALLProgram
            TimeBegin,TimeEnd=DateCheck(begintime, endtime)
            path=savepath+begintime+'_'+endtime
            if not os.path.exists(path):
                os.makedirs(path)
            else:
                shutil.rmtree(path)
                os.makedirs(path)
            Mainmenu(TimeBegin,TimeEnd,path)
            return TimeBegin,TimeEnd, path
        except DATEEndBeforeBegin:
            print("Begining date should not later than ending date!")
        except InvalidDate:
            print("Invalid Input!")
    
def Mainmenu(TimeBegin,TimeEnd,SavePath):
    NYC = StructureBuilding(TimeBegin,TimeEnd)
    #print(NYC.Borough_Dict)
    print("There are three types of information: \n 1-CollisionSituation \n 2-CollisionContributingFactors_Vehicle \n 3-CollisionSimulation")
    InformationType = input("You can choose one by input the number before the type above:")
    MenuInformation={-2:Mainmenu, 
                     -1:SetTimeInterval,
                     1:CollisionSituation,
                     2:CollisionContributingFactors_Vehicle}
    inputset=MenuInformation.keys()
    InformationType = InputCheck(inputset, InformationType)
    if InformationType>0:
        MenuInformation[InformationType](NYC,SavePath,TimeBegin,TimeEnd)
    else:
        if InformationType==-1:
            MenuInformation[InformationType]()
        else:
            MenuInformation[InformationType](TimeBegin,TimeEnd,SavePath)
            
            
def CollisionContributingFactors_Vehicle(NYC,SavePath,TimeBegin,TimeEnd):
    Interaction=Contributing_Interaction(NYC,SavePath,TimeBegin,TimeEnd)
    Level,Method,name,nameFlag=Interaction.Level_selection()
    
def CollisionSituation(NYC,SavePath,TimeBegin,TimeEnd):
    Interaction=Situation_Interaction(NYC,SavePath,TimeBegin,TimeEnd)
    Level,Method,name,nameFlag=Interaction.Level_selection()

class Situation_Interaction():
    def __init__(self,NYC,SavePath,TimeBegin,TimeEnd):
        self.menu=MethodsMenu_Situation()
        self.data=NYC
        self.SavePath=SavePath
        self.TimeBegin=TimeBegin
        self.TimeEnd=TimeEnd
    def Level_selection(self,Level='null',Method='null',name='null',nameFlag=0):
        print("Available Perspectives: \n 1-City \n 2-Borough \n 3-Precinct \n 4-Highway \n 5-Tunnel \n 6-Bridge \n 7-Road")
        Level = input('Please input the number before the perspective you want to explore:')
        Level = InputCheck(range(1,8), Level)
        LevelFlow={-2:self.Level_selection,
                   -1:Mainmenu }
        LevelFlow.update(dict.fromkeys([1,2,3,4,5,6,7],self.MethodMenu))
    
        LevelName={-2:'null',1:'City',2:'Borough',3:'Precinct',4:'Highway',5:'Tunnel',6:'Bridge',7:'Road'}
        
        if Level==-1:
            LevelFlow[Level]()
        else:
            Level, Method, name, nameFlag=LevelFlow[Level](LevelName[Level])
        #LevelFlow[Level]() if Level==-1 else Level, Method, name, nameFlag=LevelFlow[Level](LevelName[Level])
        
        
        return Level, Method, name, nameFlag
       
    def MethodMenu(self,Level,Method='null',name='null',nameFlag=0):
        
        print("There are methods for this level:")
        print ('%s' % '\n'.join(self.menu.List[Level][nameFlag]))
        
        Method = input('Please input the number before the method you want to use:')
        Method = InputCheck(self.menu.AvailableSet[Level][nameFlag], Method)
        
        Flow0={-2:self.MethodMenu,
                       -1:self.Level_selection,
                       0:self.SpecificInsight}
        Flow0.update(dict.fromkeys([1,2,3,4,5,6],self.MethodPresent))
        Flow1={-2:self.MethodMenu, #with name
                       -1:self.SpecificInsight} #back to no name
        Flow1.update(dict.fromkeys([1,2,3,4,5,6],self.MethodPresent))
        methodFlow={0:Flow0,1:Flow1}
    
        Level, Method, name, nameFlag = methodFlow[nameFlag][Method](Level, Method, name, nameFlag)
        
        return Level, Method, name, nameFlag
    def SpecificInsight(self,Level,Method='null',name='null',nameFlag=0):
        SpecificMenu={'Borough':Borough_Specific,
                      'Precinct':Precinct_Specific,
                      'Highway':Highway_Specific,
                      'Bridge':Bridge_Specific,
                      'Tunnel':Tunnel_Specific,
                      'Road':Road_Specific}
        
        InputName=SpecificMenu[Level](self.data)
        if InputName==-1:
            Level, Method, name, nameFlag=self.MethodMenu(Level)
        else:
            Level, Method, name, nameFlag=self.MethodMenu(Level,'null',InputName,1)
            
        #Level, Method, name, nameFlag=self.MethodMenu(Level) if InputName==-1 else Level, Method, name, nameFlag=self.MethodMenu(Level,[],InputName,1)
            
        return Level, Method, name, nameFlag
    def ChooseIndicator(self):
        print('Please Choose one Indicator from:')
        for key in self.menu.Indicator.keys():
            print(':'.join([str(key),self.menu.Indicator[key]]))
        while True:
            try:
                Indicator = input("Your choice: ") 
                Indicator = FirstCheck(list(map(lambda x:str(x), self.menu.Indicator.keys())),Indicator)
                return Indicator
            except InvalidFirst:
                pass
    
    def MethodPresent(self,Level,Method='null',name='null',nameFlag=0):
        self.menu.FunctionINIT_Situation(self.data,self.SavePath,self.TimeBegin,self.TimeEnd)
        if Method!=3:
            try:
                Indicator=self.ChooseIndicator()
                self.menu.FunctionList[Method](Indicator,Level,name)
                return self.MethodPresent(Level, Method, name, nameFlag)
            except GoingBack:
                Level, Method, name, nameFlag=self.MethodMenu(Level,'null',name,nameFlag)
                return Level, Method, name, nameFlag
        else:
            self.menu.FunctionList[Method](Level,name)
            Level, Method, name, nameFlag=self.MethodMenu(Level,'null',name,nameFlag)
            return Level, Method, name, nameFlag
            
        

        
        
        
class Contributing_Interaction(Situation_Interaction):
    def __init__(self,NYC,SavePath,TimeBegin,TimeEnd):
        self.menu=MethodMenu_Contributing()
        self.data=NYC
        self.SavePath=SavePath
        self.TimeBegin=TimeBegin
        self.TimeEnd=TimeEnd
    def MethodPresent(self,Level,Method='null',name='null',nameFlag=0):
        self.menu.FunctionINIT_Contributing(self.data,self.SavePath,self.TimeBegin,self.TimeEnd)
        Func_Menu={1: self.Influencing, 2: self.Relation}
        Level, Method, name, nameFlag=Func_Menu[Method](Level,Method,name,nameFlag)
        Level, Method, name, nameFlag=self.MethodMenu(Level,'null',name,nameFlag)
        return Level, Method, name, nameFlag
    
    
    def ChooseInfluencing(self):
        print('Please Choose one Influencer from:')
        for key in self.menu.Influencer.keys():
            print(':'.join([str(key),self.menu.Influencer[key]]))
        while True:
            try:
                Influencer = input("Your choice: ") 
                Influencer = FirstCheck(list(map(lambda x:str(x), self.menu.Influencer.keys())),Influencer)
                return Influencer
            except InvalidFirst:
                pass
        return Influencer
    
    def ChooseIndicator(self):
        print('Please Choose one Indicator from:')
        for key in self.menu.Indicator.keys():
            print(':'.join([str(key),self.menu.Indicator[key]]))
        while True:
            try:
                Indicator = input("Your choice: ") 
                Indicator = FirstCheck(list(map(lambda x:str(x), self.menu.Indicator.keys())),Indicator)
                return Indicator
            except InvalidFirst:
                pass
            
        
    def Influencing(self,Level,Method='null',name='null',nameFlag=0):
        try:
            Influencer = self.ChooseInfluencing()
            try:
                Indicator=self.ChooseIndicator()
                self.menu.FunctionList[Method](Influencer,Indicator,Level,name)
                return self.Influencing(Level, Method, name, nameFlag)
            except GoingBack:
                return self.Influencing(Level, Method, name, nameFlag)
                
        except GoingBack:
            return self.MethodMenu(Level,Method,name,nameFlag)
        
    def Relation(self,Level,Method='null',name='null',nameFlag=0):
        try:
            Influencer0 = self.ChooseInfluencing()
            try:
                Influencer1=self.ChooseInfluencing()
                self.menu.FunctionList[Method](Influencer0,Influencer1,Level,name)
                return self.Relation(Level, Method, name, nameFlag)
            except GoingBack:
                return self.Relation(Level, Method, name, nameFlag)
        except GoingBack:
            return self.MethodMenu(Level,Method,name,nameFlag)
    

def Borough_Specific(NYC):
    print('You can choose from:')
    Bo_Catalog=NYC.boroughCatalog()
    print('\n'.join(Bo_Catalog))
    name = input('Please input the short name(two letters) before the name:')
    name = NameCheck(NYC.Borough_Dict.keys(),name)
    if name==-2: 
        return Borough_Specific(NYC)
    else:
        return name
def Precinct_Specific(NYC):
    print("Precinct are grouped by Borough.")
    print("Please specific the Borough First.")
    while True:
        try:
            print('You can choose a bourough from:')
            Bo_Catalog=NYC.boroughCatalog()
            print('\n'.join(Bo_Catalog))
            Bname = input('Please input the short name(two letters) before the name:')
            Bname = FirstCheck(NYC.Borough_Dict.keys(),Bname)
            print(NYC.Borough_Dict[Bname].name+' : ')
            precinctCata=NYC.Borough_Dict[Bname].precinctCatalog()
            print('  \n'.join(precinctCata))
            while True:
                try:
                    name = input('Please input a precinct ID :')
                    name = FirstCheck(NYC.Borough_Dict[Bname].precinctList.keys(),name)
                    return name
                except GoingBack:
                    break
                except InvalidFirst:
                    pass
        except GoingBack:
            return -1
        except InvalidFirst:
            pass
        
def Bridge_Specific(NYC):
    print('You can choose from:')
    print('\n'.join(NYC.bridgeCatalog()))
    name = input('Please input the name:')
    name = NameCheck(NYC.Bridge_Dict.keys(),name)
    if name==-2: 
        return Bridge_Specific(NYC)
    else:
        return name
def Tunnel_Specific(NYC):
    print('You can choose from:')
    print('\n'.join(NYC.tunnelCatalog()))
    name = input('Please input the name:')
    name = NameCheck(NYC.Tunnel_Dict.keys(),name)
    if name==-2: 
        return Tunnel_Specific(NYC)
    else:
        return name
def Highway_Specific(NYC):
    print('You can choose from:')
    print('\n'.join(NYC.highwayCatalog()))
    name = input('Please input the name:')
    name = NameCheck(NYC.Highway_Dict.keys(),name)
    if name==-2: 
        return Highway_Specific(NYC)
    else:
        return name
def Road_Specific(NYC):
    print('Please specify the first character of the road you want to explore.')
    print('You can choose from ABCDEFGHIGKLMNOPQRSTUVWXYZ or - for others')
    
    while True:
        try:
            
            FirstC=input('Input a CAPITAL letter or - : ')
            FirstC=FirstCheck('ABCDEFGHIGKLMNOPQRSTUVWXYZ-',FirstC)
            if FirstC=='-':
                FirstC='*Other'
            roadCata=NYC.roadCatalog()
            print('You can choose from:')
            print('\n'.join(roadCata[FirstC]))
            while True:
                try:
                    name = input('Please input the name:')
                    name = FirstCheck(NYC.Road_Dict.keys(),name)
                    return name
                except GoingBack:
                    break
                except InvalidFirst:
                    pass

        except GoingBack:
            return -1
        except InvalidFirst:
            pass   

    
    
    
    
    



