'''
This module contain all classes of methods could be applied on the information

Copyright:
@ Nan Wu, Lingshan Gao, Shucheng Yan
@ nw1045@nyu.edu; lg2755@nyu.edu; sy1253@nyu.edu
'''
import datetime
import pandas as pd
from WN_struct_building.CityStructure import borough
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from textwrap import wrap
from itertools import cycle, islice
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
import mpl_toolkits 
from mpl_toolkits.basemap import Basemap
from matplotlib.pyplot import ylabel

class FundamentalMethods():
    '''
    Methods for display the information of NYC collisions.
    All Methods class share a init function with those common useful attributes
    Attributes:
        data: a city object.
            Type: city class
        savepath: reports save to a specific path.
            Type: string
        Influencer: Factors influencing the severity of a collision
            Type: dictionary
                Keys: int (a number that used in reading and passing the influencer)
                Value: string (the name of the relevant influencer)
        Indicator:  Indicators that used to measure the the severity of the collision
            Type: dictionary
                Keys: int (a number that used in reading and passing the indicator)
                Value: string (the name of the relevant indicator)
        InfluencerDes: Detailed description of the influencer
            Type: dictionary
                Keys: int (a number that used in reading and passing the indicator)
                Value: string (the detailed description of the relevant influencer)
        TimeBegin:  the start of the period user want to analysis
            Type: list ([2015,1])
        TimeEnd: the end of the period user want to analysis
            Type: list ([2015,1])
        TimeList: ALL year and month with type of string. 
            Type: list(['201501','201502'])
    '''
    def __init__(self, city, savepath, TimeBegin,TimeEnd):
        '''
        Constructor
        '''
        self.data=city
        self.savepath=savepath # .../results/201501_201502
        self.Influencer={1 : 'VehicleType',2 : 'ContributingFactor' }
        
        self.Indicator={1 : 'Number of Collisions', 2 : 'CollisionInjuredCount', 3 : 'CollisionKilledCount',4 : 'PersonsInjured',
                        5 : 'PersonsKilled', 6 : 'MotoristsInjured', 7 : 'MotoristsKilled', 8 : 'PassengInjured', 9 : 'PassengKilled',
                        10 : 'CyclistsInjured',11 : 'CyclistsKilled',12 : 'PedestrInjured', 13 : 'PedestrKilled',14 : 'Injury_or_Fatal'}
        
        self.IndicatorPrint={1 : 'The Number of Collisions', 2 : 'CollisionInjuredCount', 3 : 'CollisionKilledCount',4 : 'The number of person injured',
                        5 : 'The number of person killed', 6 : 'The number of Motorists injured', 7 : 'The number of Motorists killed', 8 : 'The number of passenger injured', 9 : 'The number of passenger killed',
                        10 : 'The number of cyclists injured',11 : 'The number of cyclists killed',12 : 'The number of Pedestrian injured', 13 : 'The number of pedestrian killed',14 : 'Total Injury and Fatal'}
    
        self.InfluencerDes={1:'VehicleTypeDescription',2:'ContributingFactorDescription'}
        
        self.TimeBegin=TimeBegin
        self.TimeEnd=TimeEnd # [2015,1]
        start=datetime.date(self.TimeBegin[0],self.TimeBegin[1],20)
        end=datetime.date(self.TimeEnd[0],self.TimeEnd[1],20)
        ALLDATE=pd.date_range(start,end,freq='30D')
        self.TimeList=list(map(lambda date:str(date.year)+str(date.month).zfill(2), ALLDATE))
    def ContinueALL(self):
        '''
        Continue 
        '''
        flow=input("Input anything to Continue:")
        
    def CloseFigure(self):
        '''
        Close Figure Choose
        '''
        self.flag= input("Input anything to Close the Figure and Continue")
        plt.close()
        
