'''
structure of the city
Class:
city
  borough
    precinct
  road
  highway
  bridge
  tunnel
  
  
Version 1
Copyright:
@ Nan Wu 
@ nw1045@nyu.edu
@ wooginawunan@gmail.com
'''
import numpy as np
class city():
    def __init__(self,name='New York City'):
        self.name=name
        self.Borough_Dict=dict()
        self.Road_Dict=dict()
        self.Highway_Dict=dict()
        self.Tunnel_Dict=dict()
        self.Bridge_Dict=dict()
    def bridgeCatalog(self):
        return sorted(self.Bridge_Dict.keys())
    def tunnelCatalog(self):
        return sorted(self.Tunnel_Dict.keys())
    def highwayCatalog(self):
        return sorted(self.Highway_Dict.keys())
    def roadCatalog(self):
        first=list('ABCDEFGHIGKLMNOPQRSTUVWXYZ')
        keys=list('ABCDEFGHIGKLMNOPQRSTUVWXYZ')
        keys.append('*Other')
        Road_Catalog=dict.fromkeys(keys)
        roadKey = np.array(list(self.Road_Dict.keys()))
        mask=np.array([x.startswith(y) for x in self.Road_Dict.keys() for y in first]).reshape(len(self.Road_Dict),26)
        for i in range(0,26):
            key=first[i]
            Road_Catalog[key]=roadKey[mask[:,i]]
            
        Road_Catalog['*Other']=roadKey[np.logical_not(np.any(mask,1))]
        return Road_Catalog
    def boroughCatalog(self):
        Fullname={'bk': 'Brooklyn', 'bx': 'Bronx','mn':'Manhattan','qn':'Queens','si':'Staten_Island'} 
        Road_Catalog=[]
        for key in self.Borough_Dict.keys():
            Road_Catalog.append(key+' : '+Fullname[key])
        return Road_Catalog
    def init_borough(self):
        Manhattan=borough('Manhattan')
        Bronx=borough('Bronx')
        Brooklyn=borough('Brooklyn')
        Queens=borough('Queens')
        Staten_Island= borough('Staten Island') 
        self.Borough_Dict={'bk': Brooklyn, 'bx': Bronx,'mn':Manhattan,'qn':Queens,'si':Staten_Island}
    
    def add_road(self,road):
        self.Road_Dict[road.name]=road
    
    def add_highway(self,highway):
        self.Highway_Dict[highway.name]=highway
        
    def add_bridge(self,bridge):
        self.Bridge_Dict[bridge.name]=bridge
    
    def add_tunnel(self,tunnel):
        self.Tunnel_Dict[tunnel.name]=tunnel
        
    
            
class borough():
    def __init__(self,name_bo):
        self.name=name_bo
        self.precinctList=dict()
    def addprecinct(self, precinct):
        self.precinctList[precinct.ID]= precinct
    def precinctCatalog(self):
        return sorted(self.precinctList.keys())
    
    def __repr__(self):
        str_print="Borough Name %s \n" % self.name
        str_print = str_print + 'It has %d precincts\n' % len(self.precinctList)
        return str_print
        '''
        for precinct in self.precinctList:
            str_print = str_print + str(precinct) + '\n'
            return str_print
            '''
        
    
class precinct():
    '''
    classdocs
    '''
    

    def __init__(self, ID):
        '''
        Constructor
        '''
        self.ID=ID
        dict_Month=dict()
        self.Collisions_intersection={'2015': dict_Month,'2016': dict_Month}
        self.Collisions_HighTunBri={'2015': dict_Month,'2016': dict_Month}
        self.Factors_intersection={'2015': dict_Month,'2016': dict_Month}
        self.Factors_HighTunBri={'2015': dict_Month,'2016': dict_Month}
    
    def addCollisions_Intersection(self,year,month,collisions_I,factors_I):
        self.Collisions_intersection[year][month]=collisions_I
        self.Factors_intersection[year][month]= factors_I

    
    def addCollisions_HighTunBri(self,year,month,collisions_H,factors_H):
        self.Collisions_HighTunBri[year][month]=collisions_H
        self.Factors_HighTunBri[year][month]= factors_H
           
    
        
    
class road():
    def __init__(self,name_road):
        self.name=name_road
        dict_Month=dict()
        self.Collisions={'2015': dict_Month,'2016': dict_Month}
        self.Factors={'2015': dict_Month,'2016': dict_Month}
    def addCollisions(self,year,month,collisions,factors):
        self.Collisions[year][month]=collisions
        self.Factors[year][month]= factors

class highway(road):
    pass
class bridge(road):
    pass
class tunnel(road):
    pass

# class highway():
#     def __init__(self,name_highway):
#         self.name=name_highway
#         dict_Month=dict()
#         self.Collisions={'2015': dict_Month,'2016': dict_Month}
#         self.Factors={'2015': dict_Month,'2016': dict_Month}
#     def addCollisions(self,year,month,collisions,factors):
#         self.Collisions[year][month]=collisions
#         self.Factors[year][month]= factors
#         
#     
# class bridge():
#     def __init__(self,name_bridge):
#         self.name=name_bridge
#         dict_Month=dict()
#         self.Collisions={'2015': dict_Month,'2016': dict_Month}
#         self.Factors={'2015': dict_Month,'2016': dict_Month}
#     def addCollisions(self,year,month,collisions,factors):
#         self.Collisions[year][month]=collisions
#         self.Factors[year][month]= factors
# 
# class tunnel():
#     def __init__(self,name_tunnel):
#         self.name=name_tunnel
#         dict_Month=dict()
#         self.Collisions={'2015': dict_Month,'2016': dict_Month}
#         self.Factors={'2015': dict_Month,'2016': dict_Month}
#     def addCollisions(self,year,month,collisions,factors):
#         self.Collisions[year][month]=collisions
#         self.Factors[year][month]= factors
#         
#         
        
        
        
        
        
        
        