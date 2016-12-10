'''
When loading the files, we directly take informations grouped by area and other geo level to build a city structure.
structure of the city.
All information is stored by a City object.

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
    '''
    City class
    Contains all collision information in the city by borough, road, highway,bridge,tunnel.
    When acquiring specific information in sub level of a city, by iterating the relevant Dictionary.
    Attributes:
        name: 
            The city name (Default New York City)
            Type: String
        Borough_Dict: 
            All Borough in the city. For NYC, there are 'bk': 'Brooklyn', 'bx': 'Bronx','mn':'Manhattan','qn':'Queens','si':'Staten_Island'
            Type:Dictionary.
                Keys: 'bk' 'mn' 'bx' 'qn' 'si' (short name for each Borough)
                Values: borough object             
        Road_Dict:
            All Road in the city. 
            Type:Dictionary.
                Keys: Road name 
                Values: road object             
        Highway_Dict:
            All Highway in the city. 
            Type:Dictionary.
                Keys: Highway name 
                Values: Highway object             
        Tunnel_Dict:
            All Tunnel in the city. 
            Type:Dictionary.
                Keys: Tunnel name 
                Values: Tunnel object             
        Bridge_Dict:
            All Bridge in the city. 
            Type:Dictionary.
                Keys: Bridge name 
                Values: Bridge object            
    
    Methods:
        init_borough
        
        add_road
        add_highway
        add_bridge
        add_tunnel
        
        bridgeCatalog
        tunnelCatalog
        highwayCatalog
        roadCatalog
        boroughCatalog
    '''
    def __init__(self,name='New York City'):
        '''
        Create a city object
        '''
        self.name=name
        self.Borough_Dict=dict()
        self.Road_Dict=dict()
        self.Highway_Dict=dict()
        self.Tunnel_Dict=dict()
        self.Bridge_Dict=dict()
    
    def init_borough(self):
        '''
        borough Dict init
        '''
        Manhattan=borough('Manhattan')
        Bronx=borough('Bronx')
        Brooklyn=borough('Brooklyn')
        Queens=borough('Queens')
        Staten_Island= borough('Staten Island') 
        self.Borough_Dict={'bk': Brooklyn, 'bx': Bronx,'mn':Manhattan,'qn':Queens,'si':Staten_Island}
    
    def add_road(self,road):
        '''
        Add new road to the city
        '''
        self.Road_Dict[road.name]=road
    
    def add_highway(self,highway):
        '''
        Add new highway to the city
        '''
        self.Highway_Dict[highway.name]=highway
        
    def add_bridge(self,bridge):
        '''
        Add new bridge to the city
        '''
        self.Bridge_Dict[bridge.name]=bridge
    
    def add_tunnel(self,tunnel):
        '''
        Add new tunnel to the city
        '''
        self.Tunnel_Dict[tunnel.name]=tunnel
    
    def bridgeCatalog(self):
        '''
        return All bridges name as list, Sorted by name 
        '''
        return sorted(self.Bridge_Dict.keys())
    
    def tunnelCatalog(self):
        '''
        return All tunnels name as list, Sorted by name 
        '''
        return sorted(self.Tunnel_Dict.keys())
    
    def highwayCatalog(self):
        '''
        return All highways name as list, Sorted by name 
        '''
        return sorted(self.Highway_Dict.keys())
    
    def roadCatalog(self):
        '''
        return a dictionary of all roads name.
        with 'ABCDEFGHIGKLMNOPQRSTUVWXYZ' and '*Other' as key (The first letter of the road name)
        with all road name begin with the key as the value.
        
        '''
        first=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        keys=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
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
        '''
        return a list of strings, each string is like 'bk: Brooklyn'
        '''
        Fullname={'bk': 'Brooklyn', 'bx': 'Bronx','mn':'Manhattan','qn':'Queens','si':'Staten_Island'} 
        Road_Catalog=[]
        for key in self.Borough_Dict.keys():
            Road_Catalog.append(key+' : '+Fullname[key])
        return Road_Catalog
    
            
class borough():
    '''
    borough class
    attributes:
       name: borough name
       precinctList:  all precinct in the borough
           dictionary. 
           keys: precinctID; value: relevant precinct object
    methods:
       addprecinct: add new precinct
       precinctCatalog: Catalog of all precinct ID in the borough
       
    
    '''
    def __init__(self,name_bo):
        '''
        create a borough with name
        '''
        self.name=name_bo
        self.precinctList=dict()
    def addprecinct(self, precinct):
        '''
        add new precinct
        '''
        self.precinctList[precinct.ID]= precinct
    def precinctCatalog(self):
        '''
        return All precincts ID as list, Sorted by name 
        '''
        return sorted(self.precinctList.keys())
    
    def __repr__(self):
        str_print="Borough Name %s \n" % self.name
        str_print = str_print + 'It has %d precincts\n' % len(self.precinctList)
        return str_print
      
        
    
class precinct():
    '''
    precinct Class
    attributes:
        ID
        Collisions_intersection:  a dictionary by time of all collisions records related to intersections  
           Type: dictionary
           keys: level 1(year):  '2015' '2016'
                 level 2(month): '01'...'12'  (default none)
           values: a data frame with information of collisions happened on this precinct at a specific year and month
                 columns: OccurrencePrecinctCode    CollisionID    CollisionKey    
                          Collision_ at_Intersection    IntersectionAddress    IntersectingStreet    CrossStreet    
                          CollisionVehicleCount    
                          CollisionInjuredCount    CollisionKilledCount    Vehicles_or_MotoristsInvolved    
                          PersonsInjured    PersonsKilled    MotoristsInjured    MotoristsKilled    PassengInjured    
                          PassengKilled    CyclistsInjured    CyclistsKilled    PedestrInjured    PedestrKilled    
                          Injury_or_Fatal    Bicycle
        Collisions_HighTunBri:  a dictionary by time of all collisions records related to Highway, bridge, or tunnel
           Type: dictionary
           keys: level 1(year):  '2015' '2016'
                 level 2(month): '01'...'12'  (default none)
           values: a data frame with information of collisions happened on this precinct at a specific year and month  
                columns: OccurrencePrecinctCode    CollisionID    CollisionKey    RoadwayTypeCode    RoadwayReferenceMarker    
                         Collision_ at_Location    RoadwayName    RoadwayDirection    RoadwayLocationDescription    
                         CollisionVehicleCount    CollisionInjuredCount    CollisionKilledCount    Vehicles_or_MotoristsInvolved    
                         PersonsInjured    PersonsKilled    MotoristsInjured    MotoristsKilled    PassengInjured    PassengKilled    
                         CyclistsInjured    CyclistsKilled    PedestrInjured    PedestrKilled    Injury_or_Fatal    Bicycle
        Factors_intersection: a dictionary by time of all collisions records related to intersections 
           Type: dictionary
           keys: level 1(year):  '2015' '2016'
                 level 2(month): '01'...'12'  (default none)
           values: a data frame with information of collisions happened on this precinct at a specific year and month
                columns:CollisionID    CollisionKey    VehicleSequenceNumber    VehicleTypeCode    VehicleTypeDescription    
                ContributingFactorCode    ContributingFactorDescription
                
                
        Factors_HighTunBri: a dictionary by time of all collisions records related to Highway, bridge, or tunnel 
           Type: dictionary
           keys: level 1(year):  '2015' '2016'
                 level 2(month): '01'...'12'  (default none)
           values: a data frame with information of collisions happened on this precinct at a specific year and month
                columns: OccurrencePrecinctCode RoadwayReferenceMarker    CollisionID    CollisionKey    
                         VehicleSequenceNumber    VehicleTypeCode    VehicleTypeDescription    ContributingFactorCode    
                         ContributingFactorDescription
    methods:
        addCollisions_Intersection: 
           add data frame
        addFactors_Intersection:
           add data frame
        addCollisions_HighTunBri:
           add data frame
    '''
    def __init__(self, ID):
        '''
        Constructor of precinct class
        '''
        self.ID=ID
        self.Collisions_intersection={'2015': dict(),'2016': dict()}
        self.Collisions_HighTunBri={'2015': dict(),'2016': dict()}
        self.Factors_intersection={'2015': dict(),'2016': dict()}
        self.Factors_HighTunBri={'2015': dict(),'2016': dict()}
    
    def addCollisions_Intersection(self,year,month,collisions_I):
        '''
        add by time of collisions records related to intersection
        '''
        self.Collisions_intersection[year][month]=collisions_I
        
    def addFactors_Intersection(self,year,month,factors_I):
        '''
        add by time of collisions records related to intersection
        '''
        self.Factors_intersection[year][month]= factors_I
        
    def addCollisions_HighTunBri(self,year,month,collisions_H,factors_H):
        '''
        aadd by time of collisions records related to Highway, bridge, or tunnel
        '''
        self.Collisions_HighTunBri[year][month]=collisions_H
        self.Factors_HighTunBri[year][month]= factors_H
           
    
class BTHR():
    '''
    Highway, bridge, tunnel or Road  Class
    attributes:
        name:
        Collisions:  a dictionary by time of all collisions records related to Highway, bridge, or tunnel
           Type: dictionary
           keys: level 1(year):  '2015' '2016'
                 level 2(month): '01'...'12'  (default none)
           values: a data frame with information of collisions happened on this precinct at a specific year and month  
                columns: OccurrencePrecinctCode    CollisionID    CollisionKey    RoadwayTypeCode    RoadwayReferenceMarker    
                         Collision_ at_Location    RoadwayName    RoadwayDirection    RoadwayLocationDescription    
                         CollisionVehicleCount    CollisionInjuredCount    CollisionKilledCount    Vehicles_or_MotoristsInvolved    
                         PersonsInjured    PersonsKilled    MotoristsInjured    MotoristsKilled    PassengInjured    PassengKilled    
                         CyclistsInjured    CyclistsKilled    PedestrInjured    PedestrKilled    Injury_or_Fatal    Bicycle
        Factors: a dictionary by time of all collisions records related to Highway, bridge, or tunnel 
           Type: dictionary
           keys: level 1(year):  '2015' '2016'
                 level 2(month): '01'...'12'  (default none)
           values: a data frame with information of collisions happened on this precinct at a specific year and month
                columns: OccurrencePrecinctCode RoadwayReferenceMarker    CollisionID    CollisionKey    
                         VehicleSequenceNumber    VehicleTypeCode    VehicleTypeDescription    ContributingFactorCode    
                         ContributingFactorDescription
    methods:
        addCollisions: 
    '''
    def __init__(self,name):
        self.name=name
        self.Collisions={'2015': dict(),'2016': dict()}
        self.Factors={'2015': dict(),'2016': dict()}
    def addCollisions(self,year,month,collisions,factors):
        self.Collisions[year][month]=collisions
        self.Factors[year][month]= factors

class road(BTHR):
    '''
    All collisions information happened on a specific road
    '''
    pass
class highway(BTHR):
    '''
    All collisions information happened on a specific highway
    '''
    pass
class bridge(BTHR):
    '''
    All collisions information happened on a specific bridge
    '''
    pass
class tunnel(BTHR):
    '''
    All collisions information happened on a specific tunnel
    '''
    pass

        
        
        
        
        
        
        