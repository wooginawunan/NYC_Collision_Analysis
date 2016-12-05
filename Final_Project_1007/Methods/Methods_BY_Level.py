'''
Created on Dec 2, 2016

@author: apple
'''

from Methods.MethodClass import SituationMethods
from WN_User_Interact.InputANDError import NameCheck 

class MethodsMenu_Situation():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
        self.City=['1 Brief Summary','2 Plot by Time','3 InjuryKillPie']
        self.Borough_Whole=['0 Specific Insight','4 Map','6 Borough Compare']
        self.Borough_S=['1 Brief Summary','2 Plot by Time','3 InjuryKillPie']
        self.Precinct_Whole=['0 Specific Insight','4 Map','5 Rank_TOP10']
        self.Precinct_S=['1 Brief Summary','2 Plot by Time','3 InjuryKillPie']
        self.BTHS_Whole=['0 Specific Insight','5 Rank_TOP10','1 Brief Summary','2 Plot by Time','3 InjuryKillPie']
        self.BTHS_S=['1 Brief Summary','2 Plot by Time','3 InjuryKillPie']
        self.List={'City':{0:self.City,1:self.City},
                   'Borough':{0:self.Borough_Whole,1:self.Borough_S},
                   'Precinct':{0:self.Precinct_Whole,1:self.Precinct_S},
                   ('Bridge','Highway','Tunnel','Road'):{0:self.BTHS_Whole,1:self.BTHS_S}}
        self.AvailableSet={'City':{0:[1,2,3]},
                           'Borough':{0:[0,4,6],1:[1,2,3]},
                           'Precinct':{0:[0,4,5],1:[1,2,3]},
                           ('Bridge','Highway','Tunnel','Road'):{0:[0,1,2,3,5],1:[1,2,3]}}
    def FunctionINIT_Situation(self,NYC):
        self.MethodFunction=SituationMethods(NYC)
        self.FunctionList={1:self.MethodFunction.briefSummary,
                           2:self.MethodFunction.PlotbyMonth,
                           3:self.MethodFunction.InjuryKillPIE,
                           4:self.MethodFunction.Map,
                           5:self.MethodFunction.RankTop10,
                           6:self.MethodFunction.BoroughCompare}
    
    def Borough_Specific(self,NYC):
        print('You can choose from:')
        print(NYC.Borough_Dict.keys())
        print('\n'.join(sorted(list(NYC.Borough_Dict.keys()))))
        name = input('Please input the name:')
        name = NameCheck(name,NYC.Borough_Dict.keys())
        if name==-2: 
            return self.Borough_Specific(NYC)
        else:
            return name
    def Precinct_Specific(self,NYC):
        print('You can choose from:')
        print('\n'.join(sorted(list(NYC.Precinct_Dict.keys()))))
        name = input('Please input the name:')
        name = NameCheck(name,NYC.Precinct_Dict.keys())
        if name==-2: 
            return self.Precinct_Specific(NYC)
        else:
            return name
    def Bridge_Specific(self,NYC):
        print('You can choose from:')
        print('\n'.join(sorted(list(NYC.Bridge_Dict.keys()))))
        name = input('Please input the name:')
        name = NameCheck(name,NYC.Bridge_Dict.keys())
        if name==-2: 
            return self.Bridge_Specific(NYC)
        else:
            return name
    def Tunnel_Specific(self,NYC):
        print('You can choose from:')
        print('\n'.join(sorted(list(NYC.Tunnel_Dict.keys()))))
        name = input('Please input the name:')
        name = NameCheck(name,NYC.Tunnel_Dict.keys())
        if name==-2: 
            return self.Tunnel_Specific(NYC)
        else:
            return name
    def Highway_Specific(self,NYC):
        print('You can choose from:')
        print('\n'.join(sorted(list(NYC.Highway_Dict.keys()))))
        name = input('Please input the name:')
        name = NameCheck(name,NYC.Highway_Dict.keys())
        if name==-2: 
            return self.Highway_Specific(NYC)
        else:
            return name
    def Road_Specific(self,NYC):
        print('You can choose from:')
        print('\n'.join(sorted(list(NYC.Road_Dict.keys()))))
        name = input('Please input the name:')
        name = NameCheck(name,NYC.Road_Dict.keys())
        if name==-2: 
            return self.Road_Specific(NYC)
        else:
            return name
        
        
        
        
        
        
        
        
        
        
        