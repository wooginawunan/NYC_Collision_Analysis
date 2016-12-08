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

import sys
import os
from inspect import getsourcefile
from os.path import abspath
from WN_struct_building.data_loading import load_data
from CheckandError.DefinedError import ExitALLProgram
def StructureBuilding(TimeBegin,TimeEnd,path):
    try:
        print('Loading data and initiating the system...... ')
        #DataPath=os.getcwd()
        #print(DataPath)
        
        DataPath=''.join([path,'/NYPD_DATA/'])
        while True:
            try:
                NYC = load_data(DataPath,TimeBegin,TimeEnd)
                return NYC
            except FileNotFoundError:
                print("FILE NOT FOUND! or FILE INCOMPLETED!")
                DataPath=input("Please Reset the data path to (Example: .../NYPD_DATA/):")
                if DataPath=='Exit':
                    raise ExitALLProgram               
    except EOFError:
        pass
#StructureBuilding([2015,1],[2015,1])
    