class SituationMethods(FundamentalMethods):
    '''
    This class is for analysis of the situation of the collision.
    Provide functions calculating and generate figures for the statistical summary of each indicator in a specific level.
    Attributes:
        Table_Dict:
        
    Methods:
    0 Specific Attributes Initiating
        TableDICT_Init
    1 Type of methods is generating data frame.
        CityTable
        BoroughTable
        PrecinctTable
        PrecinctCalculate
        PrecinctTableUnit
        BoroughTableUnit
        CityTableUnit
        BTHRcalculate
        BTHRTableUnit
        PrecinctTableAll
        BoroughTableAll
        BTHRTableAll
        TunnelTable
        BridgeTable
        HighwayTable
        RoadTable
    2 Type of methods present a report
        map
        ...
    '''
    def TableDICT_Init(self):
        '''
        Initiating a Table generating function dictionary
        '''
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
            return self.BoroughTableAll(self.data.Borough_Dict, Indicator)
    
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
    
    def PrecinctCalculate(self,Indicator,df): 
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
            return len(df['CollisionKey'].unique())
        else:
            return df[self.Indicator[Indicator]].sum()
    
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
            try:
                df1 = Precinct.Collisions_intersection[time[0:4]][time[4:6]]
                table_0[time]=table_0[time]+self.PrecinctCalculate(Indicator, df1)
            except KeyError:
                pass
            try:
                df2 = Precinct.Collisions_HighTunBri[time[0:4]][time[4:6]]
                table_0[time]=table_0[time]+self.PrecinctCalculate(Indicator, df2)
            except KeyError:
                pass
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
                table_0[time]=table_0[time]+(self.PrecinctTableUnit(precinct, Indicator).ix[time])[0]
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
                table_0[time]=table_0[time]+(self.BoroughTableUnit(borough, Indicator).ix[time])[0]
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
        if Indicator==1:
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
            try:
                table_0[time]=self.BTHRcalculate(Indicator, BTHR.Collisions[time[0:4]][time[4:6]])
            except KeyError:
                pass
        table=pd.DataFrame(pd.Series(table_0),columns=[BTHR.name])
        return table
    
    def PrecinctTableAll(self,precinct_List,Indicator):
        '''
        This method will generate a data frame with index is the whole time period and columns is the all instances of precinct class in one of the Borough object in NYC.
        The value is depend on the Indication.
        
        
        Args:
           precinct_List: a dictionary contains one type of objects
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
            table[precinct.ID] = self.PrecinctTableUnit(precinct, Indicator)
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

    def briefSummary(self,Indicator,level,name='null'):
        '''
        This method calculates the total number of different collision statistics
        demanded by the user. Each indicator variable refers to a collision measure,
        such as the number of people injured, the number of people killed
        '''
        self.TableDICT_Init()
        print(self.Table_Dict[level](Indicator,name))
        df = self.Table_Dict[level](Indicator,name)
        if name == 'null':        
            rowSum = df.sum(axis = 1)
            totalSum = rowSum.sum(axis = 0)
            print(self.IndicatorPrint[Indicator] + ' on the ' + level + ' level ' + ' is ' + str(totalSum))
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            
        else:
            totalSum = df.sum(axis = 0)
            print(self.IndicatorPrint[Indicator] + ' in ' + name + ' is ' + str(totalSum.ix[0]))
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        
        self.ContinueALL()
    
    
    def SavePathset(self,Indicator,level,name):
        '''
        Save file name
        Args:
            level: 'Bridge','Highway','Tunnel','Road','City','Borough','Precinct'
            name: null or a specific name
            Influencer: Factors influencing the severity of a collision
            Type: dictionary
                Keys: int (a number that used in reading and passing the influencer)
                Value: string (the name of the relevant influencer)
            Indicator:  Indicators that used to measure the the severity of the collision
            Type: dictionary
                Keys: int (a number that used in reading and passing the indicator)
                Value: string (the name of the relevant indicator)
        Return:
            string
        '''
        return ''.join([self.savepath,'/Time Series analysis on',level,'-',name,' by ', self.Indicator[Indicator],'.pdf'] 
                        if name!='null' else [self.savepath,'/Time Series analysis on ',level," by ", self.Indicator[Indicator],'.pdf'])
         
    def PlotbyMonth(self,Indicator,level,name='null'):
        '''
        This method generate a time series plot for a collision statistics demanded
        by the user
        '''
        self.TableDICT_Init()
        df = self.Table_Dict[level](Indicator,name)
        if name == 'null':
            rowsum = df.sum(axis = 1)
            ax = rowsum.plot(kind = 'bar',
                             title='Time Series analysis on ' + level + ' level')
            figure = ax.get_figure()
            ax.set_xlabel('Time')
            ax.set_ylabel(self.IndicatorPrint[Indicator])
            figure.subplots_adjust(bottom=0.20)
            figure.show()
            self.CloseFigure()
            
            figure.savefig(self.SavePathset(Indicator,level,name))
            print("Figure has been saved.")
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        else:
            #totalSum = df.sum(axis = 0)
            totalSum=df
            ax = totalSum.plot(kind = 'bar',
                               title='Time Series analysis for ' + name)
            figure = ax.get_figure()
            ax.set_xlabel('Time')
            ax.set_ylabel(self.IndicatorPrint[Indicator])
            figure.subplots_adjust(bottom=0.20)
            #figure.title('Time Series analysis for ' + name)
            #figure.ylabel(self.IndicatorPrint[Indicator])
            #figure.xlabel('Time')
            figure.show()
            
            self.CloseFigure()
            figure.savefig(self.SavePathset(Indicator,level,name))
        
            print("Figure has been saved.")
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        self.ContinueALL()
    def GetSum(self,Indicator,level,name):  
        '''
        this method calculates the total sum of collision statistics returned from the dataframe
        '''
        df=self.Table_Dict[level](Indicator,name)
        if name == 'null':
            rowSum = df.sum(axis = 1)
            totalSum = rowSum.sum(axis = 0)
        else:
            totalSum = df.sum(axis = 0)
            totalSum = totalSum.ix[0]
        return totalSum
    
    def Pieconponent(self,level,name='null'):
        '''
        This medhod retuens a dataframe in which the total number of injury and killed combined 
        are calculated for different people on the road.
        
        Example:
                         InjuredandKill
           Cyclists                1.0
           Motorists             514.0
           Passengers            381.0
           Pedestrians             4.0
        '''
        dfFORpie=dict.fromkeys(['MotoristsInjured', 'MotoristsKilled',  'PassengInjured',   'PassengKilled',
                         'CyclistsInjured', 'CyclistsKilled', 'PedestrInjured',  'PedestrKilled'])
        
        self.TableDICT_Init()
        for indicator in range(6,14):
            sum = self.GetSum(indicator, level, name)
            dfFORpie[self.Indicator[indicator]]=sum
        dfpie={'Motorists':dfFORpie['MotoristsInjured']+dfFORpie['MotoristsKilled'],  
               'Passengers':dfFORpie['PassengInjured']+dfFORpie['PassengKilled'], 
               'Cyclists':dfFORpie['CyclistsInjured']+dfFORpie['CyclistsKilled'], 
               'Pedestrians':dfFORpie['PedestrInjured']+dfFORpie['PedestrKilled']}
        df=pd.DataFrame(dfpie,index=['InjuredandKill'])
        df = df.transpose()
        return df 
    def InjuryKillPIE(self,level,name='null',Indicator = 'null'):
        '''
        This method draws the pie chart to campare the number of injury and killed combined for
        different kinds of people.
        '''
        
        dfPie = self.Pieconponent(level, name)
        print(dfPie)
        colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
        ax = dfPie.plot(kind = 'pie', y= 'InjuredandKill', title = 'pie chart comparison for injury and killed combined',
                      colors=colors, shadow = True, startangle = 90, autopct = '%1.1f%%')
        figure = ax.get_figure()
        figure.show()
        self.CloseFigure()
        figure.savefig(self.savepath + '/PieChart_for_' + level + '_level')
        print("Figure has been saved.")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        self.ContinueALL()

    def RankTop10(self, Indicator, level, name='null'):    
        '''
        This method returns the the number of top 10 of a Collision statistic demanded by user.
        '''
        self.TableDICT_Init()
        df = self.Table_Dict[level](Indicator,name)
        if name == 'null':
            rowSum = df.sum(axis = 1)
            rowSumFrame = pd.DataFrame(rowSum, columns = [self.Indicator[Indicator]])
            sortedFrame = rowSumFrame.sort(columns = self.Indicator[Indicator], ascending =False)
            if int(len(sortedFrame.index)) >= 10 :
                print(sortedFrame.head(n = 10))
            else:
                print(sortedFrame)
                
        else:
            sortedFrame = df.sort(columns = name, ascending = False)
            if int(len(df.index)) >= 10:
                print(sortedFrame.head(n = 10))
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            else:
                print(sortedFrame)
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        self.ContinueALL()
        
    def Map(self,Indicator,level,name='null'):

        # References:
        # http://stackoverflow.com/questions/6028675/setting-color-range-in-matplotlib-patchcollection
        # http://basemaptutorial.readthedocs.io/en/latest/shapefile.html
        # Precinct shapefile source : https://nycopendata.socrata.com/Public-Safety/Police-Precincts/78dh-3ptz/data
        # Borough boundaries shapefile source: https://data.cityofnewyork.us/City-Government/Borough-Boundaries/tqmj-j8zm/data
        '''
        This function plots a heatmap for number of collisions happen in each area.
        The function takes three inputs:
        level: string type. 'borough' or 'precinct'
        name: string type. Borough name. 'mn' for Manhattan, 'bk' for Brooklyn, 'bn' for Bronx, 'si' for 'Staten Island', 'qn' for Queens
        indicator: string type. The metrics that the user would like to use, such as 'number of people injured' or 'number of collisions happened'
        '''
        # Create map related variables
        patches = []
        color_list = []
        fig, ax = plt.subplots()
        # Draw a basemap according to the geographic level
        mapbase = Basemap(projection='mill',
                          llcrnrlat = 40.492,
                          llcrnrlon = -74.272,
                          urcrnrlat = 40.930,
                          urcrnrlon = -73.670,
                          resolution='c')
        mapbase.fillcontinents(color='white')
 
        # Call TableDICT to extract data
        self.TableDICT_Init()
 
        # if 'borough' level and name of the borough are not specified, then plots a heatmap for NYC by boroughs.
        if (level == 'Borough') and (name == 'null'):
            df = self.Table_Dict[level](Indicator)
            plot_series = df.sum()
            # Draw borough bounds
            mapbase.readshapefile('BoroughBound/boroughshape', 'boroughmaps', drawbounds=True)
            
            # Color the boroughs based on their value of the indicator
            for i in range(len(mapbase.boroughmaps)):
                info = mapbase.boroughmaps_info[i]
                shape = mapbase.boroughmaps[i]
                area = str(info['boro_name'])
                if area in plot_series.index:
                    color_list.append(plot_series.loc[area])
                    polygons = Polygon(np.array(shape), True)
                    patches.append(polygons)
        else:
            # if 'borough' level and name of the borough are listed, then plots a heatmap for NYC these boroughs by precinct
            if (level == 'Borough') and (name in ['mn', 'bk', 'bx', 'qn', 'si']):
                df = self.PrecinctTableAll(self.data.Borough_Dict[name].precinctList, Indicator)
            # if 'precinct' level, then plot a heatmap by precinct for the entire city.
            elif level == 'Precinct':
                df = self.Table_Dict[level](Indicator)
            
            # Add dataframe by column
            plot_series = df.sum()
            # Draw precinct bounds
            mapbase.readshapefile('PrecinctBound/precinctshape', 'precinctmaps', drawbounds=True)
                    
            # Sum the data frame by column
            plot_series = df.sum()
            # Color the precincts based on their value of the indicator
            for i in range(len(mapbase.precinctmaps)):
                info = mapbase.precinctmaps_info[i]
                shape = mapbase.precinctmaps[i]
                area = "{0:0=3d}".format(int(info['precinct']))
                if area in plot_series.index:
                    color_list.append(plot_series.loc[area])
                    polygons = Polygon(np.array(shape), True)
                    patches.append(polygons)

        colors = np.array(color_list)
        polygons = PatchCollection(patches, cmap=matplotlib.cm.jet, alpha=0.5)
        polygons.set_array(colors)
        ax.add_collection(polygons)
        plt.colorbar(polygons)
        fig.show()
        self.CloseFigure()
        fig.savefig(self.savepath +'/Heatmap '+ level + name)
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("Figure has been saved.")
        self.ContinueALL()
        
    def BoroughCompare(self,Indicator,level,name='null'):
        '''
        This method is designed specfically for 5 boroughs. Users can see a comparision
        of the collision statistics they choose among 5 boroughs.
        '''
        self.TableDICT_Init()
        df = self.Table_Dict[level](Indicator,name)
        sumTime = df.sum(axis = 0)
        ax=sumTime.plot(kind = 'bar',
                        rot=0,
                        title='Borough Comparision')
        figure = ax.get_figure()
        ax.set_xlabel('Boroughs')
        ax.set_ylabel(self.IndicatorPrint[Indicator])
        #figure.ylabel(self.IndicatorPrint[Indicator])
        #figure.xlabel('Boroughs')
        figure.show()
        self.CloseFigure()
        figure.savefig(self.savepath+'/Borough_comp_by ' + self.Indicator[Indicator])
        print("Figure has been saved.")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        self.ContinueALL()
        
    def RankTop10(self, Indicator, level, name='null'):    
        '''
        This method returns the the number of top 10 of a Collision statistic demanded by user.
        '''
        self.TableDICT_Init()
        df = self.Table_Dict[level](Indicator,name)
        if name == 'null':
            rowSum = df.sum(axis = 1)
            rowSumFrame = pd.DataFrame(rowSum, columns = [self.Indicator[Indicator]])
            sortedFrame = rowSumFrame.sort(columns = self.Indicator[Indicator], ascending =False)
            if int(len(sortedFrame.index)) >= 10:
                print(sortedFrame.head(n = 10))
            else:
                print(sortedFrame)
                
        else:
            sortedFrame = df.sort(columns = name, ascending = False)
            if int(len(df.index)) >= 10:
                print(sortedFrame.head(n = 10))
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            else:
                print(sortedFrame)
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        self.ContinueALL()
        
class ContributingMethods(FundamentalMethods):
    '''
    This class is for analysis of the contributing factors of all collision.
    Provide functions calculating and generate figures for the statistical summary of 
    how influencers influence each indicator in a specific level.
    Attributes:
        Inf_Dict: dictionary of table functions
        vehicleType: dictionary of vehicleType description
        ContributingFactor: ContributingFactor of vehicleType description
        index: 1: influencer type (vehicleType,ContributingFactor)
        
    Methods:
    0 Specific Attributes Initiating
        InfDICT_Init
    1 Type of methods is generating data frame.
        InfCalculate
        TableInit_WITH0
        precinctInfTable_Unit
        BTHRInfTable_Unit
        BTHRInfTable_All
        BoroughInfTable_Unit
        CityInfTable_Unit
        precinctInfTable
        boroughInfTable
        cityInfTable
        BridgeInfTable
        HighwayInfTable
        TunnelInfTable
        BridgeTable
        RoadInfTable
        
    2 Type of methods present a report
        InfluenceONSeverity
            CloseFigure
            Colorset
            Labelset
            Titleset
            SavePathset
            BarPlot
    '''
    def InfCalculate(self,indicator,influencer,Collisions,Factors):
        '''
        Given two dataframe of collisions and factors. Calculate the sum value of indicators for each type of influencer.  
    
        Args:
            indicator: int - the numerical label of a indicator
            influencer: int - the numerical label of a influencer
            Collisions: data frame
            Factors: data frame
        Return: 
            data frame: 
                Index : all types in the influencer
                columns: indicator
                                         indicator
            Influencer Value Type1          10
            Influencer Value Type2          20
            ...                             30
            Influencer Value TypeN          40
        Raise:
        
        '''
        if indicator==1:
            df=Factors[[self.InfluencerDes[influencer],'CollisionKey']].groupby([self.InfluencerDes[influencer]])['CollisionKey'].unique()
            return pd.DataFrame(pd.Series(map(lambda x:len(x),df),index=df.index),columns=[self.Indicator[1]])
        else:
            df=pd.merge(Factors[[self.InfluencerDes[influencer],'CollisionKey']],Collisions[[self.Indicator[indicator],'CollisionKey']], how='left', on='CollisionKey')
            return pd.DataFrame(df.groupby([self.InfluencerDes[influencer]])[self.Indicator[indicator]].sum())
    def TableInit_WITH0(self,indicator,influencer):
        '''
        table init with all possible influencer, value 0
        '''
        return pd.DataFrame(np.zeros(len(self.index[influencer])),index=self.index[influencer],columns=[self.Indicator[indicator]])
    def precinctInfTable_Unit(self,precinct,indicator,influencer):
        '''
        Calculate the sum value of indicators for each type of influencer of all the time interval on a precinct.  
        Args:
            precinct: a precinct object
            indicator: int - the numerical label of a indicator
            influencer: int - the numerical label of a influencer
        Return: 
            data frame: 
                Index : all types in the influencer
                columns: indicator
                                         indicator
            Influencer Value Type1          10
            Influencer Value Type2          20
            ...                             30
            Influencer Value TypeN          40
        Raise:
            KeyError
        '''
        table=self.TableInit_WITH0(indicator,influencer)
        for time in self.TimeList:
            try:
                Collisions_i = precinct.Collisions_intersection[time[0:4]][time[4:6]]
                Factors_i = precinct.Factors_intersection[time[0:4]][time[4:6]]
                table=table.add(self.InfCalculate(indicator,influencer,Collisions_i,Factors_i),fill_value=0)
            except KeyError:
                pass
            try:
                Collisions_H = precinct.Collisions_HighTunBri[time[0:4]][time[4:6]]
                Factors_H = precinct.Factors_HighTunBri[time[0:4]][time[4:6]]
                table=table.add(self.InfCalculate(indicator,influencer,Collisions_H,Factors_H),fill_value=0)
            except KeyError:
                pass
        return table        
        
    def BTHRInfTable_Unit(self,BTHR,indicator,influencer):
        '''
        Calculate the sum value of indicators for each type of influencer of all the time interval on a road,tunnel,highway or bridge.  
        Args:
            BTHR: a object of road,tunnel,highway or bridge class
            indicator: int - the numerical label of a indicator
            influencer: int - the numerical label of a influencer
        Return: 
            data frame: 
                Index : all types in the influencer
                columns: indicator
                                         indicator
            Influencer Value Type1          10
            Influencer Value Type2          20
            ...                             30
            Influencer Value TypeN          40
        Raise:
            KeyError
        '''
        table=self.TableInit_WITH0(indicator,influencer)
        for time in self.TimeList:
            try:
                Collisions = BTHR.Collisions[time[0:4]][time[4:6]]
                Factors = BTHR.Factors[time[0:4]][time[4:6]]
                table = table.add(self.InfCalculate(indicator,influencer,Collisions,Factors),fill_value=0)
            except KeyError:
                pass
        return table
    
    def BTHRInfTable_All(self,BTHR_Dict,indicator,influencer):
        '''
        Calculate the sum value of indicators for each type of influencer of all the time interval on all roads, tunnels, bridges or highways.  
        Args:
            BTHR_Dict: a dictionary of objects of road,tunnel,highway or bridge class
            indicator: int - the numerical label of a indicator
            influencer: int - the numerical label of a influencer
        Return: 
            data frame: 
                Index : all types in the influencer
                columns: indicator
                                         indicator
            Influencer Value Type1          10
            Influencer Value Type2          20
            ...                             30
            Influencer Value TypeN          40
        Raise:
            KeyError
        '''
        table=self.TableInit_WITH0(indicator,influencer)
        for BTHR in BTHR_Dict.values():
            table = table.add(self.BTHRInfTable_Unit(BTHR, indicator, influencer),fill_value=0)
        return table
    
    def BoroughInfTable_Unit(self,borough,indicator,influencer):
        '''
        Calculate the sum value of indicators for each type of influencer of all the time interval on a borough.  
        Args:
            borough: a precinct object
            indicator: int - the numerical label of a indicator
            influencer: int - the numerical label of a influencer
        Return: 
            data frame: 
                Index : all types in the influencer
                columns: indicator
                                         indicator
            Influencer Value Type1          10
            Influencer Value Type2          20
            ...                             30
            Influencer Value TypeN          40
        Raise:
            KeyError
        '''
        table=self.TableInit_WITH0(indicator,influencer)
        for precinct in borough.precinctList.values():
            table = table.add(self.precinctInfTable_Unit(precinct,indicator,influencer),fill_value=0)
        return table
    
    def CityInfTable_Unit(self,city,indicator,influencer):
        '''
        Calculate the sum value of indicators for each type of influencer of all the time interval on a city.  
        Args:
            city: a city object
            indicator: int - the numerical label of a indicator
            influencer: int - the numerical label of a influencer
        Return: 
            data frame: 
                Index : all types in the influencer
                columns: indicator
                                         indicator
            Influencer Value Type1          10
            Influencer Value Type2          20
            ...                             30
            Influencer Value TypeN          40
        Raise:
            KeyError
        '''
        table=self.TableInit_WITH0(indicator,influencer)
        for borough in city.Borough_Dict.values():
            table = table.add(self.BoroughInfTable_Unit(borough,indicator,influencer),fill_value=0)
        return table

    def precinctInfTable(self,Influencer,Indicator,name):
        '''
        Calculate the sum value of indicators for each type of influencer of all the time interval on a precinct.  
        Args:
            Influencer: int - the numerical label of a indicator
            Indicator:int - the numerical label of a influencer
            name: a precinct ID 
        Return:
            data frame: 
                Index : all types in the influencer
                columns: indicator
                                         indicator
            Influencer Value Type1          10
            Influencer Value Type2          20
            ...                             30
            Influencer Value TypeN          40
        '''
        if name!='null':
            #name not null (is one of keys, could be call)
            #call the function Unit
            for borough in self.data.Borough_Dict.values():
                if name in borough.precinctList.keys():
                    return self.precinctInfTable_Unit(borough.precinctList[name],Indicator,Influencer)
        else:
            print("This method could not be applied on not a specific precinct!")
               
    def boroughInfTable(self,Influencer,Indicator,name):
        '''
        Calculate the sum value of indicators for each type of influencer of all the time interval on a borough.  
        Args:
            Influencer: int - the numerical label of a indicator
            Indicator:int - the numerical label of a influencer
            name: a borough name
        Return:
            data frame: 
                Index : all types in the influencer
                columns: indicator
                                         indicator
            Influencer Value Type1          10
            Influencer Value Type2          20
            ...                             30
            Influencer Value TypeN          40
        '''
        try:
            return self.BoroughInfTable_Unit(self.data.Borough_Dict[name], Indicator, Influencer)
        except KeyError:
            print("This method could not be applied on not a specific precinct!")
            
    def cityInfTable(self,Influencer,Indicator,name='null'):
        '''
        Calculate the sum value of indicators for each type of influencer of all the time interval on a city.  
        Args:
            Influencer: int - the numerical label of a indicator
            Indicator:int - the numerical label of a influencer
            name: a city name
        Return:
            data frame: 
                Index : all types in the influencer
                columns: indicator
                                         indicator
            Influencer Value Type1          10
            Influencer Value Type2          20
            ...                             30
            Influencer Value TypeN          40
        '''
        return self.CityInfTable_Unit(self.data, Indicator, Influencer)
    
    def BridgeInfTable(self,Influencer,Indicator,name='null'):
        '''
        Calculate the sum value of indicators for each type of influencer of all the time interval on a Bridge.  
        Args:
            Influencer: int - the numerical label of a indicator
            Indicator:int - the numerical label of a influencer
            name: a bridge name or null
        Return:
            data frame: 
                Index : all types in the influencer
                columns: indicator
                                         indicator
            Influencer Value Type1          10
            Influencer Value Type2          20
            ...                             30
            Influencer Value TypeN          40
        '''
        try:
            #name not null (is one of keys, could be call)
            #call the function Unit
            return self.BTHRInfTable_Unit(self.data.Bridge_Dict[name], Indicator,Influencer) 
        except KeyError:
            #name is null (is not one of keys, could be call)
            #call the function All
            return self.BTHRInfTable_All(self.data.Bridge_Dict, Indicator,Influencer)
    
    def HighwayInfTable(self,Influencer,Indicator,name='null'):
        '''
        Calculate the sum value of indicators for each type of influencer of all the time interval on a highway.  
        Args:
            Influencer: int - the numerical label of a indicator
            Indicator:int - the numerical label of a influencer
            name: a highway name or null
        Return:
            data frame: 
                Index : all types in the influencer
                columns: indicator
                                         indicator
            Influencer Value Type1          10
            Influencer Value Type2          20
            ...                             30
            Influencer Value TypeN          40
        '''
        try:
            #name not null (is one of keys, could be call)
            #call the function Unit
            return self.BTHRInfTable_Unit(self.data.Highway_Dict[name], Indicator,Influencer) 
        except KeyError:
            #name is null (is not one of keys, could be call)
            #call the function All
            return self.BTHRInfTable_All(self.data.Highway_Dict, Indicator,Influencer)
    
    def TunnelInfTable(self,Influencer,Indicator,name='null'):
        '''
        Calculate the sum value of indicators for each type of influencer of all the time interval on a tunnel.  
        Args:
            Influencer: int - the numerical label of a indicator
            Indicator:int - the numerical label of a influencer
            name: a tunnel name or null
        Return:
            data frame: 
                Index : all types in the influencer
                columns: indicator
                                         indicator
            Influencer Value Type1          10
            Influencer Value Type2          20
            ...                             30
            Influencer Value TypeN          40
        '''
        try:
            #name not null (is one of keys, could be call)
            #call the function Unit
            return self.BTHRInfTable_Unit(self.data.Tunnel_Dict[name], Indicator,Influencer) 
        except KeyError:
            #name is null (is not one of keys, could be call)
            #call the function All
            return self.BTHRInfTable_All(self.data.Tunnel_Dict, Indicator,Influencer)
    
    def RoadInfTable(self,Influencer,Indicator,name='null'):
        '''
        Calculate the sum value of indicators for each type of influencer of all the time interval on a road.  
        Args:
            Influencer: int - the numerical label of a indicator
            Indicator:int - the numerical label of a influencer
            name: a road name  or null
        Return:
            data frame: 
                Index : all types in the influencer
                columns: indicator
                                         indicator
            Influencer Value Type1          10
            Influencer Value Type2          20
            ...                             30
            Influencer Value TypeN          40
        '''
        try:
            #name not null (is one of keys, could be call)
            #call the function Unit
            return self.BTHRInfTable_Unit(self.data.Road_Dict[name], Indicator,Influencer) 
        except KeyError:
            #name is null (is not one of keys, could be call)
            #call the function All
            return self.BTHRInfTable_All(self.data.Road_Dict, Indicator,Influencer)
        
    def InfDICT_Init(self):
        '''
        specific class attributes init
        
        '''
        self.Inf_Dict={'City':self.cityInfTable,'Borough': self.boroughInfTable,'Precinct':self.precinctInfTable,
                       'Highway':self.HighwayInfTable,'Tunnel':self.TunnelInfTable,'Bridge':self.BridgeInfTable,'Road':self.RoadInfTable} 
        self.vehicleType=['ALL-TERRAIN VEHICLE','AMBULANCE','BICYCLE','BUS','FIRE TRUCK','LARGE COM VEH(6 OR MORE TIRES)',
                          'MOTORCYCLE','PASSENGER VEHICLE','PEDICAB','PICK-UP TRUCK','SMALL COM VEH(4 TIRES)',
                          'SPORT UTILITY / STATION WAGON','TAXI VEHICLE','VAN','UNKNOWN']
        self.ContributingFactor=['None', 'Following too closely', 'Outside car distraction',
       'Alcohol involvement', 'Driver inattention/distraction',
       'Unsafe lane changing', 'Failure to yield right-of-way',
       'Lost consciousness', 'Fell asleep', 'Turning improperly',
       'Unsafe speed', 'Passing too closely',
       'Passing or lane usage improper', 'Driver inexperience',
       'Other uninvolved vehicle', 'Backing unsafely',
       'Traffic control disregarded', 'Passenger distraction',
       'Drugs (illegal)', 'Pedest/bike/other pedest error',
       'Failure to keep right', 'Cell phone (hand-held)',
       'Aggressive driving/road rage', 'Illness', 'Fatigued/drowsy',
       'Other electronic device', 'Physical disability',
       'Using on board navigate device']
        
        self.ContributingFactor=[z.upper() for z in self.ContributingFactor]
        
        self.index={1:self.vehicleType,2:self.ContributingFactor}
    
    def Colorset(self,df):
        '''
        Args:
            df: data frame
        return:
            list of [x,y,z] RGB color 
        
        '''
        return  [(x/(len(df)+5), x/(len(df)+5), 0.75) for x in range(len(df))]  
    
    def Labelset(self,df):
        '''
        Args:
            df: data frame
        return:
            shorted index string
        '''
        return ['\n'.join(wrap(l, 40)) for l in df.index]
    
    def Titleset(self,level,name,Indicator,Influencer):
        '''
        Set title
        Args:
            level: 'Bridge','Highway','Tunnel','Road','City','Borough','Precinct'
            name: null or a specific name
            Influencer: Factors influencing the severity of a collision
            Type: dictionary
                Keys: int (a number that used in reading and passing the influencer)
                Value: string (the name of the relevant influencer)
            Indicator:  Indicators that used to measure the the severity of the collision
            Type: dictionary
                Keys: int (a number that used in reading and passing the indicator)
                Value: string (the name of the relevant indicator)
        Return:
            string
        '''
        return ' '.join([self.InfluencerDes[Influencer], self.Indicator[Indicator],'\n',level,'-',name,'\n',self.TimeList[0],'to', self.TimeList[-1]] 
                        if name!='null' else [self.InfluencerDes[Influencer]," on ", self.Indicator[Indicator],'\n',level,'\n',self.TimeList[0],'to', self.TimeList[-1]])
    def SavePathset(self,Influencer,Indicator,level,name):
        '''
        Save file name
        Args:
            level: 'Bridge','Highway','Tunnel','Road','City','Borough','Precinct'
            name: null or a specific name
            Influencer: Factors influencing the severity of a collision
            Type: dictionary
                Keys: int (a number that used in reading and passing the influencer)
                Value: string (the name of the relevant influencer)
            Indicator:  Indicators that used to measure the the severity of the collision
            Type: dictionary
                Keys: int (a number that used in reading and passing the indicator)
                Value: string (the name of the relevant indicator)
        Return:
            string
        '''
        return ''.join([self.savepath,'/',self.InfluencerDes[Influencer],'_', self.Indicator[Indicator],'_',level,'-',name,'_','.pdf'] 
                        if name!='null' else [self.savepath,'/',self.InfluencerDes[Influencer]," on ", self.Indicator[Indicator],'_',level,'.pdf'])
    def BarPlot(self,df,Influencer,Indicator,level,name):
        '''
        Generate a bar chart
        Args:
            df: dataframe
            level: 'Bridge','Highway','Tunnel','Road','City','Borough','Precinct'
            name: null or a specific name
            Influencer: Factors influencing the severity of a collision
                Type: dictionary
                Keys: int (a number that used in reading and passing the influencer)
                Value: string (the name of the relevant influencer)
            Indicator:  Indicators that used to measure the the severity of the collision
                Type: dictionary
                Keys: int (a number that used in reading and passing the indicator)
                Value: string (the name of the relevant indicator)
        Return:
            string
        Raise:
            TypeError
        '''
        ax = df.sort_values(by=[self.Indicator[Indicator]]).plot.barh(
            title=self.Titleset(level, name,Indicator,Influencer),
            figsize=(10,10), 
            legend=True, 
            fontsize=10,
            color=self.Colorset(df),
            #rot=10
            )
        
        #ax.set_yticklabels(self.Labelset(df),rotation=20)
        
        figure = ax.get_figure()
        figure.subplots_adjust(left=0.30)
        figure.show()
        
        self.CloseFigure()
        figure.savefig(self.SavePathset(Influencer, Indicator,level,name))
        
        print("Figure has been saved.")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
       
    def InfluenceONSeverity(self,Influencer,Indicator,level,name='null'):
        '''
        Generate a bar chart about the influenceo on severity
        Args:
            level: 'Bridge','Highway','Tunnel','Road','City','Borough','Precinct'
            name: null or a specific name
            Influencer: Factors influencing the severity of a collision
                Type: dictionary
                Keys: int (a number that used in reading and passing the influencer)
                Value: string (the name of the relevant influencer)
            Indicator:  Indicators that used to measure the the severity of the collision
                Type: dictionary
                Keys: int (a number that used in reading and passing the indicator)
                Value: string (the name of the relevant indicator)
        '''
        
        self.InfDICT_Init()
        df = self.Inf_Dict[level](Influencer,Indicator,name)
        
        try:
            self.BarPlot(df,Influencer,Indicator,level,name)
            self.ContinueALL()
        except TypeError:
            print("No information.")
            raise
