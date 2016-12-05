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

def load_data(path):
    '''
    Args:
        path: data path  
    Returns:
        NYC : a well prepared city class
    Raises:  
        FileNotFoundError (handling inside)    
    '''
    def building_borough():     
        '''
        Separate the collisions and factors by borough and precinct, store the data in NYC
        All changes will be stored in the global variables 
        Args: NONE
        Returns: NONE
        Raises:  NONE
        '''
        for precinctID in collisions_intersection['OccurrencePrecinctCode'].unique():
            if precinctID not in NYC.Borough_Dict[area].precinctList:
                precinct_new=precinct(precinctID)
            else:
                precinct_new=NYC.Borough_Dict[area].precinctList[precinctID]
            precinct_new.addCollisions_Intersection(y, m, collisions_intersection.ix[collisions_intersection['OccurrencePrecinctCode']==precinctID],
                                       factors_intersection.ix[factors_intersection['OccurrencePrecinctCode']==precinctID])
            NYC.Borough_Dict[area].precinctList[precinctID]=precinct_new
        for precinctID in collisions_HighTunBri['OccurrencePrecinctCode'].unique():
            if precinctID not in NYC.Borough_Dict[area].precinctList:
                precinct_new=precinct(precinctID)
            else:
                precinct_new=NYC.Borough_Dict[area].precinctList[precinctID]
            precinct_new.addCollisions_HighTunBri(y, m, 
                                       collisions_HighTunBri.ix[collisions_HighTunBri['OccurrencePrecinctCode']==precinctID],
                                       factors_HighTunBri.ix[factors_HighTunBri['OccurrencePrecinctCode']==precinctID])
            NYC.Borough_Dict[area].addprecinct(precinct_new)
                
    def building_road():
        '''
        Separate the collisions and factors by borough and precinct, store the data in NYC
        All changes will be stored in the global variables 
        Args: NONE
        Returns: NONE
        Raises:  NONE
        '''
        all_street=set(collisions_intersection['IntersectingStreet'].unique())|set(collisions_intersection['CrossStreet'].unique())
        for Road in all_street:
            if Road not in NYC.Road_Dict:
                Road_new=road(Road)
            else:
                Road_new=NYC.Road_Dict[Road]
            Marker=list(collisions_intersection.ix[list(collisions_intersection['IntersectingStreet']==Road) or list(collisions_intersection['CrossStreet']==Road)]['CollisionKey'])
            Road_new.addCollisions(y, m, collisions_intersection.ix[list(collisions_intersection['IntersectingStreet']==Road) or list(collisions_intersection['CrossStreet']==Road)],
                                       factors_intersection.ix[list(map(lambda x: x in Marker,factors_intersection['CollisionKey']))])
            NYC.add_road(Road_new)
