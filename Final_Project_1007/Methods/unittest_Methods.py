'''
Unittest for Methods

Copyright:
@ Nan Wu 
@ nw1045@nyu.edu
@ wooginawunan@gmail.com
'''
import unittest
import os
from WN_struct_building import StructureBuilding
from Methods.MethodClass import *

class SituationMethods_Test(unittest.TestCase):
    

    def setUp(self):
        self.dirname, self.filename = os.path.split(os.path.abspath(__file__))
        self.DataPath=''.join([self.dirname[:-8]])
        print(self.DataPath)
        self.TimeBegin=[2015,5]
        self.TimeEnd = [2015,6]
        self.savepath = ''.join([self.dirname[:-8],'/test_results/'])
        self.NYC = StructureBuilding(self.TimeBegin,self.TimeEnd,self.DataPath)
        self.Situation = SituationMethods(self.NYC, self.savepath, self.TimeBegin,self.TimeEnd)

    def test_CityTable(self):
        values=dict(zip(range(1,15),[18375, 4643.0, 27.0, 4643.0, 27.0,1587.0,5.0,1832.0,4.0,464.0,1.0,760.0,17.0,3450.0]))

        for indicator in self.Situation.Indicator.keys():
            self.assertEqual(list(self.Situation.CityTable(indicator, 'null').ix[0])[0],values[indicator])
        
            
    def test_BoroughTable(self):
        value_1=dict(zip([ 'bk', 'mn', 'bx', 'qn', 'si'],[5294, 4295, 2531, 5219, 1036]))
        value_2=dict(zip([ 'bk', 'mn', 'bx', 'qn', 'si'],[1522.0, 686.0, 757.0, 1411.0, 267.0]))
        value_3=dict(zip([ 'bk', 'mn', 'bx', 'qn', 'si'],[9.0, 7.0, 4.0, 5.0, 2.0]))
        value_4=dict(zip([ 'bk', 'mn', 'bx', 'qn', 'si'],[1522.0, 686.0, 757.0, 1411.0, 267.0]))
        value_5=dict(zip([ 'bk', 'mn', 'bx', 'qn', 'si'],[9.0, 7.0, 4.0, 5.0, 2.0]))
        value_6=dict(zip([ 'bk', 'mn', 'bx', 'qn', 'si'],[462.0, 172.0, 277.0, 557.0, 119.0]))
        value_7=dict(zip([ 'bk', 'mn', 'bx', 'qn', 'si'],[2,0,1,0,2]))
        value_8=dict(zip([ 'bk', 'mn', 'bx', 'qn', 'si'],[607.0, 205.0, 315.0, 595.0, 110.0]))
        value_9=dict(zip([ 'bk', 'mn', 'bx', 'qn', 'si'],[1,1,0,2.0]))
        value_10=dict(zip([ 'bk', 'mn', 'bx', 'qn', 'si'],[177.0, 136.0, 52.0, 92.0, 7.0]))
        value_11=dict(zip([ 'bk', 'mn', 'bx', 'qn', 'si'],[0,1,0,0,0]))
        value_12=dict(zip([ 'bk', 'mn', 'bx', 'qn', 'si'],[276.0, 173.0, 113.0, 167.0, 31.0]))
        value_13=dict(zip([ 'bk', 'mn', 'bx', 'qn', 'si'],[6.0, 5.0, 3.0, 3.0, 0.0]))
        value_14=dict(zip([ 'bk', 'mn', 'bx', 'qn', 'si'],[1120.0, 586.0, 540.0, 1022.0, 182.0]))
        values=dict(zip(range(1,15),[value_1,value_2,value_3,value_4,value_5,value_6,value_7,value_8,value_9,value_10,value_11,value_12,value_13,value_14]))
        for indicator in self.Situation.Indicator.keys():
            for name in [ 'bk', 'mn', 'bx', 'qn', 'si']:
                self.assertEqual(list(self.Situation.BoroughTable(indicator,name).ix[0])[0],values[indicator][name])
        
        values=dict(zip(range(1,15),[2531,757,4,757,4,277,1,315,0,52,0,113,3,540]))
        for indicator in self.Situation.Indicator.keys():
            self.assertEqual(self.Situation.BoroughTable(indicator,'null')['Bronx'][0],values[indicator][name])
                            
    def test_PrecinctTable(self):
        value_1=dict(zip([ '001', '100', '060'],[295, 50, 186]))
        value_2=dict(zip([ '001', '100', '060'],[49.0, 14.0, 35.0]))
        values=dict(zip(range(1,3),[value_1,value_2]))
        for indicator in [1,2]:
            for name in [ '001', '100', '060']:
                self.assertEqual(list(self.Situation.PrecinctTable(indicator,name).ix[0])[0],values[indicator][name])
        
        self.assertSequenceEqual(self.Situation.PrecinctTable(1,'null').shape(),(2,77))
        self.assertSequenceEqual(self.Situation.PrecinctTable(2,'null').shape(),(2,77))
    
    
    def test_PrecinctCalculate(self):
        
        df1 = list(self.NYC.Borough_Dict['mn'].precinctList.values())[0].Collisions_intersection['2015']['05']
        self.assertEqual(self.Situation.PrecinctCalculate(1,df1), 266)
        self.assertEqual(self.Situation.PrecinctCalculate(4,df1), 18)
        
    def test_PrecinctTableUnit(self):
        
        df1=self.Situation.PrecinctTableUnit(self.NYC.Borough_Dict['bk'].precinctList['062'],1)
        df=pd.DataFrame({'201505':235,'201506':216},index=['062'])
        df=df.transpose()
        self.assertTrue(df1.equals(df))

        df2=self.Situation.PrecinctTableUnit(self.NYC.Borough_Dict['qn'].precinctList['101'],6)
        df=pd.DataFrame({'201505':6,'201506':4},index=['101'])
        df=df.transpose()
        self.assertTrue(df2.equals(df))

    def test_BoroughTableUnit(self):
        
        df1=self.Situation.BoroughTableUnit(self.NYC.Borough_Dict['bk'],1)
        df=pd.DataFrame({'201505':5294,'201506':5328},index=['Brooklyn'])
        df=df.transpose()
        self.assertTrue(df1.equals(df))

        df2=self.Situation.BoroughTableUnit(self.NYC.Borough_Dict['qn'],6)
        df=pd.DataFrame({'201505':557,'201506':635},index=['Queens'])
        df=df.transpose()
        self.assertTrue(df2.equals(df))

    def test_CityTableUnit(self):
        values=dict(zip(range(1,15),[18375, 4643.0, 27.0, 4643.0, 27.0,1587.0,5.0,1832.0,4.0,464.0,1.0,760.0,17.0,3450.0]))
        for indicator in self.Situation.Indicator.keys():
            self.assertEqual(list(self.Situation.CityTableUnit(self.NYC,indicator).ix[0])[0],values[indicator])
    
          
    def test_BTHRcalculate(self):
        
        df = self.NYC.Road_Dict['EAST CLARKE PLACE'].Collisions['2015']['06']
        self.assertEqual(self.Situation.BTHRcalculate(10,df),0)
        
    def test_BTHRTableUnit(self):
        
        df1=self.Situation.BTHRTableUnit(self.NYC.Road_Dict['EAST CLARKE PLACE'],1)
        df=pd.DataFrame({'201505':1,'201506':0},index=['EAST CLARKE PLACE'])
        df=df.transpose()
        self.assertTrue(df1.equals(df))
        pass
    
    def test_PrecinctTableAll(self):
        df=self.Situation.PrecinctTableAll(self.NYC.Borough_Dict['mn'].precinctList,1)
        self.assertEqual(df['010']['201505'], 266)
    
    def test_BoroughTableAll(self):
        df=self.Situation.BoroughTableAll(self.NYC.Borough_Dict,1)
        self.assertEqual(df['Manhattan']['201505'], 4295)
        df=self.Situation.BoroughTableAll(self.NYC.Borough_Dict,10)
        self.assertEqual(df['Manhattan']['201505'], 136)
        pass
    def test_BTHRTableAll(self):
        df=self.Situation.BTHRableAll(self.NYC.Bridge_Dict,1)
        self.assertEqual(df['VZ BR UPPER']['201505'], 19)
        df=self.Situation.BTHRTableAll(self.NYC.Tunnel_Dict,13)
        self.assertEqual(df['BBT W TUBE']['201505'], 0)
        pass
    def test_TunnelTable(self):
        df=self.Situation.TunnelTable(1,'null')
        self.assertEqual(df['BBT W TUBE']['201505'], 2)
        df=self.Situation.TunnelTable(13,'null')
        self.assertEqual(df['BBT W TUBE']['201505'], 0)
        
        df=self.Situation.TunnelTable(1,'BBT E TUBE')
        self.assertEqual(df['BBT W TUBE']['201505'], 2)
        df=self.Situation.TunnelTable(13,'BBT E TUBE')
        self.assertEqual(df['BBT W TUBE']['201505'], 0)
        pass
    def test_BridgeTable(self):
        df=self.Situation.BridgeTable(1,'null')
        self.assertEqual(df['VZ BR UPPER']['201505'], 19)
        df=self.Situation.BridgeTable(3,'null')
        self.assertEqual(df['VZ BR UPPER']['201505'], 0)
        df=self.Situation.BridgeTable(1,'QNSBORO BR UPPER')
        self.assertEqual(df['QNSBORO BR UPPER']['201505'], 10)
        df=self.Situation.BridgeTable(3,'QNSBORO BR UPPER')
        self.assertEqual(df['QNSBORO BR UPPER']['201505'], 0)
        pass
    def test_HighwayTable(self):
        
        df=self.Situation.HighwayTable(1,'null')
        self.assertEqual(df['HUTCHINSON RIVER EXP']['201505'], 5)
        df=self.Situation.HighwayTable(5,'null')
        self.assertEqual(df['HUTCHINSON RIVER EXP']['201505'], 0)
        df=self.Situation.HighwayTable(1,'LAURELTON PKY')
        self.assertEqual(df['LAURELTON PKY']['201505'], 15)
        df=self.Situation.HighwayTable(5,'LAURELTON PKY')
        self.assertEqual(df['LAURELTON PKY']['201505'], 0)
    
    def test_RoadTable(self):
        df=self.Situation.RoadTable(1,'null')
        self.assertEqual(df['EAST CLARKE PLACE']['201505'], 1)
        df=self.Situation.RoadTable(8,'null')
        self.assertEqual(df['EAST CLARKE PLACE']['201505'], 0)
        df=self.Situation.RoadTable(1,'86 STREET TRANSVERSE')
        self.assertEqual(df['86 STREET TRANSVERSE']['201505'], 1)
        df=self.Situation.RoadTable(8,'86 STREET TRANSVERSE')
        self.assertEqual(df['86 STREET TRANSVERSE']['201505'], 0)
        pass
        
        
        

