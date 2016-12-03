
def TotalAccident(self, level, name, timeStart, timeEnd):
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
						num = num + 1
					for Year, Month, collisions_H in self.data.Borough_Dict[b].precinctList[name].Collisions_HighTunBri:
						num = num + 1
					break


	if(level == "Road"):
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
