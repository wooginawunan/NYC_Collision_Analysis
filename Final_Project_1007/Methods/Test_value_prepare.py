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
Situation = SituationMethods(NYC, savepath, TimeBegin,TimeEnd)
values=dict.fromkeys(range(1,15))



for indicator in Situation.Indicator.keys():
    print(list(Situation.CityTable(indicator, 'null').ix[0])[0])

for indicator in [1,2]:
    for name in [ '001', '100', '060']:
        print(list(Situation.PrecinctTable(indicator,name).ix[0])[0])
        
print(Situation.PrecinctTable(1,'null').shape)
print(Situation.PrecinctTable(2,'null').shape)

print(NYC.boroughCatalog())
print(NYC.Borough_Dict['mn'].precinctCatalog())
print(NYC.Borough_Dict['bk'].precinctCatalog())
print(NYC.Borough_Dict['bx'].precinctCatalog())
print(NYC.Borough_Dict['qn'].precinctCatalog())
print(NYC.Borough_Dict['si'].precinctCatalog())  

df1 = list(NYC.Borough_Dict['mn'].precinctList.values())[0].Collisions_intersection['2015']['05']
        
print(Situation.PrecinctCalculate(1,df1))
print(Situation.PrecinctCalculate(4,df1))   

df1=Situation.PrecinctTableUnit(list(NYC.Borough_Dict['bk'].precinctList.values())[0],1)
print(df1)
df2=Situation.PrecinctTableUnit(list(NYC.Borough_Dict['qn'].precinctList.values())[0],6)
print(df2)

df1=Situation.BoroughTableUnit(NYC.Borough_Dict['bk'],1)

df2=Situation.BoroughTableUnit(NYC.Borough_Dict['qn'],6)
print(df1)
print(df2)






        

        
for indicator in Situation.Indicator.keys():
    values[indicator]=[]
    for name in ['bk', 'mn', 'bx', 'qn', 'si']:
        values[indicator].append(Situation.BoroughTable(indicator,name).ix[0])
    print(values[indicator])
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    
for indicator in Situation.Indicator.keys():
    print(Situation.BoroughTable(indicator,'null'))
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

    


