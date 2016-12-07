from WN_struct_building.CityStructure import borough

def TotalAccident(self, level, name,indicator):
	num = 0
	if(level == "City"):
		sum=0
		for borough in self.Borough_Dict.values():
			for precinct in borough.precinctList.values():
				for year in precinct.Collisions_intersection.values():
					for month in year.values():
						sum(month['PersonKilled'])
						len(month)
 
	if(level == "Borough"):
		for precinct in self.Borough_Dict[name].values():
		    for year in precinct.Collisions_intersection.values():
					for month in year.values():
						sum(month['PersonKilled'])
						len(month)
						
		
		
		for n in name:
			for p in self.data.Borough_Dict[n].precinctList:
				num = num + TotalAccident(self, "Precinct", p.ID)
	if(level == "Precinct"):
		for n in name:
			for b in ['bk', 'bx','mn','qn','si']:
				if (self.data.Borough_Dict[b].precinctList[name] != null) :
					for Year, Month, collisions_I in self.data.Borough_Dict[b].precinctList[name].Collisions_intersection['2015']['01']:
						num = num + 1
					for Year, Month, collisions_H in self.data.Borough_Dict[b].precinctList[name].Collisions_HighTunBri:
						num = num + 1
					break


	if(level == "Road"):
		if name==[]:
			for road in self.Road_Dict.values():
			for year in precinct.Collisions_intersection.values():
					for month in year.values():
						sum(month['PersonKilled'])
						len(month)
		else:
			for year in self.Road_Dict[name].values():
					for month in year.values():
						sum(month['PersonKilled'])
						len(month)
			    
			    
			    
			    
			    
		for n in name:
			for Year, Month, Collisions in self.data.Road_Dict[n]:
				num = num + 1

	if(level == "Highway"):
		for n in name:
			for Year, Month, Collisions in self.data.Highway_Dict[n]:
				num = num + 1
	if(level == "Bridge"):
		for n in name:
			for Year, Month, Collisions in self.data.Bridge_Dict[n]:
				num = num + 1
	if(level == "Tunnel"):
		for n in name:
			for Year, Month, Collisions in self.data.Tunnel_Dict[n]:
				num = num + 1
	return num

def TotalInjury(self, level, name, timeStart, timeEnd):
	num = 0
	# if(level == "City"):

	if(level == "Borough"):
		for n in name:
			for p in self.data.Borough_Dict[n].precinctList:
				num = num + TotalAccident(self, "Precinct", p.ID)
	if(level == "Precinct"):
		for n in name:
			for b in ['bk', 'bx','mn','qn','si']:
				if (self.data.Borough_Dict[b].precinctList[name] != null) :
					for Year, Month, collisions_I in self.data.Borough_Dict[b].precinctList[name].Collisions_intersection:
						num = num + collisions_I.PersonsInjured
					for Year, Month, collisions_H in self.data.Borough_Dict[b].precinctList[name].Collisions_HighTunBri:
						num = num + Collisions_H.PersonsInjured
					break


	if(level == "Road"):
		for n in name:
			for Year, Month, Collisions in self.data.Road_Dict[n]:
				num = num + Collisions.PersonsInjured

	if(level == "Highway"):
		for n in name:
			for Year, Month, Collisions in self.data.Highway_Dict[n]:
				num = num + Collisions.PersonsInjured
	if(level == "Bridge"):
		for n in name:
			for Year, Month, Collisions in self.data.Bridge_Dict[n]:
				num = num + Collisions.PersonsInjured
	if(level == "Tunnel"):
		for n in name:
			for Year, Month, Collisions in self.data.Tunnel_Dict[n]:
				num = num + Collisions.PersonsInjured
	return num

def TotalKilled(self, level, name, timeStart, timeEnd):
	num = 0
	# if(level == "City"):

	if(level == "Borough"):
		for n in name:
			for p in self.data.Borough_Dict[n].precinctList:
				num = num + TotalAccident(self, "Precinct", p.ID)
	if(level == "Precinct"):
		for n in name:
			for b in ['bk', 'bx','mn','qn','si']:
				if (self.data.Borough_Dict[b].precinctList[name] != null) :
					for Year, Month, collisions_I in self.data.Borough_Dict[b].precinctList[name].Collisions_intersection:
						num = num + collisions_I.PersonsKilled
					for Year, Month, collisions_H in self.data.Borough_Dict[b].precinctList[name].Collisions_HighTunBri:
						num = num + Collisions_H.PersonsKilled
					break


	if(level == "Road"):
		for n in name:
			for Year, Month, Collisions in self.data.Road_Dict[n]:
				num = num + Collisions.PersonsKilled

	if(level == "Highway"):
		for n in name:
			for Year, Month, Collisions in self.data.Highway_Dict[n]:
				num = num + Collisions.PersonsKilled
	if(level == "Bridge"):
		for n in name:
			for Year, Month, Collisions in self.data.Bridge_Dict[n]:
				num = num + Collisions.PersonsKilled
	if(level == "Tunnel"):
		for n in name:
			for Year, Month, Collisions in self.data.Tunnel_Dict[n]:
				num = num + Collisions.PersonsKilled
	return num
