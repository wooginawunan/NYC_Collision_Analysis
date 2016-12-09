'''
Created on Dec 4, 2016

@author: apple
'''
import unittest
import os
from WN_struct_building.data_loading import *
from CheckandError.DefinedError import ExitALLProgram

class LoadingDataTest(unittest.TestCase):
    def setUp(self):
        self.dirname, self.filename = os.path.split(os.path.abspath(__file__))
        self.DataPath=''.join([self.dirname[:-18],'/NYPD_DATA/'])
        self.Loading=LoadingbyStructure()
        self.collisions_HighTunBri, self.factors_HighTunBri=load_HighTunBri(self.DataPath, '2015', '01', 'bk')
        self.collisions_Intersection, self.factors_Intersection=load_intersection(self.DataPath, '2015', '01', 'bk')
    def test_FileNameSet(self):
        self.assertEqual(FileNameSet('2015', '01', 1),('hacc.xls','RoadwayCollisions-1','RoadwayVehiclesContrFactors-2' )) 
        self.assertEqual(FileNameSet('2016', '01', 1),('hacc-en-us.xlsx' , 'RoadwayCollisions_1', 'RoadwayVehiclesContrFactors_2'))
        self.assertEqual(FileNameSet('2015', '09', 1),('hacc-en-us.xlsx' , 'RoadwayCollisions_1', 'RoadwayVehiclesContrFactors_2'))
        self.assertEqual(FileNameSet('2015', '01', 0),('acc.xls','IntersectCollisions-1','IntersectVehiclesContrFactors-2')) 
        self.assertEqual(FileNameSet('2016', '01', 0),('acc-en-us.xlsx' , 'IntersectCollisions_1', 'IntersectVehiclesContrFactors'))
        self.assertEqual(FileNameSet('2015', '09', 0),('acc-en-us.xlsx' , 'IntersectCollisions_1', 'IntersectVehiclesContrFactors'))
    def test_FILEload(self):
        FILEload(self.DataPath,'2015','01','mn','hacc.xls','RoadwayCollisions-1','RoadwayVehiclesContrFactors-2',3,1)
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
        self.assertEqual(self.collisions_HighTunBri['Bicycle'][1], 0.0)  
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
        self.assertEqual(len(self.collisions_Intersection),4089)
        self.assertSequenceEqual(list(self.collisions_Intersection.columns),['OccurrencePrecinctCode', 'CollisionID', 'CollisionKey', 'Collision_ at_Intersection', 'IntersectionAddress', 'IntersectingStreet', 'CrossStreet', 'CollisionVehicleCount', 'CollisionInjuredCount', 'CollisionKilledCount', 'Vehicles_or_MotoristsInvolved', 'PersonsInjured', 'PersonsKilled', 'MotoristsInjured', 'MotoristsKilled', 'PassengInjured', 'PassengKilled', 'CyclistsInjured', 'CyclistsKilled', 'PedestrInjured', 'PedestrKilled', 'Injury_or_Fatal', 'Bicycle'])
        self.assertEqual(len(self.factors_Intersection),8124)
        self.assertSequenceEqual(list(self.collisions_HighTunBri.columns),['OccurrencePrecinctCode', 'CollisionID', 'CollisionKey', 'RoadwayTypeCode', 'RoadwayReferenceMarker', 'Collision_ at_Location', 'RoadwayName', 'RoadwayDirection', 'RoadwayLocationDescription', 'CollisionVehicleCount', 'CollisionInjuredCount', 'CollisionKilledCount', 'Vehicles_or_MotoristsInvolved', 'PersonsInjured', 'PersonsKilled', 'MotoristsInjured', 'MotoristsKilled', 'PassengInjured', 'PassengKilled', 'CyclistsInjured', 'CyclistsKilled', 'PedestrInjured', 'PedestrKilled', 'Injury_or_Fatal', 'Bicycle'])


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()