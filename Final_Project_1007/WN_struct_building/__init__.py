'''
This package builds the fundamental data structure for the whole project.
Loading data from documents about monthly NYPD Motor Vehicle Collisions in whole NYC.
Building Classes for each precinct.
Building Classes for Information of Collisions happened in different intersections, highways, tunnels and bridges   
Version 1
Copyright:
@ Nan Wu 
@ nw1045@nyu.edu
@ wooginawunan@gmail.com
'''
#def loadingANDbuilding():
from WN_struct_building.building_CityCollisions import load_data
def StructureBuilding():
    try:
        print('Loading data and initiating the system...... ')
        data_path='/Users/apple/Desktop/Projects/dataset_NYPD/'
        NYC = load_data(data_path)
        return NYC
        
    except EOFError:
        
        pass

    