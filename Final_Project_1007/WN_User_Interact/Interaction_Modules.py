#!/usr/local/bin/python2.7
# encoding: utf-8
'''
WN_User_Interact.Interaction_Modules -- shortdesc

WN_User_Interact.Interaction_Modules is a description

It defines classes_and_methods

@author:     user_name

@copyright:  2016 organization_name. All rights reserved.

@license:    license

@contact:    user_email
@deffield    updated: Updated
''' 

from WN_User_Interact.InputANDError import InputCheck
from WN_User_Interact.CollisionSituation import CollisionSituation
from WN_struct_building import StructureBuilding
def ProgramIntroduction():
    print('Welcome to NYC Motor Vehicle Collisions Observation System.')
    print('We provide an analysis of the historical trends and features of auto collision \n and other associated demographic and geographic information in NYC. \n There is also an interactive maps which may help you better observe \n the whole traffic collision situation in NYC.')
    print('DATA SOURCE:')
    print('DATA INTRODUCTION:')
    print("COPY RIGHT:")
    print("FUNCTIONS")
    print('EXIT WAY')
    print('HELP MENUAL')
    print("We have several perspectives for your to explore.They are in two categories:")
    print("Area: City; Borough; Precinct")
    print("Type of Roadways: Highway; Tunnel; Bridge; Road")
    print("There are available methods under the specific perspective.")
    print("Input Examples: ")
    print("...")
    print("Now you can begin with it.")
def Mainmenu():
    NYC = StructureBuilding()
    print(NYC.Borough_Dict)
    print("There are three types of information: \n 1-CollisionSituation \n 2-CollisionContributingFactors_Vehicle \n 3-CollisionSimulation")
    InformationType = input("You can choose one by input the number before the type above.")
    MenuInformation={-2:Mainmenu, 
                     -1:Mainmenu,
                     1:CollisionSituation,
                     2:CollisionContributingFactors_Vehicle,
                     3:CollisionSimulation}
    inputset=MenuInformation.keys()
    InformationType = InputCheck(inputset, InformationType)
    MenuInformation[InformationType](NYC) if InformationType>0 else MenuInformation[InformationType]()
    
def CollisionContributingFactors_Vehicle(NYC):
    pass
def CollisionSimulation(NYC):
    pass

    
    
    
    
    
    
    
    



