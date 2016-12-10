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
        self.NYC = StructureBuilding(self.TimeBegin1,self.TimeEnd1,self.DataPath)
        self.Situation = SituationMethods(self.NYC, self.savepath, self.TimeBegin,self.TimeEnd)

    def test_CityTable(self):
        values=dict(zip(range(1,15),[18375, 4643.0, 27.0, 4643.0, 27.0,
                                     1587.0,5.0,1832.0,4.0,464.0,1.0,760.0,17.0,3450.0]

        for indicator in self.Situation.Indicator.keys():
            self.assertEqual(list(self.Situation.CityTable(indicator, 'null').ix[0])[0],values[indicator])
        
            
    def test_BoroughTable(self):
        value_1=dict(zip([ 'bk', 'mn', 'bx', 'qn', 'si'],[3222,3086,2402,5138,789]))
        value_2=dict(zip([ 'bk', 'mn', 'bx', 'qn', 'si'],[856,525,721,1397,215]))
        value_3=dict(zip([ 'bk', 'mn', 'bx', 'qn', 'si'],[7,6,4,5,2]))
        value_4=dict(zip([ 'bk', 'mn', 'bx', 'qn', 'si'],[856,525,721,1397,215]))
        value_5=dict(zip([ 'bk', 'mn', 'bx', 'qn', 'si'],[7,6,4,5,2]))
        value_6=dict(zip([ 'bk', 'mn', 'bx', 'qn', 'si'],[293,127,266,551,104]))
        value_7=dict(zip([ 'bk', 'mn', 'bx', 'qn', 'si'],[2,0,1,0,2]))
        value_8=dict(zip([ 'bk', 'mn', 'bx', 'qn', 'si'],[315,160,299,590,89]))
        value_9=dict(zip([ 'bk', 'mn', 'bx', 'qn', 'si'],[1,1,0,2.0]))
        value_10=dict(zip([ 'bk', 'mn', 'bx', 'qn', 'si'],[99,105,50,90,5]))
        value_11=dict(zip([ 'bk', 'mn', 'bx', 'qn', 'si'],[0,1,0,0,0]))
        value_12=dict(zip([ 'bk', 'mn', 'bx', 'qn', 'si'],[149,133,106,166,17]))
        value_13=dict(zip([ 'bk', 'mn', 'bx', 'qn', 'si'],[4,4,3,3,0]))
        value_14=dict(zip([ 'bk', 'mn', 'bx', 'qn', 'si'],[628,447,511,1010,142]))
        values=dict(zip(range(1,15),[value_1,value_2,value_3,value_4,value_5,value_6,value_7,value_8,value_9,value_10,value_11,value_12,value_13,value_14]))
        for indicator in self.Situation.Indicator.keys():
            for name in [ 'bk', 'mn', 'bx', 'qn', 'si']:
                self.assertEqual(list(self.Situation.BoroughTable(indicator,name).ix[0])[0],values[indicator][name])
        
        values=dict(zip(range(1,15),[2402,721,4,721,4,266,1,299,0,50,0,106,3,511]))
        for indicator in self.Situation.Indicator.keys():
            self.assertEqual(self.Situation.BoroughTable(indicator,'null')['Bronx'][0],values[indicator][name])
                            
    def test_PrecinctTable(self):
        value_1=dict(zip([ '001', '100', '060'],[295,50,186]))
        value_2=dict(zip([ '001', '100', '060'],[49.0,14.0,35.0]))
        values=dict(zip(range(1,3),[value_1,value_2]))
        for indicator in [1,2]:
            for name in [ '001', '100', '060']:
                self.assertEqual(list(self.Situation.PrecinctTable(indicator,name).ix[0])[0],values[indicator][name])
        
        self.assertSequenceEqual(self.Situation.PrecinctTable(1,'null').shape(),(2,77))
        self.assertSequenceEqual(self.Situation.PrecinctTable(2,'null').shape(),(2,77))
    
    
    def test_PrecinctCalculate(self):
        
        df1 = list(self.NYC.Borough_Dict['mn'].precinctList.values())[0].Collisions_intersection['2015']['05']
        self.Situation.PrecinctCalculate(1,df1) 139
        self.Situation.PrecinctCalculate(4,df1) 19
        
    def test_PrecinctTableUnit(self):
        
        df1=self.Situation.PrecinctTableUnit(list(self.NYC.Borough_Dict['bk'].precinctList.values())[0],1)
               061
201505  299
201506  283
        df2=self.Situation.PrecinctTableUnit(list(self.NYC.Borough_Dict['qn'].precinctList.values())[0],6)
    112
201505  27.0
201506  23.0
    def test_BoroughTableUnit(self):
        
        df1=self.Situation.BoroughTableUnit(self.NYC.Borough_Dict['bk'],1)
        df2=self.Situation.BoroughTableUnit(self.NYC.Borough_Dict['qn'],6)
               Brooklyn
201505      5294
201506      5328
        Queens
201505   557.0
201506   635.0
        
    def test_CityTableUnit(self):
        values=dict(zip(range(1,15),[14637,3714.0,24.0,3714.0,24.0,1341.0,5.0,1453.0,4.0,349.0,1.0,571.0,14.0,2738]))
        for indicator in self.Situation.Indicator.keys():
            self.assertEqual(list(self.Situation.CityTableUnit(self.NYC,indicator).ix[0])[0],values[indicator])
            
    def test_BTHRcalculate(self):
        
        df = list(self.NYC.Road_Dict.values())[0].Collisions['2015']['05']
        self.Situation.BTHRcalculate(self,1,df)
        df = list(self.NYC.Road_Dict.values())[1].Collisions['2016']['05']
        self.Situation.BTHRcalculate(self,10,df)
        
    def test_BTHRTableUnit(self):
        
        self.Situation.BTHRTableUnit(list(self.NYC.Road_Dict.values())[0],1)
        
        pass
    def test_PrecinctTableAll(self):
        self.Situation.PrecinctTableAll(self.NYC.Borough_Dict['mn'].precinct_List,1)
        pass
    def test_BoroughTableAll(self):
        pass
    def test_BTHRTableAll(self):
        pass
    def test_TunnelTable(self):
        pass
    def test_BridgeTable(self):
        pass
    def test_HighwayTable(self):
        pass
    def test_RoadTable(self):
        pass
        
        
        
'''
class ContributingMethods_Test(unittest.TestCase):


    def setUp(self):
        


    def testName(self):
        pass

'''
if __name__ == "__main__":
    unittest.main()