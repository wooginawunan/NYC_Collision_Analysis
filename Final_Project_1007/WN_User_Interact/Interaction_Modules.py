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


#from .CollisionSituation import CollisionSituation
from WN_struct_building import StructureBuilding
from Methods.Methods_Menu import MethodsMenu_Situation,MethodMenu_Contributing
from CheckandError.DefinedError import *
from CheckandError.Check import *

import os
import shutil

def ProgramIntroduction():
    '''
    An brief introduction of the whole project.
    
    '''
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
    print("Back with: Back")
    print("Now you can begin with it.")
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
   
def BeginDate():
    while True:
        try:
            begintime=input('Please input the beginning date (Format: YYYYMM, Example: 201501):')
            GeneralCheck(begintime)
            OneDateCheck(begintime) 
            return begintime
        except InvalidDate:
            print("Invalid Date Input.")
            
def EndDate():
    while True:
        try:
            begintime=input('Please input the ending date (Format: YYYYMM, Example: 201501):')
            GeneralCheck(begintime)
            OneDateCheck(begintime) 
            return begintime
        except InvalidDate:
            print("Invalid Date Input.")
            
def loadTimeInterval():
    while True:
        print("Longest Time Interval is 201501-201612.")
        begintime = BeginDate()
        endtime = EndDate() 
        try:
            TimeBegin,TimeEnd = TwoDateCheck(begintime, endtime)
            return TimeBegin,TimeEnd,begintime,endtime
        except DATEEndBeforeBegin:
            print("Beginning date should not later than ending date!")
            
def CreateFolder(path):
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        shutil.rmtree(path)
        os.makedirs(path)

def CreateSaveFolder(begintime,endtime,savepath):
    savepath=''.join([savepath,'/results/'])
    path=savepath+begintime+'_'+endtime
    CreateFolder(path)
    return path

def SetTimeInterval(dirname):
    print("You can set a period for data loading and structure building.")
    print('ALL following analysis will be based on this period.')
    print('Results will be save in a folder named by this period under results folder.')
    print('Example:201501_201601')
    
    TimeBegin,TimeEnd,begintime,endtime = loadTimeInterval()
    path=CreateSaveFolder(begintime,endtime,dirname)  
    NYC = StructureBuilding(TimeBegin,TimeEnd,dirname)    
    Mainmenu(TimeBegin,TimeEnd,path,NYC)
    
    return TimeBegin,TimeEnd, path


def Load_INTinput(Instruction,Availbelset):
    while True:
        try:
            InformationType = input(Instruction)
            GeneralCheck(InformationType)
            InformationType = IntInputCheck(Availbelset, InformationType)
            return InformationType
        except InvalidInput:
            print("Invalid Input!")

def Load_Stringinput_First(Instruction,Availbelset):
    while True:
        try:
            name = input(Instruction)
            GeneralCheck(name)
            name = StringInputCheck(Availbelset, name)
            return name
        except GoingBack:
            return -1
        except InvalidInput:
            pass

def Borough_Specific(NYC):
    print('You can choose from:')
    Bo_Catalog=NYC.boroughCatalog()
    print('\n'.join(Bo_Catalog))
    return Load_Stringinput_First('Please input the short name(two letters) before the name:',NYC.Borough_Dict.keys())

def PrecinctbyBoroughPrint(NYC):
    print('You can choose a borough from:')
    Bo_Catalog=NYC.boroughCatalog()
    print('\n'.join(Bo_Catalog))
    Bname = input('Please input the short name(two letters) before the name:')
    GeneralCheck(Bname)
    Bname = StringInputCheck(NYC.Borough_Dict.keys(),Bname)
    print(NYC.Borough_Dict[Bname].name+' : ')
    precinctCata=NYC.Borough_Dict[Bname].precinctCatalog()
    print('  \n'.join(precinctCata))
    return Bname

def Precinct_Specific(NYC):
    print("Precinct are grouped by Borough.")
    print("Please specific the Borough First.")
    while True:
        try:
            Bname = PrecinctbyBoroughPrint(NYC)
            while True:
                try:
                    name = input('Please input a precinct ID :')
                    GeneralCheck(name)
                    name = StringInputCheck(NYC.Borough_Dict[Bname].precinctList.keys(),name)
                    return name
                except GoingBack:
                    break
                except InvalidInput:
                    pass
        except GoingBack:
            return -1
        except InvalidInput:
            pass

def RoadNameDictPrint(NYC):
    FirstC=input('Input a CAPITAL letter or - : ')
    GeneralCheck(FirstC)
    FirstC=StringInputCheck('ABCDEFGHIGKLMNOPQRSTUVWXYZ-',FirstC)
    if FirstC=='-':
        FirstC='*Other'
    roadCata=NYC.roadCatalog()
    print('You can choose from:')
    print('\n'.join(roadCata[FirstC]))

