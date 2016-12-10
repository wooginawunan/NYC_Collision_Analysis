'''
This module contain menu of methods and menu of level that could be used in interaction

Copyright:
@ Nan Wu 
@ nw1045@nyu.edu
@ wooginawunan@gmail.com
'''
from .MethodClass import SituationMethods, ContributingMethods
class MethodsMenu_Situation():
    '''
    Situation Analysis Methods Menu
    Attributes:
        City: Methods printing description string
        Borough_Whole: Methods printing description string
        Borough_S: Methods printing description string
        Precinct_Whole: Methods printing description string
        Precinct_S: Methods printing description string
        BTHS_Whole: Methods printing description string
        BTHS_S: Methods printing description string
        List: dictionary, keys(level), value(Methods printing description string)
        AvailableSet: dictionary, keys(level), value(Methods function numeric label)
        Indicator: 
            Type: dictionary
                Keys: int (a number that used in reading and passing the indicator)
                Value: string (the name of the relevant indicator)
        MethodFunction: SituationMethods object
        FunctionList: dictionary, keys(numeric label of function),values(functions)
        
    Methods:
        FunctionINIT_Situation
    '''
    def __init__(self):
        '''
        Constructor
        '''
        self.City=['1 Brief Summary','2 Plot by Time','3 InjuryKillPie']
        self.Borough_Whole=['0 Specific Insight','4 Map','6 Borough Compare']
        self.Borough_S=['1 Brief Summary','2 Plot by Time','3 InjuryKillPie','4 Map']
        self.Precinct_Whole=['0 Specific Insight','4 Map','5 Rank_TOP10']
        self.Precinct_S=['1 Brief Summary','2 Plot by Time','3 InjuryKillPie']
        self.BTHS_Whole=['0 Specific Insight','5 Rank_TOP10','1 Brief Summary','2 Plot by Time','3 InjuryKillPie']
        self.BTHS_S=['1 Brief Summary','2 Plot by Time','3 InjuryKillPie']
        self.List={'City':{0:self.City,1:self.City},
                   'Borough':{0:self.Borough_Whole,1:self.Borough_S},
                   'Precinct':{0:self.Precinct_Whole,1:self.Precinct_S}}
        
        self.List.update(dict.fromkeys(['Bridge','Highway','Tunnel','Road'],{0:self.BTHS_Whole,1:self.BTHS_S}))
        self.AvailableSet={'City':{0:[1,2,3]},
                           'Borough':{0:[0,4,6],1:[1,2,3,4]},
                           'Precinct':{0:[0,4,5],1:[1,2,3]}}
        
        self.AvailableSet.update(dict.fromkeys(['Bridge','Highway','Tunnel','Road'],{0:[0,1,2,3,5],1:[1,2,3]}))
        self.Indicator={1 : 'Number of Collisions', 2 : 'CollisionInjuredCount', 3 : 'CollisionKilledCount',4 : 'PersonsInjured',
                        5 : 'PersonsKilled', 6 : 'MotoristsInjured', 7 : 'MotoristsKilled', 8 : 'PassengInjured', 9 : 'PassengKilled',
                        10 : 'CyclistsInjured',11 : 'CyclistsKilled',12 : 'PedestrInjured', 13 : 'PedestrKilled',14 : 'Injury_or_Fatal'}
    def FunctionINIT_Situation(self,NYC,SavePath,TimeBegin,TimeEnd):
        '''
        Init method functions in this level
        Args:
            NYC: city object
            SavePath: data path
            TimeBegin: Loading data from. format:[YYYY,M] example:[2015,1]
            TimeEnd: Loading data end in. format:[YYYY,M] example:[2016,2]
        '''
        self.MethodFunction=SituationMethods(NYC,SavePath,TimeBegin,TimeEnd)
        self.FunctionList={1:self.MethodFunction.briefSummary,
                           2:self.MethodFunction.PlotbyMonth,
                           3:self.MethodFunction.InjuryKillPIE,
                           4:self.MethodFunction.Map,
                           5:self.MethodFunction.RankTop10,
                           6:self.MethodFunction.BoroughCompare}

class MethodMenu_Contributing():
    '''
    Contributing factors Analysis Methods Menu
    Attributes:
        Fundamental: Methods printing description string
        Whole: Methods printing description string
        BTHS: Methods printing description string
        List: dictionary, keys(level), value(Methods printing description string)
        AvailableSet: dictionary, keys(level), value(Methods function numeric label)
        Indicator: 
            Type: dictionary
                Keys: int (a number that used in reading and passing the indicator)
                Value: string (the name of the relevant indicator)
        MethodFunction: SituationMethods object
        FunctionList: dictionary, keys(numeric label of function),values(functions)
    Methods:
        FunctionINIT_Contributing
    '''
    def __init__(self):
        '''
        Constructor
        '''
        
        self.Fundamental=['1 Influence On Collision Severity']
        self.Whole=['0 Specific Insight']
        self.BHTR=['0 Specific Insight','1 Influence On Collision Severity']
        self.List={'City':{0:self.Fundamental,1:self.Fundamental},
                   'Borough':{0:self.Whole,1:self.Fundamental},
                   'Precinct':{0:self.Whole,1:self.Fundamental}}
        
        self.List.update(dict.fromkeys(['Bridge','Highway','Tunnel','Road'],{0:self.BHTR,1:self.Fundamental}))
        self.AvailableSet={'City':{0:[1]},
                           'Borough':{0:[0],1:[1]},
                           'Precinct':{0:[0],1:[1]}}
        
        self.AvailableSet.update(dict.fromkeys(['Bridge','Highway','Tunnel','Road'],{0:[0,1,2],1:[1,2]}))
        self.Influencer={1 : 'VehicleType',2 : 'ContributingFactor'}
        self.Indicator={1 : 'Number of Collisions', 2 : 'CollisionInjuredCount', 3 : 'CollisionKilledCount',4 : 'PersonsInjured',
                        5 : 'PersonsKilled', 6 : 'MotoristsInjured', 7 : 'MotoristsKilled', 8 : 'PassengInjured', 9 : 'PassengKilled',
                        10 : 'CyclistsInjured',11 : 'CyclistsKilled',12 : 'PedestrInjured', 13 : 'PedestrKilled',14 : 'Injury_or_Fatal'}
        
    def FunctionINIT_Contributing(self,NYC,SavePath,TimeBegin,TimeEnd):
        '''
        Init method functions in this level
        Args:
            NYC: city object
            SavePath: data path
            TimeBegin: Loading data from. format:[YYYY,M] example:[2015,1]
            TimeEnd: Loading data end in. format:[YYYY,M] example:[2016,2]
        '''
        self.MethodFunction=ContributingMethods(NYC,SavePath,TimeBegin,TimeEnd)
        self.FunctionList={1:self.MethodFunction.InfluenceONSeverity}       
        
        
        
        
        
        
        
        
        
        
        
        
        