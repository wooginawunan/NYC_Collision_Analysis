import unittest
import os
from WN_struct_building import StructureBuilding
from Methods.MethodClass import *

dirname, filename = os.path.split(os.path.abspath(__file__))
DataPath=''.join([dirname[:-8]])
print(DataPath)

TimeBegin = [2015,5]
TimeEnd = [2015,6]
savepath = ''.join([dirname[:-8],'/test_results/'])
NYC = StructureBuilding(TimeBegin,TimeEnd,DataPath)
Contributing = ContributingMethods(NYC, savepath, TimeBegin,TimeEnd)
Contributing.InfDICT_Init()


#def test_InfCalculate(self):
Collisions = NYC.Borough_Dict['bk'].precinctList['060'].Collisions_intersection['2015']['05']
Factors = NYC.Borough_Dict['bk'].precinctList['060'].Factors_intersection['2015']['05'] 
print(Contributing.InfCalculate(1,1,Collisions,Factors))
print(Contributing.InfCalculate(1,2,Collisions,Factors))

print(Contributing.InfCalculate(7,1,Collisions,Factors))

print(Contributing.InfCalculate(7,2,Collisions,Factors))
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')    
#    def test_precinctInfTable_Unit( ):
print(Contributing.precinctInfTable_Unit(NYC.Borough_Dict['bk'].precinctList['060'],1,1))
print(Contributing.precinctInfTable_Unit(NYC.Borough_Dict['bk'].precinctList['060'],8,1))
print(Contributing.precinctInfTable_Unit(NYC.Borough_Dict['bk'].precinctList['060'],1,2))
print(Contributing.precinctInfTable_Unit(NYC.Borough_Dict['bk'].precinctList['060'],8,2))
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')        
#   def test_BTHRInfTable_Unit(self):
print(Contributing.BTHRInfTable_Unit(NYC.Road_Dict['135 AVENUE'],1,1))
print(Contributing.BTHRInfTable_Unit(NYC.Road_Dict['135 AVENUE'],9,1))
print(Contributing.BTHRInfTable_Unit(NYC.Road_Dict['135 AVENUE'],1,2))
print(Contributing.BTHRInfTable_Unit(NYC.Road_Dict['135 AVENUE'],9,2))
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')        
#  def test_BTHRInfTable_All(self):
print(Contributing.BTHRInfTable_All( NYC.Road_Dict,1,1))
print(Contributing.BTHRInfTable_All( NYC.Highway_Dict,9,1))
print(Contributing.BTHRInfTable_All( NYC.Bridge_Dict,1,2))
print(Contributing.BTHRInfTable_All( NYC.Tunnel_Dict,9,2))
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')        
# def test_BoroughInfTable_Unit(self):
print(Contributing.BoroughInfTable_Unit( NYC.Borough_Dict['mn'],1,1))
print(Contributing.BoroughInfTable_Unit( NYC.Borough_Dict['bk'],8,1))
print(Contributing.BoroughInfTable_Unit( NYC.Borough_Dict['si'],8,2))
print(Contributing.BoroughInfTable_Unit( NYC.Borough_Dict['qn'],1,2))
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')        
#  def test_CityInfTable_Unit(self):
print(Contributing.CityInfTable_Unit( NYC,1,1))
print(Contributing.CityInfTable_Unit( NYC,5,1))
print(Contributing.CityInfTable_Unit( NYC,1,2))
print(Contributing.CityInfTable_Unit( NYC,5,2))
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')        
# def test_precinctInfTable(self):
print(Contributing.precinctInfTable(1,1,'060'))
print(Contributing.precinctInfTable(2,1,'060'))
print(Contributing.precinctInfTable(1,11,'001'))
print(Contributing.precinctInfTable(2,11,'100'))
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')        
#  def test_boroughInfTable(self):
print(Contributing.boroughInfTable(1,1,'mn'))
print(Contributing.boroughInfTable(2,1,'bk'))
print(Contributing.boroughInfTable(1,10,'si'))
print(Contributing.boroughInfTable(2,10,'qn'))
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')       
#  def test_cityInfTable(self):
print(Contributing.cityInfTable(1,1))
print(Contributing.cityInfTable(2,1))
print(Contributing.cityInfTable(1,12))
print(Contributing.cityInfTable(2,12))
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')        
# def test_BridgeInfTable(self):
print(Contributing.BridgeInfTable(1,1,'MACOMBS DAM BR'))
print(Contributing.BridgeInfTable(2,1,'MACOMBS DAM BR'))
print(Contributing.BridgeInfTable(1,3,'null'))
print(Contributing.BridgeInfTable(2,3,'MACOMBS DAM BR'))
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')        
#   def test_HighwayInfTable(self):
print(Contributing.HighwayInfTable(1,1,'MAJOR DEEGAN EXP'))
print(Contributing.HighwayInfTable(2,1,'MAJOR DEEGAN EXP'))
print(Contributing.HighwayInfTable(1,4,'null'))
print(Contributing.HighwayInfTable(2,4,'null'))
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')       
#   def test_TunnelInfTable(self):
print(Contributing.TunnelInfTable(1,1,'BBT E TUBE'))
print(Contributing.TunnelInfTable(2,1,'BBT E TUBE'))
print(Contributing.TunnelInfTable(1,5,'null'))
print(Contributing.TunnelInfTable(2,5,'null'))
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')    
#  def test_BridgeTable(self):
print(Contributing.BridgeInfTable(1,1,'QNSBORO BR UPPER'))
print(Contributing.BridgeInfTable(2,1,'QNSBORO BR UPPER'))
print(Contributing.BridgeInfTable(1,6,'null'))
print(Contributing.BridgeInfTable(2,6,'null'))
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')       
# def test_RoadInfTable(self):
print(Contributing.RoadInfTable(1,1,'86 STREET TRANSVERSE'))
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
print(Contributing.RoadInfTable(1,9,'86 STREET TRANSVERSE'))
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
print(Contributing.RoadInfTable(2,1,'null'))
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
print(Contributing.RoadInfTable(2,9,'null'))
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')











