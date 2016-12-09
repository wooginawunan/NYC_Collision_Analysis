'''
Created on Dec 4, 2016

@author: apple
'''
import unittest
import os
from WN_struct_building.data_loading import *
from CheckandError.DefinedError import ExitALLProgram
import numpy as np
from WN_struct_building.CityStructure import *
from sklearn.metrics.pairwise import manhattan_distances
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
    
    def test_DescriptionCleaning(self):
        collisions,factors = FILEload(self.DataPath,'2015','01','mn','hacc.xls','RoadwayCollisions-1','RoadwayVehiclesContrFactors-2',3,1)
        collision, factor = DescriptionCleaning(self.collisions_Intersection, factors)
        self.assertEqual(sum(collision.CollisionID.isnull()),0)
        self.assertEqual(sum(factor.CollisionID.isnull()),0)
    def test_ADDprecinctCode(self):
        collisions,factors = FILEload(self.DataPath,'2015','01','mn','hacc.xls','RoadwayCollisions-1','RoadwayVehiclesContrFactors-2',3,1)
        collisions,factors = DescriptionCleaning(collisions,factors)
        factors = RenameColumn(factors)
        ADDprecinctCode(factors,collisions).OccurrencePrecinctCode
    def test_UPPERCase(self):
        
        collisions,factors = FILEload(self.DataPath,'2015','01','mn','hacc.xls','RoadwayCollisions-1','RoadwayVehiclesContrFactors-2',3,1)
        collisions,factors = DescriptionCleaning(collisions,factors)
        factors = RenameColumn(factors)
        factors = Handling_xa0(factors)
        factors = UPPERCase(factors)
        index = np.random.randint(len(factors),size=20)
        [self.assertTrue(factors['VehicleTypeDescription'][i].isupper()) for i in index]
        [self.assertTrue(factors['ContributingFactorDescription'][i].isupper()) for i in index]
    
    def test_Handling_xa0(self):
       
        collisions,factors = FILEload(self.DataPath,'2015','01','mn','hacc.xls','RoadwayCollisions-1','RoadwayVehiclesContrFactors-2',3,1)
        collisions,factors = DescriptionCleaning(collisions,factors)
        factors = RenameColumn(factors)
        factors = Handling_xa0(factors)
        index = np.random.randint(len(factors),size=20)
        [self.assertNotIn('\xa0',factors['ContributingFactorDescription'][i]) for i in index]
    
    def test_RenameColumn(self):
        with self.assertRaises(AttributeError):
            RenameColumn(self.factors_Intersection).ColllisionKey
          

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
    
       
class StructureBuildingTest(unittest.TestCase):
    def setUp(self):
        self.dirname, self.filename = os.path.split(os.path.abspath(__file__))
        self.DataPath=''.join([self.dirname[:-18],'/NYPD_DATA/'])
        self.NYC=load_data(self.DataPath,[2015,1],[2015,1])
    def test_City(self):
        self.assertSequenceEqual(self.NYC.Borough_Dict.keys(),dict.fromkeys(['bk', 'bx','mn','qn','si']).keys())
        self.assertIsInstance(self.NYC, city)
        self.assertGreater(len(self.NYC.Road_Dict), 0)
        self.assertGreater(len(self.NYC.Highway_Dict), 0)
        self.assertGreater(len(self.NYC.Bridge_Dict), 0)
        self.assertGreater(len(self.NYC.Tunnel_Dict), 0)
        print(sorted(self.NYC.Highway_Dict.keys()))
        print(sorted(self.NYC.Tunnel_Dict.keys()))
        print(sorted(self.NYC.Bridge_Dict.keys()))
        print(self.NYC.roadCatalog())
    def test_Borough(self):
        for Bo in self.NYC.Borough_Dict.values():
            self.assertIsInstance(Bo, borough)
            print(sorted(Bo.precinctList.keys()))
    def test_Precinct(self):
        manhatta=self.NYC.Borough_Dict['mn']
        for pre in manhatta.precinctList.values():
            self.assertIsInstance(pre, precinct)
            for m in [str(x).zfill(2) for x in range(1,13)]:
                with self.assertRaises(KeyError):
                    pre.Collisions_HighTunBri['2016'][m]
            for m in [str(x).zfill(2) for x in range(2,13)]:
                with self.assertRaises(KeyError):
                    pre.Collisions_HighTunBri['2015'][m]
            for m in [str(x).zfill(2) for x in range(1,13)]:
                with self.assertRaises(KeyError):
                    pre.Collisions_intersection['2016'][m]
            for m in [str(x).zfill(2) for x in range(2,13)]:
                with self.assertRaises(KeyError):
                    pre.Collisions_intersection['2015'][m]
    def test_BTHR(self):
        for btrh in self.NYC.Road_Dict.values():
            self.assertIsInstance(btrh, road)
            for m in [str(x).zfill(2) for x in range(1,13)]:
                with self.assertRaises(KeyError):
                    btrh.Factors['2016'][m]
            for m in [str(x).zfill(2) for x in range(2,13)]:
                with self.assertRaises(KeyError):
                    btrh.Factors['2015'][m]
            for m in [str(x).zfill(2) for x in range(1,13)]:
                with self.assertRaises(KeyError):
                    btrh.Collisions['2016'][m]
            for m in [str(x).zfill(2) for x in range(2,13)]:
                with self.assertRaises(KeyError):
                    btrh.Collisions['2015'][m]

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()