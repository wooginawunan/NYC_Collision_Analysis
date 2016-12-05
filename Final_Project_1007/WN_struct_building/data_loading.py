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

class load_data():
    def __init__(self,path):
        self.path
        self.NYC=city()
        self.NYC.init_borough()
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
                        self.collisions_intersection, self.factors_intersection = self.load_intersection( y, m, area)
                        self.collisions_HighTunBri, self.factors_HighTunBri = self.load_HighTunBri( y, m, area)
                        self.building_borough(y,m,area)   
                        self.building_road(y,m,area) 
                        self.building_highway(y,m,area)
                        self.building_bridge(y,m,area)
                        self.building_tunnel(y,m,area)
                    except FileNotFoundError:
                        print(y+m+area)  
    def load_intersection(self,y,m,area):
        path=self.path
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
    
    def load_HighTunBri(self,y,m,area):
        path=self.path
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
    def building_borough(self,y,m,area):     
        '''
        Separate the collisions and factors by borough and precinct, store the data in NYC
        All changes will be stored in the global variables 
        Args: NONE
        Returns: NONE
        Raises:  NONE
        '''
        collisions_intersection=self.collisions_intersection
        collisions_HighTunBri=self.collisions_HighTunBri
        factors_intersection=self.factors_intersection
        factors_HighTunBri=self.factors_HighTunBri
        NYC=self.NYC
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
                