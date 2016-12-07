'''
Created on Dec 2, 2016

@author: apple
'''
from .MethodClass import SituationMethods, ContributingMethods
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
        self.MethodFunction=SituationMethods(NYC,SavePath,TimeBegin,TimeEnd)
        self.FunctionList={1:self.MethodFunction.briefSummary,
                           2:self.MethodFunction.PlotbyMonth,
                           3:self.MethodFunction.InjuryKillPIE,
                           4:self.MethodFunction.Map,
                           5:self.MethodFunction.RankTop10,
                           6:self.MethodFunction.BoroughCompare}


class MethodMenu_Contributing():
    def __init__(self):
        '''
        Constructor
        '''
        
        self.Fundamental=['1 Influence On Collision Severity','2 Relation Between Factors']
        self.Whole=['0 Specific Insight']
        self.BHTR=['0 Specific Insight','1 Influence On Collision Severity','2 Relation Between Factors']
        self.List={'City':{0:self.Fundamental,1:self.Fundamental},
                   'Borough':{0:self.Whole,1:self.Fundamental},
                   'Precinct':{0:self.Whole,1:self.Fundamental}}
        
        self.List.update(dict.fromkeys(['Bridge','Highway','Tunnel','Road'],{0:self.BHTR,1:self.Fundamental}))
        self.AvailableSet={'City':{0:[1,2]},
                           'Borough':{0:[0],1:[1,2]},
                           'Precinct':{0:[0],1:[1,2]}}
        
        self.AvailableSet.update(dict.fromkeys(['Bridge','Highway','Tunnel','Road'],{0:[0,1,2],1:[1,2]}))
        self.Influencer={1 : 'VehicleType',2 : 'ContributingFactor' ,3 : 'CollisionVehicleCount'}
        self.Indicator={1 : 'Number of Collisions', 2 : 'CollisionInjuredCount', 3 : 'CollisionKilledCount',4 : 'PersonsInjured',
                        5 : 'PersonsKilled', 6 : 'MotoristsInjured', 7 : 'MotoristsKilled', 8 : 'PassengInjured', 9 : 'PassengKilled',
                        10 : 'CyclistsInjured',11 : 'CyclistsKilled',12 : 'PedestrInjured', 13 : 'PedestrKilled',14 : 'Injury_or_Fatal'}
        
    def FunctionINIT_Contributing(self,NYC,SavePath,TimeBegin,TimeEnd):
        self.MethodFunction=ContributingMethods(NYC,SavePath,TimeBegin,TimeEnd)
        self.FunctionList={1:self.MethodFunction.InfluenceONSeverity,
                           2:self.MethodFunction.RelationshipBetweenInfluencer}       
        
        
        
        
        
        
        
        
        
        
        
        
        