class ContributingMethods_Test(unittest.TestCase):


    def setUp(self):
        self.dirname, self.filename = os.path.split(os.path.abspath(__file__))
        self.DataPath=''.join([self.dirname[:-8]])
        print(self.DataPath)
        self.TimeBegin=[2015,5]
        self.TimeEnd = [2015,6]
        self.savepath = ''.join([self.dirname[:-8],'/test_results/'])
        self.NYC = StructureBuilding(self.TimeBegin,self.TimeEnd,self.DataPath)
        self.Contributing = ContributingMethods(self.NYC, self.savepath, self.TimeBegin,self.TimeEnd)
        self.Contributing.InfDICT_Init()
         

    def test_InfCalculate(self):
        Collisions = self.NYC.Borough_Dict['bk'].precinctList['060'].Collisions_intersection['2015']['05']
        Factors = self.NYC.Borough_Dict['bk'].precinctList['060'].Factors_intersection['2015']['05']
        df=self.Contributing.InfCalculate(1,1,Collisions,Factors)
        self.assertEqual(df['Number of Collisions']['BICYCLE'], 1)
        self.Contributing.InfCalculate(1,2,Collisions,Factors)
        self.assertEqual(df['Number of Collisions']['AGGRESSIVE DRIVING/ROAD RAGE'], 1)
        self.Contributing.InfCalculate(7,1,Collisions,Factors)
        self.assertEqual(df['MotoristsKilled']['BICYCLE'], 0)
        self.Contributing.InfCalculate(7,2,Collisions,Factors)
        self.assertEqual(df['MotoristsKilled']['AGGRESSIVE DRIVING/ROAD RAGE'], 0)
        
    def test_precinctInfTable_Unit(self):
        df=self.Contributing.precinctInfTable_Unit(self.NYC.Borough_Dict['bk'].precinctList['060'],1,1)
        self.assertEqual(df['Number of Collisions']['BICYCLE'], 7)
        df=self.Contributing.precinctInfTable_Unit(self.NYC.Borough_Dict['bk'].precinctList['060'],8,1)
        self.assertEqual(df['PassengInjured']['BICYCLE'], 0)
        df=self.Contributing.precinctInfTable_Unit(self.NYC.Borough_Dict['bk'].precinctList['060'],1,2)
        self.assertEqual(df['Number of Collisions']['AGGRESSIVE DRIVING/ROAD RAGE'], 1)
        df=self.Contributing.precinctInfTable_Unit(self.NYC.Borough_Dict['bk'].precinctList['060'],8,2)
        self.assertEqual(df['PassengInjured']['AGGRESSIVE DRIVING/ROAD RAGE'], 0)
        
    def test_BTHRInfTable_Unit(self):
        df=self.Contributing.BTHRInfTable_Unit(self.NYC.Road_Dict['135 AVENUE'],1,1)
        self.assertEqual(df['Number of Collisions']['BICYCLE'], 0)
        df=self.Contributing.BTHRInfTable_Unit(self.NYC.Road_Dict['135 AVENUE'],9,1)
        self.assertEqual(df['PassengKilled']['BICYCLE'], 0)
        df=self.Contributing.BTHRInfTable_Unit(self.NYC.Road_Dict['135 AVENUE'],1,2)
        self.assertEqual(df['Number of Collisions']['AGGRESSIVE DRIVING/ROAD RAGE'], 0)
        df=self.Contributing.BTHRInfTable_Unit(self.NYC.Road_Dict['135 AVENUE'],9,2)
        self.assertEqual(df['PassengKilled']['AGGRESSIVE DRIVING/ROAD RAGE'], 0)
        
    def test_BTHRInfTable_All(self):
        df=self.Contributing.BTHRInfTable_All(self.NYC.Road_Dict,1,1)
        self.assertEqual(df['Number of Collisions']['BICYCLE'], 882)
        df=self.Contributing.BTHRInfTable_All(self.NYC.Highway_Dict,9,1)
        self.assertEqual(df['PassengKilled']['BICYCLE'], 0)
        df=self.Contributing.BTHRInfTable_All(self.NYC.Bridge_Dict,1,2)
        self.assertEqual(df['Number of Collisions']['AGGRESSIVE DRIVING/ROAD RAGE'], 1)
        df=self.Contributing.BTHRInfTable_All(self.NYC.Tunnel_Dict,9,2)
        self.assertEqual(df['PassengKilled']['AGGRESSIVE DRIVING/ROAD RAGE'], 0)
        
    def test_BoroughInfTable_Unit(self):
        df=self.Contributing.BoroughInfTable_Unit(self.NYC.Borough_Dict['mn'],1,1)
        self.assertEqual(df['Number of Collisions']['BICYCLE'], 371)
        df=self.Contributing.BoroughInfTable_Unit(self.NYC.Borough_Dict['bk'],8,1)
        self.assertEqual(df['PassengInjured']['BICYCLE'], 35)
        df=self.Contributing.BoroughInfTable_Unit(self.NYC.Borough_Dict['si'],8,2)
        self.assertEqual(df['PassengInjured']['AGGRESSIVE DRIVING/ROAD RAGE'], 1)
        df=self.Contributing.BoroughInfTable_Unit(self.NYC.Borough_Dict['qn'],1,2)
        self.assertEqual(df['Number of Collisions']['AGGRESSIVE DRIVING/ROAD RAGE'], 32)
        
    def test_CityInfTable_Unit(self):
        df=self.Contributing.CityInfTable_Unit(self.NYC,1,1)
        self.assertEqual(df['Number of Collisions']['BICYCLE'], 1178)
        df=self.Contributing.CityInfTable_Unit(self.NYC,5,1)
        self.assertEqual(df['PersonsKilled']['BICYCLE'], 21)
        df=self.Contributing.CityInfTable_Unit(self.NYC,1,2)
        self.assertEqual(df['Number of Collisions']['AGGRESSIVE DRIVING/ROAD RAGE'], 179)
        df=self.Contributing.CityInfTable_Unit(self.NYC,5,2)
        self.assertEqual(df['PersonsKilled']['AGGRESSIVE DRIVING/ROAD RAGE'], 0)
        
    def test_precinctInfTable(self):
        df=self.Contributing.precinctInfTable(1,1,'060')
        self.assertEqual(df['Number of Collisions']['BICYCLE'], 7)
        df=self.Contributing.precinctInfTable(2,1,'060')
        self.assertEqual(df['Number of Collisions']['AGGRESSIVE DRIVING/ROAD RAGE'], 1)
        df=self.Contributing.precinctInfTable(1,11,'001')
        self.assertEqual(df['CyclistsKilled']['BICYCLE'], 0)
        df=self.Contributing.precinctInfTable(2,11,'100')
        self.assertEqual(df['CyclistsKilled']['AGGRESSIVE DRIVING/ROAD RAGE'], 0)
        
    def test_boroughInfTable(self):
        df=self.Contributing.boroughInfTable(1,1,'mn')
        self.assertEqual(df['Number of Collisions']['BICYCLE'], 371.0)
        df=self.Contributing.boroughInfTable(2,1,'bk')
        self.assertEqual(df['Number of Collisions']['AGGRESSIVE DRIVING/ROAD RAGE'], 63)
        df=self.Contributing.boroughInfTable(1,10,'si')
        self.assertEqual(df['CyclistsInjured']['BICYCLE'], 10)
        df=self.Contributing.boroughInfTable(2,10,'qn')
        self.assertEqual(df['CyclistsKilled']['AGGRESSIVE DRIVING/ROAD RAGE'], 0)
    
    def test_cityInfTable(self):
        df=self.Contributing.cityInfTable(1,1)
        self.assertEqual(df['Number of Collisions']['BICYCLE'], 1178.0)
        df=self.Contributing.cityInfTable(2,1)
        self.assertEqual(df['Number of Collisions']['AGGRESSIVE DRIVING/ROAD RAGE'], 179.0)
        df=self.Contributing.cityInfTable(1,12)
        self.assertEqual(df['PedestrInjured']['BICYCLE'], 4)
        df=self.Contributing.cityInfTable(2,12)
        self.assertEqual(df['PedestrInjured']['AGGRESSIVE DRIVING/ROAD RAGE'], 13)
        
    def test_BridgeInfTable(self):
        df=self.Contributing.BridgeInfTable(1,1,'MACOMBS DAM BR')
        self.assertEqual(df['Number of Collisions']['BICYCLE'], 0)
        df=self.Contributing.BridgeInfTable(2,1,'MACOMBS DAM BR')
        self.assertEqual(df['Number of Collisions']['AGGRESSIVE DRIVING/ROAD RAGE'], 0)
        df=self.Contributing.BridgeInfTable(1,3,'null')
        self.assertEqual(df['CollisionKilledCount']['BICYCLE'], 0)
        df=self.Contributing.BridgeInfTable(2,3,'MACOMBS DAM BR')
        self.assertEqual(df['CollisionKilledCount']['AGGRESSIVE DRIVING/ROAD RAGE'], 0)
        
    def test_HighwayInfTable(self):
        df=self.Contributing.HighwayInfTable(1,1,'MAJOR DEEGAN EXP')
        self.assertEqual(df['Number of Collisions']['BICYCLE'], 0)
        df=self.Contributing.HighwayInfTable(2,1,'MAJOR DEEGAN EXP')
        self.assertEqual(df['Number of Collisions']['AGGRESSIVE DRIVING/ROAD RAGE'], 2)
        df=self.Contributing.HighwayInfTable(1,4,'null')
        self.assertEqual(df['PersonsInjured']['BICYCLE'], 0)
        df=self.Contributing.HighwayInfTable(2,4,'null')
        self.assertEqual(df['PersonsInjured']['AGGRESSIVE DRIVING/ROAD RAGE'], 2)
        
    def test_TunnelInfTable(self):
        df=self.Contributing.TunnelInfTable(1,1,'BBT E TUBE')
        self.assertEqual(df['Number of Collisions']['BICYCLE'], 0)
        df=self.Contributing.TunnelInfTable(2,1,'BBT E TUBE')
        self.assertEqual(df['Number of Collisions']['AGGRESSIVE DRIVING/ROAD RAGE'], 0)
        df=self.Contributing.TunnelInfTable(1,5,'null')
        self.assertEqual(df['PersonsKilled']['BICYCLE'], 0)
        df=self.Contributing.TunnelInfTable(2,5,'null')
        self.assertEqual(df['PersonsKilled']['AGGRESSIVE DRIVING/ROAD RAGE'], 0)
        
    def test_BridgeTable(self):
        df=self.Contributing.BridgeInfTable(1,1,'QNSBORO BR UPPER')
        self.assertEqual(df['Number of Collisions']['BICYCLE'], 0)
        df=self.Contributing.BridgeInfTable(2,1,'QNSBORO BR UPPER')
        self.assertEqual(df['Number of Collisions']['AGGRESSIVE DRIVING/ROAD RAGE'], 0)
        df=self.Contributing.BridgeInfTable(1,6,'null')
        self.assertEqual(df['MotoristsInjured']['BICYCLE'], 0)
        df=self.Contributing.BridgeInfTable(2,6,'null')
        self.assertEqual(df['MotoristsInjured']['AGGRESSIVE DRIVING/ROAD RAGE'], 0)
        
    def test_RoadInfTable(self):
        df=self.Contributing.RoadInfTable(1,1,'86 STREET TRANSVERSE')
        self.assertEqual(df['Number of Collisions']['BICYCLE'], 0)
        df=self.Contributing.RoadInfTable(1,9,'86 STREET TRANSVERSE')
        self.assertEqual(df['PassengKilled']['BICYCLE'], 0)
        df=self.Contributing.RoadInfTable(2,1,'null')
        self.assertEqual(df['Number of Collisions']['AGGRESSIVE DRIVING/ROAD RAGE'], 114)
        df=self.Contributing.RoadInfTable(2,9,'null')
        self.assertEqual(df['PassengKilled']['AGGRESSIVE DRIVING/ROAD RAGE'], 0)

if __name__ == "__main__":
    unittest.main()