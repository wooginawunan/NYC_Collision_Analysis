'''
Created on Dec 2, 2016

@author: apple
'''
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from WN_struct_building.CityStructure import borough
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from mpl_toolkits.basemap import Basemap


'''
References:
http://stackoverflow.com/questions/6028675/setting-color-range-in-matplotlib-patchcollection
http://basemaptutorial.readthedocs.io/en/latest/shapefile.html
Shapefile source:
https://nycopendata.socrata.com/Public-Safety/Police-Precincts/78dh-3ptz/data
'''

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
    
    def CityTable(self,Indicator,name='null'):
        '''
        Out Put Same as the CityTableUnit
        '''
        return self.CityTableUnit(self.data,Indicator)
    def BoroughTable(self,Indicator,name='null'):
        '''
        This method will be the main interacting function will functional methods.
        It will return a data frame with one column when name is specific (not null).
        And it will return a data frame with many columns when name is null. 
        '''
        try:
            #name not null (is one of keys, could be call)
            #call the function Unit
            return self.BoroughTableUnit(self.data.Borough_Dict[name], Indicator)
        except KeyError:
            #name is null (is not one of keys, could be call)
            #call the function All
            return self.BTHRTableAll(self.data.Tunnel_Dict, Indicator)
    
    def PrecinctTable(self,Indicator,name='null'):
        '''
        This method will be the main interacting function will functional methods.
        It will return a data frame with one column when name is specific (not null).
        And it will return a data frame with many columns (all precinct in the City) when name is null. 
        '''
        if name!='null':
            #name not null (is one of keys, could be call)
            #call the function Unit
            for borough in self.data.Borough_Dict.values():
                if name in borough.precinctList.keys():
                    return self.PrecinctTableUnit(borough.precinctList[name],Indicator)   
        else:
            #name is null (is not one of keys, could be call)
            #call the function All
            
            pre_List=dict()
            for borough in self.data.Borough_Dict.values():
                pre_List.update(borough.precinctList)
            return self.PrecinctTableAll(pre_List, Indicator)
    
    
         
                            
   
    def PrecinctCalculate(self,Indicator,df1,df2): 
        '''
        This method calculate the value of a specific Indicator on specific area and time 
        Args:
           Indicator: one possible indicator of the severity of the collision
           df: Data frame
        Return:
           the value 
        
        Raise:
        '''
        if Indicator==1:
            return len(df1['CollisionKey'].unique())+len(df2['CollisionKey'].unique())
        else:
            return df1[self.Indicator[Indicator]].sum()+df2[self.Indicator[Indicator]].sum() 
    def PrecinctTableUnit(self,Precinct,Indicator):
        '''
        This method will generate a data frame index is the whole time period and columns is a specific Precinct.
        Args:
           Precinct: an instance of precinct class
           Indicator: one possible indicator of the severity of the collision
        Return:
           table: Data Frame
           Example:
                if the indication is number of collisions
                         060(PrecinctID)
                Index       
                201501       10        
                201502       11                
                201503       12
        Raise:
        
        '''
        table_0=dict.fromkeys(self.TimeList,0)
        for time in table_0.keys():
            table_0[time]=self.PrecinctCalculate(Indicator, 
                                                 Precinct.Collisions_intersection[time[0:4]][time[4:6]], 
                                                 Precinct.Collisions_HighTunBri[time[0:4]][time[4:6]])
        table=pd.DataFrame(pd.Series(table_0),columns=[Precinct.ID])
        return table
    def BoroughTableUnit(self,Borough,Indicator):
        '''
        This method will generate a data frame index is the whole time period and columns is a specific Borough.
        Args:
           Borough: an instance of borough class
           Indicator: one possible indicator of the severity of the collision
        Return:
           table: Data Frame
           Example:
                if the indication is number of collisions
                         Manhattan (Borough_name)
                Index       
                201501       10        
                201502       11                
                201503       12
        Raise:
        
        '''
        table_0=dict.fromkeys(self.TimeList,0)
        for time in table_0.keys():
            for precinct in Borough.precinctList.values():
                table_0[time]=table_0[time]+self.PrecinctTableUnit(precinct, Indicator).ix[time]
        table=pd.DataFrame(pd.Series(table_0),columns=[Borough.name])
        return table
    
        
        
    def CityTableUnit(self,City,Indicator):
        '''
        This method will generate a data frame index is the whole time period and columns is a specific City.
        Args:
           City: an instance of city class
           Indicator: one possible indicator of the severity of the collision
        Return:
           table: Data Frame
           Example:
                if the indication is number of collisions
                         New York City (city name)
                Index       
                201501       10        
                201502       11                
                201503       12
        Raise:
        
        '''
        table_0=dict.fromkeys(self.TimeList,0)
        for time in table_0.keys():
            for borough in City.Borough_Dict.values():
                table_0[time]=table_0[time]+self.BoroughTableUnit(borough, Indicator).ix[time]
        table=pd.DataFrame(pd.Series(table_0),columns=[City.name])
        return table
    def BTHRcalculate(self,Indicator,df):
        '''
        This method calculate the value of a specific Indicator on specific area and time 
        Args:
           Indicator: one possible indicator of the severity of the collision
           df: Data frame
        Return:
           the value 
        
        Raise:
        '''
        if Indicator==-1:
            return len((df['CollisionKey'].unique()))
        else:
            return df[self.Indicator[Indicator]].sum()
    def BTHRTableUnit(self,BTHR,Indicator):
        '''
        This method will generate a data frame index is the whole time period and columns is a specific Road, Bridge, Tunnel,Highway.
        Args:
           BTHR: an instance of Road, Bridge, Tunnel,Highway class
           Indicator: one possible indicator of the severity of the collision
        Return:
           table: Data Frame
           Example:
                if the indication is number of collisions
                        Bridge.name_1  
                Index       
                201501       10        
                201502       11                
                201503       12
        Raise:
        
        '''
        table_0=dict.fromkeys(self.TimeList,0)
        for time in table_0.keys():
            table_0[time]=self.BTHRcalculate(Indicator, BTHR.Collisions[time[0:4]][time[4:6]])
        table=pd.DataFrame(pd.Series(table_0),columns=[BTHR.name])
        return table
    def PrecinctTableAll(self,precinct_List,Indicator):
        '''
        This method will generate a data frame with index is the whole time period and columns is the all instances of precinct class in one of the Borough object in NYC.
        The value is depend on the Indication.
        
        
        Args:
           precint_List: a dictionary contains one type of objects  
           Indicator: one possible indicator of the severity of the collision
        Return:
           table: Data Frame
           Example:
                if the indication is number of collisions
                         PrecinctID_1   PrecinctID_2  PrecinctID_3  PrecinctID_4  PrecinctID_5'
                Index       
                201501       10       1         7        0        0
                201502       11        2        9        1        4
                201503       12        7        3        5        5
        Raise:
        
        ''' 
        table=pd.DataFrame(index=self.TimeList)
        for precinct in precinct_List.values():
            table[precinct.name] = self.PrecinctTableUnit(precinct, Indicator)
        return table
    def BoroughTableAll(self,Borough_Dict,Indicator):
        '''
        This method will generate a data frame with index is the whole time period and columns is the all instances of the Borough object in NYC.
        The value is depend on the Indication.
        
        
        Args:
           Borough_Dict: a dictionary contains one type of objects in NYC 
           Indicator: one possible indicator of the severity of the collision
        Return:
           table: Data Frame
           Example:
                if the indication is number of collisions
                         Brooklyn   Bronx  Manhattan  Queens  Staten_Island'
                Index       
                201501       10       1         7        0        0
                201502       11        2        9        1        4
                201503       12        7        3        5        5
        Raise:
        
        ''' 
        table=pd.DataFrame(index=self.TimeList)
        for borough in Borough_Dict.values():
            table[borough.name] = self.BoroughTableUnit(borough, Indicator)
        return table
    def BTHRTableAll(self,BTHR_Dict,Indicator):
        '''
        This method will generate a data frame with index is the whole time period and columns is the all instances of the BTHR object in NYC.
        The value is depend on the Indication.
        
        
        Args:
           BTHR_Dict: a dictionary contains one type of objects in NYC (Bridge_Dict, Road_Dict, Highway_Dict, Tunnel_Dict) 
           Indicator: one possible indicator of the severity of the collision
        Return:
           table: Data Frame
           Example:
                if the indication is number of collisions
                        Bridge.name_1  ...  Bridge.name_N
                Index       
                201501       10        ...     7
                201502       11                9
                201503       12                3
        Raise:
        
        '''
        table=pd.DataFrame(index=self.TimeList)
        for BTHR in BTHR_Dict.values():
            table[BTHR.name] = self.BTHRTableUnit(BTHR, Indicator)
        return table
        
    
    def RoadTable(self,Indicator,name='null'):
        '''
        This method will be the main interacting function will functional methods.
        It will return a data frame with one column when name is specific (not null).
        And it will return a data frame with many columns when name is null. 
        '''
        try:
            #name not null (is one of keys, could be call)
            #call the function Unit
            return self.BTHRTableUnit(self.data.Road_Dict[name], Indicator) 
        except KeyError:
            #name is null (is not one of keys, could be call)
            #call the function All
            return self.BTHRTableAll(self.data.Road_Dict, Indicator)
        
    def HighwayTable(self,Indicator,name='null'):
        '''
        This method will be the main interacting function will functional methods.
        It will return a data frame with one column when name is specific (not null).
        And it will return a data frame with many columns when name is null. 
        '''
        try:
            #name not null (is one of keys, could be call)
            #call the function Unit
            return self.BTHRTableUnit(self.data.Highway_Dict[name], Indicator) 
        except KeyError:
            #name is null (is not one of keys, could be call)
            #call the function All
            return self.BTHRTableAll(self.data.Highway_Dict, Indicator)
    def BridgeTable(self,Indicator,name='null'):
        '''
        This method will be the main interacting function will functional methods.
        It will return a data frame with one column when name is specific (not null).
        And it will return a data frame with many columns when name is null. 
        '''
        try:
            #name not null (is one of keys, could be call)
            #call the function Unit
            return self.BTHRTableUnit(self.data.Bridge_Dict[name], Indicator) 
        except KeyError:
            #name is null (is not one of keys, could be call)
            #call the function All
            return self.BTHRTableAll(self.data.Bridge_Dict, Indicator)
    def TunnelTable(self,Indicator,name='null'):
        '''
        This method will be the main interacting function will functional methods.
        It will return a data frame with one column when name is specific (not null).
        And it will return a data frame with many columns when name is null. 
        '''
        try:
            #name not null (is one of keys, could be call)
            #call the function Unit
            return self.BTHRTableUnit(self.data.Tunnel_Dict[name], Indicator) 
        except KeyError:
            #name is null (is not one of keys, could be call)
            #call the function All
            return self.BTHRTableAll(self.data.Tunnel_Dict, Indicator)
    
    
    
    
    
    def SummaryTableCreating(self,Indicator,level,name='null'):
        pass
       # return Table
    def briefSummary(self,Indicator,level,name='null'):
        pass
        #TotalAccidennt()
        #TotalInjury()
        #TotalKilled()
    def PlotbyMonth(self,Indicator,level,name='null'):
        pass
    def InjuryKillPIE(self,level,name='null'):
        pass
    def Map(self,Indicator,level,name='null'):
        
        '''
        This function plots a heatmap for numbers of collision happen in each area.
        The function takes three inputs:
        level: string type. 'borough' or 'precinct'
        name: string type. Borough name. 'mn' for Manhattan, 'bk' for Brooklyn, 'bn' for Bronx, 'si' for 'Staten Island', 'qn' for Queens
        indicator: string type. The metrics that the user would like to use, such as 'number of people injured' or 'collision'
        '''
        # Create map related variables
        fig, ax = plt.subplots()
        patches = []
        color_list = []
        # Draw a basemap according to the geographic level
        mapbase = Basemap(projection='mill',
                          llcrnrlat = 40.492,
                          llcrnrlon = -74.272,
                          urcrnrlat = 40.930,
                          urcrnrlon = -73.670,
                          resolution='c')
                          mapbase.fillcontinents(color='white')
        mapbase.fillcontinents(color='white')
                      
        # Call TableDICT method to extract data
        self.TableDICT_Init()

        # if 'borough' level and name of the borough are not specified, then plots a heatmap for NYC by boroughs.
        if (level == 'borough') and (name == 'null'):
            df = self.Table_Dict[level](Indicator)
            mapbase.readshapefile('BoroughBound/boroughshape', 'boroughmaps', drawbounds=True)
            for i in range(len(mapbase.boroughmaps)):
                info = mapbase.boroughmaps_info[i]
                shape = mapbase.boroughmaps[i]
                area = str(info['boro_name'])
                plot_series = df.sum()
                if area in plot_series.index:
                    color_list.append(plot_series.loc[area])
                    polygons = Polygon(np.array(shape), True)
                    patches.append(polygons)

        # if 'precinct' level, then load the precinct map
        elif level == 'precinct':
        mapbase.readshapefile('PrecinctBound/precinctshape', 'precinctmaps', drawbounds=True)
            # if plot precincts for the whole city
            ## TODO: Double check inputs with Gina
            if name in ['Manhattan', 'Brooklyn', 'Bronx', 'Queens', 'Staten Island']:
                df = self.Table_Dict[level](Indicator, name)
            # if plot precincts for only one borough
            elif name == 'null':
                df = self.Table_Dict[level](Indicator)
            # Sum the data frame by column
            plot_series = df.sum()
                
            for i in range(len(mapbase.precinctmaps)):
                info = mapbase.precinctmaps_info[i]
                shape = mapbase.precinctmaps[i]
                area = str(int(info['precinct']))
                
                if area in plot_series.index:
                    color_list.append(plot_series.loc[area])
                    polygons = Polygon(np.array(shape), True)
                    patches.append(polygons)

        colors = np.array(color_list)
        polygons = PatchCollection(patches, cmap=matplotlib.cm.jet, alpha=0.5)
        polygons.set_array(colors)
        ax.add_collection(polygons)
        plt.colorbar(polygons)
        plt.show()
        
    def BoroughCompare(self,Indicator,level,name='null'):
        pass
    def RankTop10(self,Indicator,level,name='null'):
        pass



class ContributingMethods(FundamentalMethods):
    def InfluenceONSeverity(self,Influencer,SeverityMeasure,level,name='null'):
        pass
    def RelationshipBetweenInfluencer(self, Influencer0, Influencer1,level,name='null'):
        pass     