def Road_Specific(NYC):
    print('Please specify the first character of the road you want to explore.')
    print('You can choose from ABCDEFGHIGKLMNOPQRSTUVWXYZ or - for others')
    
    while True:
        try:
            RoadNameDictPrint(NYC)
            while True:
                try:
                    name = input('Please input the name:')
                    GeneralCheck(name)
                    name = StringInputCheck(NYC.Road_Dict.keys(),name)
                    return name
                except GoingBack:
                    break
                except InvalidInput:
                    pass

        except GoingBack:
            return -1
        except InvalidInput:
            pass   
        
def Bridge_Specific(NYC):
    print('You can choose from:')
    print('\n'.join(NYC.bridgeCatalog()))
    return Load_Stringinput_First('Please input the name:',NYC.Bridge_Dict.keys())
    
        
def Tunnel_Specific(NYC):
    print('You can choose from:')
    print('\n'.join(NYC.tunnelCatalog()))
    return Load_Stringinput_First('Please input the name:',NYC.Tunnel_Dict.keys())

def Highway_Specific(NYC):
    print('You can choose from:')
    print('\n'.join(NYC.highwayCatalog()))
    return Load_Stringinput_First('Please input the name:',NYC.Highway_Dict.keys())


def Mainmenu(TimeBegin,TimeEnd,SavePath,NYC):
    MenuInformation={-1:SetTimeInterval,
                     1:CollisionSituation,
                     2:CollisionContributingFactors_Vehicle}
    print("There are three types of information: \n 1-CollisionSituation \n 2-CollisionContributingFactors_Vehicle ")
    InformationType = Load_INTinput("You can choose one by input the number before the type above:", MenuInformation.keys())
    
    if InformationType>0:
        MenuInformation[InformationType](NYC,SavePath,TimeBegin,TimeEnd)
    else:
        MenuInformation[InformationType](SavePath[:-22])
                        
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
        Level = Load_INTinput('Please input the number before the perspective you want to explore:',range(1,8))
        
        LevelName={1:'City',2:'Borough',3:'Precinct',4:'Highway',5:'Tunnel',6:'Bridge',7:'Road'}
        
        if Level==-1:
            Mainmenu(self.TimeBegin,self.TimeEnd,self.SavePath,self.data)
        else:
            Level, Method, name, nameFlag=self.MethodMenu(LevelName[Level])
        
        return Level, Method, name, nameFlag
                  
    def MethodMenu(self,Level,Method='null',name='null',nameFlag=0):
        
        print("There are methods for this level:")
        print ('%s' % '\n'.join(self.menu.List[Level][nameFlag]))
        Method = Load_INTinput('Please input the number before the method you want to use:',self.menu.AvailableSet[Level][nameFlag])
        
        
        Flow0={-1:self.Level_selection,
                0:self.SpecificInsight}
        Flow0.update(dict.fromkeys([1,2,3,4,5,6],self.MethodPresent))
        Flow1={ -1:self.SpecificInsight} #back to no name
        Flow1.update(dict.fromkeys([1,2,3,4,5,6],self.MethodPresent))
        methodFlow={0:Flow0,1:Flow1}
    
        return methodFlow[nameFlag][Method](Level, Method, name, nameFlag)

    def SpecificInsight(self,Level,Method='null',name='null',nameFlag=0):
        SpecificMenu={'Borough':Borough_Specific,
                      'Precinct':Precinct_Specific,
                      'Highway':Highway_Specific,
                      'Bridge':Bridge_Specific,
                      'Tunnel':Tunnel_Specific,
                      'Road':Road_Specific}
        
        InputName=SpecificMenu[Level](self.data)
        if InputName==-1:
            return self.MethodMenu(Level)
        else:
            return self.MethodMenu(Level,'null',InputName,1)
            
    def ChooseIndicator(self):
        print('Please Choose one Indicator from:')
        for key in self.menu.Indicator.keys():
            print(':'.join([str(key),self.menu.Indicator[key]]))
        
        while True:
            try:
                Indicator = input("Your choice: ") 
                GeneralCheck(Indicator)
                Indicator = StringInputCheck(list(map(lambda x:str(x), self.menu.Indicator.keys())),Indicator)
                return int(Indicator)
            except InvalidInput:
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
        Func_Menu={1: self.Influencing}
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
                GeneralCheck(Influencer)
                Influencer = StringInputCheck(list(map(lambda x:str(x), self.menu.Influencer.keys())),Influencer)
                return int(Influencer)
            except InvalidInput:
                pass
        return Influencer
    
    def ChooseIndicator(self):
        print('Please Choose one Indicator from:')
        for key in self.menu.Indicator.keys():
            print(':'.join([str(key),self.menu.Indicator[key]]))
        while True:
            try:
                Indicator = input("Your choice: ") 
                GeneralCheck(Indicator)
                Indicator = StringInputCheck(list(map(lambda x:str(x), self.menu.Indicator.keys())),Indicator)
                return int(Indicator)
            except InvalidInput:
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
        
            
    



    
    
    
    



