#Observation class
import json

class Observation:
	##TODO: Add comments describing aattributes 
	def __init__(self, date, observer_type, region, location_name, avalanche, signs_of_instability, id_val):
		self.date = date
		self.observer_type = observer_type
		self.region = region
		self.location_name = location_name
		self.avalanche_reported = avalanche
		self.signs_of_instability_reported = signs_of_instability
		self.id = id_val

		self.latitude = 0
		self.longitude = 0
		self.avalanches = []
		self.signs_of_instability = None
		self.notes = ""

	def to_string(self):
		s = "Date: " + self.date + "\n"
		s = s + "Obs Type: " + self.observer_type + "\n"
		s = s + "Region: " + self.region + "\n"
		s = s + "Latitude: " + str(self.latitude) + "\n"
		s = s + "Longitude: " + str(self.longitude) + "\n"
		s = s + "Location: " + self.location_name + "\n"
		s = s + "Avalanche?: " + self.avalanche_reported + "\n"
		s = s + "Signs of instability?: " + self.signs_of_instability_reported + "\n"
		s = s + "id: " + self.id + "\n"
		
		if (len(self.avalanches) > 0):
			s = s + "Avalanches: " + "\n"
			for a in self.avalanches:
				s = s + a.to_string()

		if(self.signs_of_instability != None):
			s = s + "Signs of instability: " + "\n"
			s = s + self.signs_of_instability.to_string()

		s = s + "Notes: " + self.notes + "\n"

		return s

	def toJson(self):
		return dict(id=self.id, observation_type="self.observation_type", region="self.region", latitude=self.latitutde, longitude=self.longitude, avalanche_reported=self.avalanche_reported, signs_of_instability_reported=self.signs_of_instability_reported, avalanches=self.avalanches, signs_of_instability=self.signs_of_instability, notes=self.notes)
 

	def __eq__(self, observation):
		if (not isinstance(observation, Observation)): return False
		if (self.date != observation.date): return False
		if (self.observer_type != observation.observer_type): return False
		if (self.region != observation.region): return False
		if (self.latitude != observation.latitude): return False
		if (self.longitude != observation.longitude): return False
		if (self.location_name != observation.location_name): return False
		if (self.avalanche_reported != observation.avalanche_reported): return False
		if (self.signs_of_instability_reported != observation.signs_of_instability_reported): return False
		if (self.id != observation.id): return False
		if (self.notes != observation.notes): return False
		if (self.signs_of_instability != observation.signs_of_instability): return False

		if (len(self.avalanches) != len(observation.avalanches)): return False
		
		for i in range(0, len(self.avalanches)):
			if (not (self.avalanches[i] == observation.avalanches[i])): return False

		return True

class SignsOfInstability:

	def __init__(self):
		self.shooting_cracks = ""
		self.collapsing_or_whumpfing = ""

	def to_string(self):
		s = "Shooting cracks? " + self.shooting_cracks + "\n"
		s = s + "Collapsing or whumpfing? " + self.collapsing_or_whumpfing + "\n"
		return s

	def __eq__(self, soi):
		if(not isinstance(soi, SignsOfInstability)): return False
		if (self.shooting_cracks != soi.shooting_cracks): return False
		if (self.collapsing_or_whumpfing != soi.collapsing_or_whumpfing): return False

		return True

	def toJson(self):
		return dict(shooting_cracks=self.shooting_cracks, collapsing_or_whumpfing=self.collapsing_or_whumpfing)

class Avalanche:

	def __init__(self):
		self.size = ""
		self.type = ""
		self.intentional = ""
		self.elevation = ""
		self.aspect = ""
		self.comments = ""
		self.cause = ""

	def to_string(self):
		s = "Size " + self.size + "\n"
		s = s + "Type: " + self.type + "\n"
		s = s + "Intentional: " + self.intentional + "\n"
		s = s + "Elevation: " + self.elevation + "\n"
		s = s + "Aspect: " + self.aspect + "\n"
		s = s + "Comments: " + self.comments + "\n"
		s = s + "Cause: " + self.cause + "\n"

		return s

	def __eq__(self, avalanche):
		if(not isinstance(avalanche, Avalanche)): return False
		if (self.size != avalanche.size): return False
		if (self.type != avalanche.type): return False
		if (self.intentional != avalanche.intentional): return False
		if (self.elevation != avalanche.elevation): return False
		if (self.aspect != avalanche.aspect): return False
		if (self.comments != avalanche.comments): return False
		if (self.cause != avalanche.cause): return False

		return True


	def toJson(self):
		return dict(size=self.size, type=self.type, intentional=self.intentional, elevation=self.elevation, aspect=self.aspect, comments=self.comments, cause=self.cause)