'''




















#1 #7

for indicator in Situation.Indicator.keys():
    print(list(Situation.CityTable(indicator, 'null').ix[0])[0],end=", ")
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
#2
for indicator in Situation.Indicator.keys():
    values[indicator]=[]
    for name in ['bk', 'mn', 'bx', 'qn', 'si']:
        values[indicator].append(list(Situation.BoroughTable(indicator,name).ix[0])[0])
    print(values[indicator],end=", ")
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
#2    
for indicator in Situation.Indicator.keys():
    print(Situation.BoroughTable(indicator,'null'))
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

#3
for indicator in [1,2]:
    for name in [ '001', '100', '060']:
        print(list(Situation.PrecinctTable(indicator,name).ix[0])[0],end=", ")

#3
print(Situation.PrecinctTable(1,'null').shape)
print(Situation.PrecinctTable(2,'null').shape)
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>') 
#4
df1 = list(NYC.Borough_Dict['mn'].precinctList.values())[0].Collisions_intersection['2015']['05']
        
print(Situation.PrecinctCalculate(1,df1))
print(Situation.PrecinctCalculate(4,df1))   
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
#5
df1=Situation.PrecinctTableUnit(list(NYC.Borough_Dict['bk'].precinctList.values())[0],1)
print(df1)
df2=Situation.PrecinctTableUnit(list(NYC.Borough_Dict['qn'].precinctList.values())[0],6)
print(df2)
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
#6
df1=Situation.BoroughTableUnit(NYC.Borough_Dict['bk'],1)

df2=Situation.BoroughTableUnit(NYC.Borough_Dict['qn'],6)
print(df1)
print(df2)
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
#8
#def test_BTHRcalculate(self):
        
#df = list(NYC.Road_Dict.values())[0].Collisions['2015']['05']
#print(Situation.BTHRcalculate(1,df))
df = list(NYC.Road_Dict.values())[1].Collisions['2015']['06']
print(Situation.BTHRcalculate(10,df))
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
#9
print(Situation.BTHRTableUnit(list(NYC.Road_Dict.values())[0],1))
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')






#10
print(Situation.PrecinctTableAll(NYC.Borough_Dict['mn'].precinctList,1))
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
#11
print(Situation.BoroughTableAll(NYC.Borough_Dict,1))
print(Situation.BoroughTableAll(NYC.Borough_Dict,10))
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
#12
print(Situation.BTHRTableAll(NYC.Bridge_Dict,1))
print(Situation.BTHRTableAll(NYC.Tunnel_Dict,13))
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
#13

print(Situation.TunnelTable(1,'null'))
print(Situation.TunnelTable(13,'null'))
print(Situation.TunnelTable(1,'BBT E TUBE'))
print(Situation.TunnelTable(13,'BBT E TUBE'))
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
#14
print(Situation.BridgeTable(1,'null'))
print(Situation.BridgeTable(3,'null'))
print(Situation.BridgeTable(1,'QNSBORO BR UPPER'))
print(Situation.BridgeTable(3,'QNSBORO BR UPPER'))
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

#15
print(Situation.HighwayTable(1,'null'))
print(Situation.HighwayTable(5,'null'))
print(Situation.HighwayTable(1,'LAURELTON PKY'))
print(Situation.HighwayTable(5,'LAURELTON PKY'))
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

#16
print(Situation.RoadTable(1,'null'))
print(Situation.RoadTable(8,'null'))
print(Situation.RoadTable(1,'86 STREET TRANSVERSE'))
print(Situation.RoadTable(8,'86 STREET TRANSVERSE'))
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')


'''





    


