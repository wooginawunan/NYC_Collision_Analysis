'''
Created on Dec 2, 2016

@author: apple
'''
import datetime
import pandas as pd
from WN_struct_building.CityStructure import borough
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
    def TableDICT_Init(self):
        self.Table_Dict={'City':self.CityTable,'Borough': self.BoroughTable,'Precinct':self.PrecinctTable,'Highway':self.HighwayTable,'Tunnel':self.TunnelTable,'Bridge':self.BridgeTable,'Road':self.RoadTable}
    def CityTable(self,Indicator,name=[]):
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
                        
        table=pd.DataFrame(pd.Series(table_0),columns=['NYC'])
        return table
                            
    def BoroughTable(self,Indicator,name=[]):
        table_0=dict.fromkeys(self.TimeList,0)
        if name==[]:
            for time in table_0.keys():
                y=time[0:4]
                m=time[4:6]
                bo_table=dict()
                for borough in self.Borough_Dict.values():
                    amount=0
                    for precinct in borough.precinctList.values():
                        df1=precinct.Collisions_intersection[y][m]
                        df2=precinct.Collisions_HighTunBri[y][m]
                        if Indicator==1:
                            amount=amount+len(df1['CollisionKey'].unique())+len(df2['CollisionKey'].unique())
                        else:
                            amount=amount+df1[self.Indicator[Indicator]].sum()+df2[self.Indicator[Indicator]].sum()
                    bo_table[borough.name]=amount
                table_0[time]=bo_table
            table=pd.DataFrame(table_0).transpose()
            return table
        else:
            borough=self.Borough_Dict[name]
            for time in table_0.keys():
                y=time[0:4]
                m=time[4:6]
                for precinct in borough.precinctList.values():
                    df1=precinct.Collisions_intersection[y][m]
                    df2=precinct.Collisions_HighTunBri[y][m]
                    if Indicator==1:
                        table_0[time]=table_0[time]+len(df1['CollisionKey'].unique())+len(df2['CollisionKey'].unique())
                    else:
                        table_0[time]=table_0[time]+df1[self.Indicator[Indicator]].sum()+df2[self.Indicator[Indicator]].sum()
            table=pd.DataFrame(pd.Series(table_0),columns=[borough.name])
            return table
        
                            
    def PrecinctTable(self,Indicator,name=[]):
        table_0=dict.fromkeys(self.TimeList,0)
        if name==[]:
            for time in table_0.keys():
                y=time[0:4]
                m=time[4:6]
                bo_table=dict()
                for borough in self.Borough_Dict.values():
                    for precinct in borough.precinctList.values():
                        amount=0
                        df1=precinct.Collisions_intersection[y][m]
                        df2=precinct.Collisions_HighTunBri[y][m]
                        if Indicator==1:
                            amount=amount+len(df1['CollisionKey'].unique())+len(df2['CollisionKey'].unique())
                        else:
                            amount=amount+df1[self.Indicator[Indicator]].sum()+df2[self.Indicator[Indicator]].sum()
                        bo_table[precinct.ID]=amount
                table_0[time]=bo_table
            table=pd.DataFrame(table_0).transpose()
            return table
        else:
            for time in table_0.keys():
                y=time[0:4]
                m=time[4:6]
                for borough in self.Borough_Dict.values():
                    if name in borough.precinctList.keys():
                        df1=precinct.Collisions_intersection[y][m]
                        df2=precinct.Collisions_HighTunBri[y][m]
                        if Indicator==1:
                            table_0[time]=table_0[time]+len(df1['CollisionKey'].unique())+len(df2['CollisionKey'].unique())
                        else:
                            table_0[time]=table_0[time]+df1[self.Indicator[Indicator]].sum()+df2[self.Indicator[Indicator]].sum()
            table=pd.DataFrame(pd.Series(table_0),columns=name)
            return table
    def RoadTable(self,Indicator,name=[]):
        table_0=dict.fromkeys(self.TimeList,0)
        if name==[]:
            for time in table_0.keys():
                y=time[0:4]
                m=time[4:6]
                bo_table=dict()
                for road in self.Road_Dict.values():
                    amount=0
                    df=road.Collisions[y][m]
                    if Indicator==1:
                        amount=amount+len(df['CollisionKey'].unique())
                    else:
                        amount=amount+df[self.Indicator[Indicator]].sum()
                    bo_table[road.name]=amount
                table_0[time]=bo_table
            table=pd.DataFrame(table_0).transpose()
            return table
        else:
            road=self.Road_Dict[name]
            for time in table_0.keys():
                y=time[0:4]
                m=time[4:6]
                df=road.Collisions[y][m]
                if Indicator==1:
                    table_0[time]=table_0[time]+len(df['CollisionKey'].unique())
                else:
                    table_0[time]=table_0[time]+df[self.Indicator[Indicator]].sum()
            table=pd.DataFrame(pd.Series(table_0),columns=[name])
            return table
    def HighwayTable(self,Indicator,name=[]):
        table_0=dict.fromkeys(self.TimeList,0)
        if name==[]:
            for time in table_0.keys():
                y=time[0:4]
                m=time[4:6]
                bo_table=dict()
                for highway in self.Highway_Dict.values():
                    amount=0
                    df=highway.Collisions[y][m]
                    if Indicator==1:
                        amount=amount+len(df['CollisionKey'].unique())
                    else:
                        amount=amount+df[self.Indicator[Indicator]].sum()
                    bo_table[highway.name]=amount
                table_0[time]=bo_table
            table=pd.DataFrame(table_0).transpose()
            return table
        else:
            highway=self.Highway_Dict[name]
            for time in table_0.keys():
                y=time[0:4]
                m=time[4:6]
                df=highway.Collisions[y][m]
                if Indicator==1:
                    table_0[time]=table_0[time]+len(df['CollisionKey'].unique())
                else:
                    table_0[time]=table_0[time]+df[self.Indicator[Indicator]].sum()
            table=pd.DataFrame(pd.Series(table_0),columns=[name])
            return table
    def BridgeTable(self,Indicator,name=[]):
        table_0=dict.fromkeys(self.TimeList,0)
        if name==[]:
            for time in table_0.keys():
                y=time[0:4]
                m=time[4:6]
                bo_table=dict()
                for bridge in self.Bridge_Dict.values():
                    amount=0
                    df=bridge.Collisions[y][m]
                    if Indicator==1:
                        amount=amount+len(df['CollisionKey'].unique())
                    else:
                        amount=amount+df[self.Indicator[Indicator]].sum()
                    bo_table[bridge.name]=amount
                table_0[time]=bo_table
            table=pd.DataFrame(table_0).transpose()
            return table
        else:
            bridge=self.Bridge_Dict[name]
            for time in table_0.keys():
                y=time[0:4]
                m=time[4:6]
                df=bridge.Collisions[y][m]
                if Indicator==1:
                    table_0[time]=table_0[time]+len(df['CollisionKey'].unique())
                else:
                    table_0[time]=table_0[time]+df[self.Indicator[Indicator]].sum()
            table=pd.DataFrame(pd.Series(table_0),columns=[name])
            return table
    def TunnelTable(self,Indicator,name=[]):
        table_0=dict.fromkeys(self.TimeList,0)
        if name==[]:
            for time in table_0.keys():
                y=time[0:4]
                m=time[4:6]
                bo_table=dict()
                for tunnel in self.Tunnel_Dict.values():
                    amount=0
                    df=tunnel.Collisions[y][m]
                    if Indicator==1:
                        amount=amount+len(df['CollisionKey'].unique())
                    else:
                        amount=amount+df[self.Indicator[Indicator]].sum()
                    bo_table[tunnel.name]=amount
                table_0[time]=bo_table
            table=pd.DataFrame(table_0).transpose()
            return table
        else:
            tunnel=self.Tunnel_Dict[name]
            for time in table_0.keys():
                y=time[0:4]
                m=time[4:6]
                df=tunnel.Collisions[y][m]
                if Indicator==1:
                    table_0[time]=table_0[time]+len(df['CollisionKey'].unique())
                else:
                    table_0[time]=table_0[time]+df[self.Indicator[Indicator]].sum()
            table=pd.DataFrame(pd.Series(table_0),columns=[name])
            return table
    
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
        self.TableDICT_Init()
        df=self.Table_Dict[level](Indicator,name)
        
    def BoroughCompare(self,Indicator,level,name=[]):
        pass
    def RankTop10(self,Indicator,level,name=[]):
        pass



class ContributingMethods(FundamentalMethods):
    def InfluenceONSeverity(self,Influencer,SeverityMeasure,level,name=[]):
        pass
    def RelationshipBetweenInfluencer(self, Influencer0, Influencer1,level,name=[]):
        pass     