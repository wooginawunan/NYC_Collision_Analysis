'''
Created on Nov 14, 2016

@author: apple
'''
information={'city':NYC.Borough_Dict[area],'Year':y, 'Month': m,'Intersection': {'collisions': collisions_intersection,'factors':factors_intersection},'HighTunBri':{'collisions': collisions_HighTunBri,'factors':factors_HighTunBri}}
                NYC.Borough_Dict[area] = building_borough(information)   
def load_data(path):
    def building_borough(information):
            collisions_intersection=information['Intersection']['collisions']
            collisions_HighTunBri=information['HighTunBri']['collisions']
            factors_intersection=information['Intersection']['factors']
            factors_HighTunBri=information['HighTunBri']['factors']
            
            for precinctID in collisions_intersection['OccurrencePrecinctCode'].unique():
                if precinctID not in information['borough'].precinctList:
                    precinct_new=precinct(precinctID)
                else:
                    precinct_new=information['borough'][precinctID]
                precinct_new.addCollisions(information['Year'], information['Month'], 
                                           collisions_intersection.ix[collisions_intersection['OccurrencePrecinctCode']==precinctID],
                                           factors_intersection.ix[factors_intersection['OccurrencePrecinctCode']==precinctID])
                information['borough'].precinctList[precinctID]=precinct_new
            for precinctID in collisions_HighTunBri['OccurrencePrecinctCode'].unique():
                if precinctID not in information['borough'].precinctList:
                    precinct_new=precinct(precinctID)
                else:
                    precinct_new=information['borough'][precinctID]
                precinct_new.addCollisions(information['Year'], information['Month'], 
                                           collisions_HighTunBri.ix[collisions_HighTunBri['OccurrencePrecinctCode']==precinctID],
                                           factors_HighTunBri.ix[factors_HighTunBri['OccurrencePrecinctCode']==precinctID])
                information['borough'].precinctList[precinctID]=precinct_new
            return 
                
import numpy as np
import pandas as pd
from WN_struct_building.CityStructure import city
from WN_struct_building.building_CityCollisions import *

def load_intersection(path,y,m,area):
    if y=='2015' & int(m)<7:
        file='acc.xls'
        sheet_n1='IntersectCollisions-1'
        sheet_n2='IntersectVehiclesContrFactors-2'
    else:
        file='acc-en-us.xlsx'
        sheet_n1='IntersectCollisions_1'
        sheet_n2='IntersectVehiclesContrFactors'
    collisions_intersection = pd.read_excel(''.join([path,'NYPD/',y,'_',m,'_col_excel/',area,file]),sheetname=sheet_n1, header=3, skiprows=3)
    collisions_intersection = pd.DataFrame(collisions_intersection)
    factors_intersection = pd.read_excel(''.join([path,'NYPD/',y,'_',m,'_col_excel/',area,file]),sheetname=sheet_n2, header=3, skiprows=3)
    factors_intersection  = pd.DataFrame(factors_intersection)
    collisions_intersection = collisions_intersection[collisions_intersection.CollisionID.notnull()]
    factors_intersection = factors_intersection[factors_intersection.ColllisionKey.notnull()]
    factors_intersection.rename(columns={'ColllisionKey':'CollisionKey'})
    factors_intersection=pd.merge(factors_intersection,collisions_intersection[['OccurrencePrecinctCode','CollisionKey']], how='left', on='CollisionKey')
    return collisions_intersection,factors_intersection

def load_HighTunBri(path,y,m,area):
    if y=='2015' & int(m)<7:
        file='hacc.xls'
        sheet_n1='IntersectCollisions-1'
        sheet_n2='IntersectVehiclesContrFactors-2'
    else:
        file='hacc-en-us.xlsx'
        sheet_n1='IntersectCollisions_1'
        sheet_n2='IntersectVehiclesContrFactors'
    collisions_HighTunBri = pd.read_excel(''.join([path,'NYPD/',y,'_',m,'_col_excel/',area,file]),sheetname=sheet_n1, header=3, skiprows=3)
    collisions_HighTunBri = pd.DataFrame(collisions_HighTunBri)
    factors_HighTunBri = pd.read_excel(''.join([path,'NYPD/',y,'_',m,'_col_excel/',area,file]),sheetname=sheet_n2, header=3, skiprows=3)
    factors_HighTunBri  = pd.DataFrame(factors_HighTunBri)
    collisions_HighTunBri = collisions_HighTunBri[collisions_HighTunBri.CollisionID.notnull()]
    factors_HighTunBri = factors_HighTunBri[factors_HighTunBri.ColllisionKey.notnull()]
    factors_HighTunBri.rename(columns={'ColllisionKey':'CollisionKey'})
    factors_HighTunBri=pd.merge(factors_HighTunBri,collisions_HighTunBri[['OccurrencePrecinctCode','CollisionKey']], how='left', on='CollisionKey')
    
    return collisions_HighTunBri, factors_HighTunBri

def load_data(path):
    #load NYPD data
    year=['2015','2016']
    month=['01','02','03','04','05','06','07','08','09','10','11','12']
    area_name=['bk','bx','mn','qn','si']
    #intersection
    for y in year:
        for m in month:
            for area in area_name:
                collisions_intersection, factors_intersection = load_intersection(path, y, m, area)
                collisions_HighTunBri, factors_HighTunBri = load_HighTunBri(path, y, m, area)
                information={'city':NYC.Borough_Dict[area],'Year':y, 'Month': m,'Intersection': {'collisions': collisions_intersection,'factors':factors_intersection},'HighTunBri':{'collisions': collisions_HighTunBri,'factors':factors_HighTunBri}}
                NYC.Borough_Dict[area] = building_borough(information)
NYC=city()
NYC.init_borough()
                
if __name__ == "__main__":
    try:
        data_path='/Users/apple/Desktop/Projects/dataset_NYPD/'
        load_data(data_path)
    except EOFError:
        pass

    