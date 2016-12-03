
def TotalAccident(self, level, name, timeStart, timeEnd):
	num = 0
	info = {}
	# if(level == "City"):

	if(level == "Borough"):
		for n in name:
			for p in self.data.Borough_Dict[n].precinctList:
				num = num + TotalAccident(self, "Precinct", p.ID).num
				info.append(TotalAccident(self, "Precinct", p.ID).info)
	if(level == "Precinct"):
		for n in name:
			for b in ['bk', 'bx','mn','qn','si']:
				if (self.data.Borough_Dict[b].precinctList[name] != null) :
					for Year, Month, Intersection in self.data.Borough_Dict[b].precinctList[name]:
						num = num + 1
						info.append({	'city': NYC.Borough_Dict[n],
										'Year': Year, 
										'Month': Month,
										'Intersection': {
											'collisions': Intersection.collisions,
											'factors': Intersection.factors},
											'HighTunBri':{
												'collisions': Intersection.HighTunBri.collisions,
												'factors': Intersection.HighTunBri.factors
											}
										})	
					break


	if(level == "Road"):
		for n in name:
			for Year, Month, Intersection in self.data.Road_Dict[n]:
				num = num + 1
				info.append({	'city': NYC.Road_Dict[area],
								'Year': Year, 
								'Month': Month,
								'Intersection': {
									'collisions': Intersection.collisions,
									'factors': Intersection.factors},
									'HighTunBri':{
										'collisions': Intersection.HighTunBri.collisions,
										'factors': Intersection.HighTunBri.factors
									}
								})

	if(level == "Highway"):
		for n in name:
			for Year, Month, Intersection in self.data.Highway_Dict[n]:
				num = num + 1
				info.append({	'city': NYC.Highway_Dict[area],
								'Year': Year, 
								'Month': Month,
								'Intersection': {
									'collisions': Intersection.collisions,
									'factors': Intersection.factors},
									'HighTunBri':{
										'collisions': Intersection.HighTunBri.collisions,
										'factors': Intersection.HighTunBri.factors
									}
								})
	if(level == "Bridge"):
		for n in name:
			for Year, Month, Intersection in self.data.Bridge_Dict[n]:
				num = num + 1
				info.append({	'city': NYC.Bridge_Dict[area],
								'Year': Year, 
								'Month': Month,
								'Intersection': {
									'collisions': Intersection.collisions,
									'factors': Intersection.factors},
									'HighTunBri':{
										'collisions': Intersection.HighTunBri.collisions,
										'factors': Intersection.HighTunBri.factors
									}
								})
	if(level == "Tunnel"):
		for n in name:
			for Year, Month, Intersection in self.data.Tridge_Dict[n]:
				num = num + 1
				info.append({	'city': NYC.Tridge_Dict[area],
								'Year': Year, 
								'Month': Month,
								'Intersection': {
									'collisions': Intersection.collisions,
									'factors': Intersection.factors},
									'HighTunBri':{
										'collisions': Intersection.HighTunBri.collisions,
										'factors': Intersection.HighTunBri.factors
									}
								})

	return {num, info}

def TotalInjure(self, level, name, timeStart, timeEnd):
	num = 0
	info = {}
	if(level == "Borough"):
		for n in name:
			for Year, Month, Intersection in self.data.Borough_Dict[name]:
				num = num + self.data.Borough_Dict[name].Intersection.collisions.PersonsInjured
				info.append({	'city': NYC.Borough_Dict[name],
								'Year': Year, 
								'Month': Month,
								'Intersection': {
									'collisions': Intersection.collisions,
									'factors': Intersection.factors},
									'HighTunBri':{
										'collisions': Intersection.HighTunBri.collisions,
										'factors': Intersection.HighTunBri.factors
									}
								})


	return {num, info}

def TotalKill(path):

	return count

def TotalInjure(path):


	return count