#         for Road in collisions_intersection['IntersectingStreet'].unique():
#             if Road not in NYC.Road_Dict:
#                 Road_new=road(Road)
#             else:
#                 Road_new=NYC.Road_Dict[Road]
#             Marker=list(collisions_intersection.ix[collisions_intersection['IntersectingStreet']==Road]['CollisionKey'])
#             Road_new.addCollisions(y, m, collisions_intersection.ix[collisions_intersection['IntersectingStreet']==Road],
#                                        factors_intersection.ix[list(map(lambda x: x in Marker,factors_intersection['CollisionKey']))])
#             NYC.add_road(Road_new)
#         for Road in collisions_intersection['CrossStreet'].unique():
#             if Road not in NYC.Road_Dict:
#                 Road_new=road(Road)
#             else:
#                 Road_new=NYC.Road_Dict[Road]
#             Marker=list(collisions_intersection.ix[collisions_intersection['CrossStreet']==Road]['CollisionKey'])
#             Road_new.addCollisions(y, m, collisions_intersection.ix[collisions_intersection['CrossStreet']==Road],
#                                        factors_intersection.ix[list(map(lambda x: x in Marker,factors_intersection['CollisionKey']))])
#             NYC.add_road(Road_new)
               
        
    def building_highway():
        '''
        Separate the collisions and factors by borough and precinct, store the data in NYC
        All changes will be stored in the global variables 
        Args: NONE
        Returns: NONE
        Raises:  NONE
        '''
        for Highway in collisions_HighTunBri.ix[collisions_HighTunBri['RoadwayTypeCode']=='H']['RoadwayName'].unique():
            if Highway not in NYC.Highway_Dict:
                Highway_new=highway(Highway)
            else:
                Highway_new=NYC.Highway_Dict[Highway]
            Marker=list(collisions_HighTunBri.ix[collisions_HighTunBri['RoadwayName']==Highway]['RoadwayReferenceMarker'])
            Highway_new.addCollisions(y, m, collisions_HighTunBri.ix[collisions_HighTunBri['RoadwayName']==Highway], 
                                     factors_HighTunBri.ix[list(map(lambda x: x in Marker,factors_HighTunBri['RoadwayReferenceMarker']))])
            NYC.add_highway(Highway_new)
    def building_tunnel():
        '''
        Separate the collisions and factors by borough and precinct, store the data in NYC
        All changes will be stored in the global variables 
        Args: NONE
        Returns: NONE
        Raises:  NONE
        '''
        for Tunnel in collisions_HighTunBri.ix[collisions_HighTunBri['RoadwayTypeCode']=='T']['RoadwayName'].unique():
            if Tunnel not in NYC.Tunnel_Dict:
                Tunnel_new=tunnel(Tunnel)
            else:
                Tunnel_new=NYC.Tunnel_Dict[Tunnel]
            Marker=list(collisions_HighTunBri.ix[collisions_HighTunBri['RoadwayName']==Tunnel]['RoadwayReferenceMarker'])
            Tunnel_new.addCollisions(y, m, collisions_HighTunBri.ix[collisions_HighTunBri['RoadwayName']==Tunnel], 
                                     factors_HighTunBri.ix[list(map(lambda x: x in Marker,factors_HighTunBri['RoadwayReferenceMarker']))])
            NYC.add_tunnel(Tunnel_new)
    def building_bridge():
        '''
        Separate the collisions and factors by borough and precinct, store the data in NYC
        All changes will be stored in the global variables 
        Args: NONE
        Returns: NONE
        Raises:  NONE
        '''
        for Bridge in collisions_HighTunBri.ix[collisions_HighTunBri['RoadwayTypeCode']=='B']['RoadwayName'].unique():
            if Bridge not in NYC.Bridge_Dict:
                Bridge_new=bridge(Bridge)
            else:
                Bridge_new=NYC.Bridge_Dict[Bridge]
            Marker=list(collisions_HighTunBri.ix[collisions_HighTunBri['RoadwayName']==Bridge]['RoadwayReferenceMarker'])
            Bridge_new.addCollisions(y, m, collisions_HighTunBri.ix[collisions_HighTunBri['RoadwayName']==Bridge], 
                                     factors_HighTunBri.ix[list(map(lambda x: x in Marker,factors_HighTunBri['RoadwayReferenceMarker']))]) 
            NYC.add_bridge(Bridge_new)
    
            
    def load_intersection(path,y,m,area):
        if (y=='2015') & (int(m)<6):
            file='acc.xls'
            sheet_n1='IntersectCollisions-1'
            sheet_n2='IntersectVehiclesContrFactors-2'
        else:
            file='acc-en-us.xlsx'
            sheet_n1='IntersectCollisions_1'
            sheet_n2='IntersectVehiclesContrFactors'
        collisions_intersection = pd.read_excel(''.join([path,'NYPD/',y,'_',m,'_col_excel/',area,file]),sheetname=sheet_n1, header=2, skiprows=1)
        collisions_intersection = pd.DataFrame(collisions_intersection)
        factors_intersection = pd.read_excel(''.join([path,'NYPD/',y,'_',m,'_col_excel/',area,file]),sheetname=sheet_n2, header=2, skiprows=1)
        factors_intersection  = pd.DataFrame(factors_intersection)
        collisions_intersection = collisions_intersection[collisions_intersection.CollisionID.notnull()]
        factors_intersection = factors_intersection[factors_intersection.ColllisionKey.notnull()]
        factors_intersection = factors_intersection.rename(columns={'ColllisionKey':'CollisionKey'})
        factors_intersection = pd.merge(factors_intersection,collisions_intersection[['OccurrencePrecinctCode','CollisionKey']], how='left', on='CollisionKey')
        return collisions_intersection,factors_intersection
    
    def load_HighTunBri(path,y,m,area):
        if (y=='2015') & (int(m)<6):
            file='hacc.xls'
            sheet_n1='RoadwayCollisions-1'
            sheet_n2='RoadwayVehiclesContrFactors-2'
        else:
            file='hacc-en-us.xlsx'
            sheet_n1='RoadwayCollisions_1'
            sheet_n2='RoadwayVehiclesContrFactors_2'
        collisions_HighTunBri = pd.read_excel(''.join([path,'NYPD/',y,'_',m,'_col_excel/',area,file]),sheetname=sheet_n1, header=3, skiprows=1)
        collisions_HighTunBri = pd.DataFrame(collisions_HighTunBri)
        factors_HighTunBri = pd.read_excel(''.join([path,'NYPD/',y,'_',m,'_col_excel/',area,file]),sheetname=sheet_n2, header=3, skiprows=1)
        factors_HighTunBri = pd.DataFrame(factors_HighTunBri)
        collisions_HighTunBri = collisions_HighTunBri[collisions_HighTunBri.CollisionID.notnull()]
        factors_HighTunBri = factors_HighTunBri[factors_HighTunBri.ColllisionKey.notnull()]
        factors_HighTunBri = factors_HighTunBri.rename(columns={'ColllisionKey':'CollisionKey'})
        factors_HighTunBri = pd.merge(factors_HighTunBri,collisions_HighTunBri[['OccurrencePrecinctCode','CollisionKey']], how='left', on='CollisionKey')
        
        return collisions_HighTunBri, factors_HighTunBri
    
    NYC=city()
    NYC.init_borough()
    #load NYPD data
    #year=['2015','2016']
    year=['2015']
    #month=['01','02','03','04','05','06','07','08','09','10','11','12']
    month=['01']
    area_name=['bk','bx','mn','qn','si']
    #intersection
    for y in year:
        for m in month:
            for area in area_name:
                try:
                    collisions_intersection, factors_intersection = load_intersection(path, y, m, area)
                    collisions_HighTunBri, factors_HighTunBri = load_HighTunBri(path, y, m, area)
                    building_borough()   
                    building_road() 
                    building_highway()
                    building_bridge()
                    building_tunnel()
                except FileNotFoundError:
                    print('There is no file about above area and period')
                    print(y+m+area)
                    
                    
    return NYC

