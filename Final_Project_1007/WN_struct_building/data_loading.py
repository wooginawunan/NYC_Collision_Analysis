'''
This module loads in all NYPD collisions data into a City class.
Main function:
load_data
  global variable:
      NYC 
      year, y
      month, m
      area_name. area
  sub functions:
      building_borough
      building_road
      building_bridge
      building_tunnel
      building_highway
Version 1
Copyright:
@ Nan Wu 
@ nw1045@nyu.edu
@ wooginawunan@gmail.com
'''
from WN_struct_building.CityStructure import *
import pandas as pd
import datetime
from _datetime import date
def load_data(path,TimeBegin,TimeEnd):
    
    print('Building Structures...')
    
    print('Reading File...')
    
    start=datetime.date(TimeBegin[0],TimeBegin[1],20)
    end=datetime.date(TimeEnd[0],TimeEnd[1],20)
    ALLDATE=pd.date_range(start,end,freq='30D')
    area_name=['bk','bx','mn','qn','si']
    Loading=LoadingbyStructure()
    for date in ALLDATE:
        for area in area_name:
            print(date.year,date.month,area,'...')
            #raise FileNotFoundError
            collisions_intersection, factors_intersection = load_intersection(path, str(date.year), str(date.month).zfill(2), area)
            collisions_HighTunBri, factors_HighTunBri = load_HighTunBri(path, str(date.year), str(date.month).zfill(2), area)
            Loading.building_borough(str(date.year), str(date.month).zfill(2), area, collisions_intersection, factors_intersection,collisions_HighTunBri, factors_HighTunBri )
            Loading.building_road(str(date.year), str(date.month).zfill(2), area,collisions_intersection, factors_intersection,collisions_HighTunBri, factors_HighTunBri)
            Loading.building_highway(str(date.year), str(date.month).zfill(2), area,collisions_intersection, factors_intersection,collisions_HighTunBri, factors_HighTunBri)
            Loading.building_bridge(str(date.year), str(date.month).zfill(2), area,collisions_intersection, factors_intersection,collisions_HighTunBri, factors_HighTunBri)
            Loading.building_tunnel(str(date.year), str(date.month).zfill(2), area,collisions_intersection, factors_intersection,collisions_HighTunBri, factors_HighTunBri)
    print('Success...')
    
    return Loading.NYC
            
class LoadingbyStructure():
    def __init__(self):
        self.NYC=city()
        self.NYC.init_borough()
    def building_borough(self,y,m,area,collisions_intersection, factors_intersection,collisions_HighTunBri, factors_HighTunBri):     
        '''
        Separate the collisions and factors by borough and precinct, store the data in NYC
        All changes will be stored in the global variables 
        Args: NONE
        Returns: NONE
        Raises:  NONE
        '''
        for precinctID in collisions_intersection['OccurrencePrecinctCode'].unique():
            if precinctID not in self.NYC.Borough_Dict[area].precinctList:
                precinct_new=precinct(precinctID)
            else:
                precinct_new=self.NYC.Borough_Dict[area].precinctList[precinctID]
            precinct_new.addCollisions_Intersection(y, m, collisions_intersection.ix[collisions_intersection['OccurrencePrecinctCode']==precinctID],
                                       factors_intersection.ix[factors_intersection['OccurrencePrecinctCode']==precinctID])
            self.NYC.Borough_Dict[area].precinctList[precinctID]=precinct_new
        for precinctID in collisions_HighTunBri['OccurrencePrecinctCode'].unique():
            if precinctID not in self.NYC.Borough_Dict[area].precinctList:
                precinct_new=precinct(precinctID)
            else:
                precinct_new=self.NYC.Borough_Dict[area].precinctList[precinctID]
            precinct_new.addCollisions_HighTunBri(y, m, 
                                       collisions_HighTunBri.ix[collisions_HighTunBri['OccurrencePrecinctCode']==precinctID],
                                       factors_HighTunBri.ix[factors_HighTunBri['OccurrencePrecinctCode']==precinctID])
            self.NYC.Borough_Dict[area].addprecinct(precinct_new)
                
    def building_road(self,y,m,area,collisions_intersection, factors_intersection,collisions_HighTunBri, factors_HighTunBri):
        '''
        Separate the collisions and factors by borough and precinct, store the data in NYC
        All changes will be stored in the global variables 
        Args: NONE
        Returns: NONE
        Raises:  NONE
        '''
        all_street=set(collisions_intersection['IntersectingStreet'].unique())|set(collisions_intersection['CrossStreet'].unique())
        for Road in all_street:
            if Road not in self.NYC.Road_Dict:
                Road_new=road(Road)
            else:
                Road_new=self.NYC.Road_Dict[Road]
            Marker=list(collisions_intersection.ix[list(collisions_intersection['IntersectingStreet']==Road) or list(collisions_intersection['CrossStreet']==Road)]['CollisionKey'])
            Road_new.addCollisions(y, m, collisions_intersection.ix[list(collisions_intersection['IntersectingStreet']==Road) or list(collisions_intersection['CrossStreet']==Road)],
                                       factors_intersection.ix[list(map(lambda x: x in Marker,factors_intersection['CollisionKey']))])
            self.NYC.add_road(Road_new)
