'''
Created on Dec 2, 2016

@author: apple
'''

from Methods.MethodClass import SituationMethods
from CheckandError.Check import NameCheck,FirstCheck
from CheckandError.DefinedError import GoingBack,InvalidFirst
from astropy.wcs.docstrings import name

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
                   'Precinct':{0:self.Precinct_Whole,1:self.Precinct_S}}
        
        self.List.update(dict.fromkeys(['Bridge','Highway','Tunnel','Road'],{0:self.BTHS_Whole,1:self.BTHS_S}))
        self.AvailableSet={'City':{0:[1,2,3]},
                           'Borough':{0:[0,4,6],1:[1,2,3]},
                           'Precinct':{0:[0,4,5],1:[1,2,3]}}
        
        self.AvailableSet.update(dict.fromkeys(['Bridge','Highway','Tunnel','Road'],{0:[0,1,2,3,5],1:[1,2,3]}))
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
        Road_Catalog=NYC.boroughCatalog()
        print('\n'.join(Road_Catalog))
        name = input('Please input the short name(two letters) before the name:')
        name = NameCheck(NYC.Borough_Dict.keys(),name)
        if name==-2: 
            return self.Borough_Specific(NYC)
        else:
            return name
    def Precinct_Specific(self,NYC):
        print('You can choose from:')
        for key in NYC.Borough_Dict.keys():
            print(NYC.Borough_Dict[key].name+' : ')
            precinctCata=NYC.Borough_Dict[key].precinctCatalog()
            print('  \n'.join(precinctCata))
        name = input('Please input the name:')
        name = NameCheck(NYC.Precinct_Dict.keys(),name)
        if name==-2: 
            return self.Precinct_Specific(NYC)
        else:
            return name
    def Bridge_Specific(self,NYC):
        print('You can choose from:')
        print('\n'.join(NYC.bridgeCatalog()))
        name = input('Please input the name:')
        name = NameCheck(NYC.Bridge_Dict.keys(),name)
        if name==-2: 
            return self.Bridge_Specific(NYC)
        else:
            return name
    def Tunnel_Specific(self,NYC):
        print('You can choose from:')
        print('\n'.join(NYC.tunnelCatalog()))
        name = input('Please input the name:')
        name = NameCheck(NYC.Tunnel_Dict.keys(),name)
        if name==-2: 
            return self.Tunnel_Specific(NYC)
        else:
            return name
    def Highway_Specific(self,NYC):
        print('You can choose from:')
        print('\n'.join(NYC.highwayCatalog()))
        name = input('Please input the name:')
        name = NameCheck(NYC.Highway_Dict.keys(),name)
        if name==-2: 
            return self.Highway_Specific(NYC)
        else:
            return name
    def Road_Specific(self,NYC):
        print('Please specify the first character of the road you want to explore.')
        print('You can choose from ABCDEFGHIGKLMNOPQRSTUVWXYZ or *Other')
        
        while True:
            try:
                
                FirstC=input('Input a CAPITAL letter or *: ')
                FirstC=NameCheck('ABCDEFGHIGKLMNOPQRSTUVWXYZ*',FirstC)
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
                        print('Invalid Input!')

            except GoingBack:
                return -1
            except InvalidFirst:
                print('Invalid Input!')
        
        
        
        
        
        
        
        
        
        
        
        
        
        