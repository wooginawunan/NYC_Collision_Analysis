'''
Created on Dec 2, 2016

@author: apple
'''
import datetime
import pandas as pd
class FundamentalMethods():
    '''
    classdocs
    '''
    def __init__(self, city, savepath, TimeBegin,TimeEnd):
        '''
        Constructor
        '''
        self.data=city
        self.savepath=savepath # .../results/201501_201502
        self.Influencer={1 : 'VehicleType',2 : 'ContributingFactor' ,3 : 'CollisionVehicleCount'}
        self.Indicator={1 : 'Number of Collisions', 2 : 'CollisionInjuredCount', 3 : 'CollisionKilledCount',4 : 'PersonsInjured',
                        5 : 'PersonsKilled', 6 : 'MotoristsInjured', 7 : 'MotoristsKilled', 8 : 'PassengInjured', 9 : 'PassengKilled',
                        10 : 'CyclistsInjured',11 : 'CyclistsKilled',12 : 'PedestrInjured', 13 : 'PedestrKilled',14 : 'Injury_or_Fatal'}
        self.TimeBegin=TimeBegin
        self.TimeEnd=TimeEnd # [2015,1]
        start=datetime.date(self.TimeBegin[0],self.TimeBegin[1],20)
        end=datetime.date(self.TimeEnd[0],self.TimeEnd[1],20)
        ALLDATE=pd.date_range(start,end,freq='30D')
        self.TimeList=list(map(lambda date:str(date.year)+str(date.month).zfill(2), ALLDATE))
class SituationMethods(FundamentalMethods):
    def CityTable(self,Indicator):
        table_0=dict.fromkeys(self.TimeList,0)
        for time in table_0.keys():
            y=time[0:4]
            m=time[4:6]
            for borough in self.Borough_Dict.values():
                for precinct in borough.precinctList.values():
                    df1=precinct.Collisions_intersection[y][m]
                    df2=precinct.Collisions_HighTunBri[y][m]
                    if Indicator==1:
                        table_0[time]=table_0[time]+len(df1['CollisionKey'].unique())+len(df2['CollisionKey'].unique())
                    else:
                        table_0[time]=table_0[time]+df1[self.Indicator[Indicator]].sum()+df2[self.Indicator[Indicator]].sum()
        table=pd.DataFrame(table_0)
                            
    def BoroughTable(self,Indicator,name=[]):
        table_0=dict.fromkeys(self.TimeList,0)
        for time in table_0.keys():
            y=time[0:4]
            m=time[4:6]
            if name==[]:
                
                
        
        
        
        
    def PrecinctTable(self,Indicator,name=[]):
        pass
    def RoadTable(self,Indicator,name=[]):
        pass
    def HighwayTable(self,Indicator,name=[]):
        pass
    def BridgeTable(self,Indicator,name=[]):
        pass
    def TunnelTable(self,Indicator,name=[]):
        pass
    
    def SummaryTableCreating(self,Indicator,level,name=[]):
        pass
       # return Table
    def briefSummary(self,Indicator,level,name=[]):
        pass
        #TotalAccidennt()
        #TotalInjury()
        #TotalKilled()
    def PlotbyMonth(self,Indicator,level,name=[]):
        pass
    def InjuryKillPIE(self,level,name=[]):
        pass
    def Map(self,Indicator,level,name=[]):
        pass
    def BoroughCompare(self,Indicator,level,name=[]):
        pass
    def RankTop10(self,Indicator,level,name=[]):
        pass



class ContributingMethods(FundamentalMethods):
    def InfluenceONSeverity(self,Influencer,SeverityMeasure,level,name=[]):
        pass
    def RelationshipBetweenInfluencer(self, Influencer0, Influencer1,level,name=[]):
        pass     