#         
               
        
    def building_highway(self,y,m,area,collisions_intersection, factors_intersection,collisions_HighTunBri, factors_HighTunBri):
        '''
        Separate the collisions and factors by borough and precinct, store the data in NYC
        All changes will be stored in the global variables 
        Args: NONE
        Returns: NONE
        Raises:  NONE
        '''
        for Highway in collisions_HighTunBri.ix[collisions_HighTunBri['RoadwayTypeCode']=='H']['RoadwayName'].unique():
            if Highway not in self.NYC.Highway_Dict:
                Highway_new=highway(Highway)
            else:
                Highway_new=self.NYC.Highway_Dict[Highway]
            Marker=list(collisions_HighTunBri.ix[collisions_HighTunBri['RoadwayName']==Highway]['RoadwayReferenceMarker'])
            Highway_new.addCollisions(y, m, collisions_HighTunBri.ix[collisions_HighTunBri['RoadwayName']==Highway], 
                                     factors_HighTunBri.ix[list(map(lambda x: x in Marker,factors_HighTunBri['RoadwayReferenceMarker']))])
            self.NYC.add_highway(Highway_new)
    def building_tunnel(self,y,m,area,collisions_intersection, factors_intersection,collisions_HighTunBri, factors_HighTunBri):
        '''
        Separate the collisions and factors by borough and precinct, store the data in NYC
        All changes will be stored in the global variables 
        Args: NONE
        Returns: NONE
        Raises:  NONE
        '''
        for Tunnel in collisions_HighTunBri.ix[collisions_HighTunBri['RoadwayTypeCode']=='T']['RoadwayName'].unique():
            if Tunnel not in self.NYC.Tunnel_Dict:
                Tunnel_new=tunnel(Tunnel)
            else:
                Tunnel_new=self.NYC.Tunnel_Dict[Tunnel]
            Marker=list(collisions_HighTunBri.ix[collisions_HighTunBri['RoadwayName']==Tunnel]['RoadwayReferenceMarker'])
            Tunnel_new.addCollisions(y, m, collisions_HighTunBri.ix[collisions_HighTunBri['RoadwayName']==Tunnel], 
                                     factors_HighTunBri.ix[list(map(lambda x: x in Marker,factors_HighTunBri['RoadwayReferenceMarker']))])
            self.NYC.add_tunnel(Tunnel_new)
    def building_bridge(self,y,m,area,collisions_intersection, factors_intersection,collisions_HighTunBri, factors_HighTunBri):
        '''
        Separate the collisions and factors by borough and precinct, store the data in NYC
        All changes will be stored in the global variables 
        Args: NONE
        Returns: NONE
        Raises:  NONE
        '''
        for Bridge in collisions_HighTunBri.ix[collisions_HighTunBri['RoadwayTypeCode']=='B']['RoadwayName'].unique():
            if Bridge not in self.NYC.Bridge_Dict:
                Bridge_new=bridge(Bridge)
            else:
                Bridge_new=self.NYC.Bridge_Dict[Bridge]
            Marker=list(collisions_HighTunBri.ix[collisions_HighTunBri['RoadwayName']==Bridge]['RoadwayReferenceMarker'])
            Bridge_new.addCollisions(y, m, collisions_HighTunBri.ix[collisions_HighTunBri['RoadwayName']==Bridge], 
                                     factors_HighTunBri.ix[list(map(lambda x: x in Marker,factors_HighTunBri['RoadwayReferenceMarker']))]) 
            self.NYC.add_bridge(Bridge_new)

