'''
Created on Dec 4, 2016

@author: apple
'''
import unittest
import os
from WN_struct_building.data_loading import load_data
from CheckandError.DefinedError import ExitALLProgram
from WN_struct_building.data_loading import load_data,load_HighTunBri,load_intersection,LoadingbyStructure

class Test(unittest.TestCase):
    def setUp(self):
        DataPath=os.getcwd()
        self.DataPath=''.join([DataPath,'/NYPD_DATA/'])
        self.Loading=LoadingbyStructure()
        self.collisions_HighTunBri, self.factors_HighTunBri=load_HighTunBri(self.DataPath, '2015', '01', 'bk')
        self.collisions_Intersection, self.factors_Intersection=load_intersection(self.DataPath, '2015', '01', 'bk')
    def test_load_HighTunBri(self):
        with self.assertRaises(FileNotFoundError):
            load_HighTunBri(self.DataPath,'2014','01','bk')
        with self.assertRaises(FileNotFoundError):
            load_HighTunBri(self.DataPath, '2015', '13', 'mn')
        with self.assertRaises(FileNotFoundError):
            load_HighTunBri(self.DataPath, '2015', '12', 'qq')
        with self.assertRaises(FileNotFoundError):
            load_HighTunBri('a/','2015','01','bk') 
        self.assertEqual(len(self.collisions_HighTunBri), 294)   
        self.assertEqual(len(self.collisions_HighTunBri['Bicycle'][1]), 0.0)  
        self.assertEqual(len(self.factors_HighTunBri),615)
        self.assertEqual(len(self.factors_HighTunBri),615)
        self.assertSequenceEqual(list(self.factors_HighTunBri.columns),['RoadwayReferenceMarker', 'CollisionID', 'CollisionKey', 'VehicleSequenceNumber', 'VehicleTypeCode', 'VehicleTypeDescription', 'ContributingFactorCode', 'ContributingFactorDescription', 'OccurrencePrecinctCode'])
    def test_load_Intersection(self):   
        with self.assertRaises(FileNotFoundError):
            load_intersection(self.DataPath,'2014','01','bk')
        with self.assertRaises(FileNotFoundError):
            load_intersection(self.DataPath, '2015', '13', 'mn')
        with self.assertRaises(FileNotFoundError):
            load_intersection(self.DataPath, '2015', '12', 'qq')
        with self.assertRaises(FileNotFoundError):
            load_intersection('a/','2015','01','bk') 
        self.assertEqual(len(self.collisions_intersection),4089)
        self.assertSequenceEqual(list(self.collisions_intersection.columns),['OccurrencePrecinctCode', 'CollisionID', 'CollisionKey', 'Collision_ at_Intersection', 'IntersectionAddress', 'IntersectingStreet', 'CrossStreet', 'CollisionVehicleCount', 'CollisionInjuredCount', 'CollisionKilledCount', 'Vehicles_or_MotoristsInvolved', 'PersonsInjured', 'PersonsKilled', 'MotoristsInjured', 'MotoristsKilled', 'PassengInjured', 'PassengKilled', 'CyclistsInjured', 'CyclistsKilled', 'PedestrInjured', 'PedestrKilled', 'Injury_or_Fatal', 'Bicycle'])
        self.assertEqual(len(self.factors_intersection),8124)
        self.assertSequenceEqual(list(self.collisions_HighTunBri.columns),['OccurrencePrecinctCode', 'CollisionID', 'CollisionKey', 'RoadwayTypeCode', 'RoadwayReferenceMarker', 'Collision_ at_Location', 'RoadwayName', 'RoadwayDirection', 'RoadwayLocationDescription', 'CollisionVehicleCount', 'CollisionInjuredCount', 'CollisionKilledCount', 'Vehicles_or_MotoristsInvolved', 'PersonsInjured', 'PersonsKilled', 'MotoristsInjured', 'MotoristsKilled', 'PassengInjured', 'PassengKilled', 'CyclistsInjured', 'CyclistsKilled', 'PedestrInjured', 'PedestrKilled', 'Injury_or_Fatal', 'Bicycle'])
    def test_building_borough(self):
        self.Loading.building_borough('2015', '01', 'bk', self.collisions_intersection, self.factors_intersection, self.collisions_HighTunBri, self.factors_HighTunBri)
        self.NYC.init_borough()
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()