def load_intersection(path,y,m,area):
    '''
    Intersection related Data Loading
    Args:
       path: data path where the excel documents are stored in.
       y: year string, format 'YYYY'
       m: month string, format 'MM'
       area: area short name in the name of excel documents , available set { 'bk','bx','mn','qn','si' }
    Returns:
       collisions_intersection: data frame  
       factors_intersection: data frame
    Raises: 
       FileNotFoundError
    '''
    #file name set
    if (y=='2015') & (int(m)<6):
        file='acc.xls'
        sheet_n1='IntersectCollisions-1'
        sheet_n2='IntersectVehiclesContrFactors-2'
    else:
        file='acc-en-us.xlsx'
        sheet_n1='IntersectCollisions_1'
        sheet_n2='IntersectVehiclesContrFactors'
    #file reading
    collisions_intersection = pd.read_excel(''.join([path,y,'_',m,'_col_excel/',area,file]),sheetname=sheet_n1, header=2, skiprows=1)
    factors_intersection = pd.read_excel(''.join([path,y,'_',m,'_col_excel/',area,file]),sheetname=sheet_n2, header=2, skiprows=1)
    #data cleaning
    collisions_intersection = collisions_intersection[collisions_intersection.CollisionID.notnull()]
    factors_intersection = factors_intersection[factors_intersection.ColllisionKey.notnull()]
    #add OccurrencePrecinctCode to Factor information
    factors_intersection = factors_intersection.rename(columns={'ColllisionKey':'CollisionKey'})
    factors_intersection = pd.merge(factors_intersection,collisions_intersection[['OccurrencePrecinctCode','CollisionKey']], how='left', on='CollisionKey')
    
    return collisions_intersection,factors_intersection
    
def load_HighTunBri(path,y,m,area):
    '''
    HiggwayTunnelBridge related Data Loading
    Args:
       path: data path where the excel documents are stored in.
       y: year string, format 'YYYY'
       m: month string, format 'MM'
       area: area short name in the name of excel documents , available set { 'bk','bx','mn','qn','si' }
    Returns:
       collisions_intersection: data frame  
       factors_intersection: data frame
    Raises: 
       FileNotFoundError
    '''
    #file name set
    if (y=='2015') & (int(m)<6):
        file='hacc.xls'
        sheet_n1='RoadwayCollisions-1'
        sheet_n2='RoadwayVehiclesContrFactors-2'
    else:
        file='hacc-en-us.xlsx'
        sheet_n1='RoadwayCollisions_1'
        sheet_n2='RoadwayVehiclesContrFactors_2'
    #file reading
    collisions_HighTunBri = pd.read_excel(''.join([path,y,'_',m,'_col_excel/',area,file]),sheetname=sheet_n1, header=3, skiprows=1)
    factors_HighTunBri = pd.read_excel(''.join([path,y,'_',m,'_col_excel/',area,file]),sheetname=sheet_n2, header=3, skiprows=1)
    #data cleaning
    collisions_HighTunBri = collisions_HighTunBri[collisions_HighTunBri.CollisionID.notnull()]
    factors_HighTunBri = factors_HighTunBri[factors_HighTunBri.ColllisionKey.notnull()]
    #add OccurrencePrecinctCode to Factor information
    factors_HighTunBri = factors_HighTunBri.rename(columns={'ColllisionKey':'CollisionKey'})
    factors_HighTunBri = pd.merge(factors_HighTunBri,collisions_HighTunBri[['OccurrencePrecinctCode','CollisionKey']], how='left', on='CollisionKey')
    
    return collisions_HighTunBri, factors_HighTunBri
            

