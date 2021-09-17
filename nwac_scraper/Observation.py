#Observation class

class Observation:

	def __init__(self, date, observer_type, region, latitude, longitude, location_name, avalanche, signs_of_instability, report_path):
		self.date = date
		self.observer_type = observer_type
		self.region = region
		self.latitude = latitude
		self.longitude = longitude
		self.location_name = location_name
		self.avalanche_reported = avalanche
		self.signs_of_instability_reported = signs_of_instability
		self.report_path = report_path

		self.avalanches = []
		self.signs_of_instability = None
		self.notes = ""

	def print(self):
		print("Date: " + self.date)
		print("Obs Type: " + self.observer_type)
		print("Region: " + self.region)
		print("Latitude: " + str(self.latitude))
		print("Longitude: " + str(self.longitude))
		print("Location: " + self.location_name)
		print("Avalanche?: " + self.avalanche_reported)
		print("Signs of instability?: " + self.signs_of_instability_reported)
		print("report_path: " + self.report_path)
		
		if (len(self.avalanches) > 0):
			print("Avalanches: ")
			for a in self.avalanches:
				a.print()

		if(self.signs_of_instability != None):
			print("Signs of instability: ")
			self.signs_of_instability.print()

		print("Notes: " + self.notes)


class SignsOfInstability:

	def __init__(self):
		self.shooting_cracks = ""
		self.collapsing_or_whumpfing = ""

	def print(self):
		print("Shooting cracks? " + self.shooting_cracks)
		print("Collapsing or whumpfing? " + self.collapsing_or_whumpfing)

class Avalanche:

	def __init__(self):
		self.size = ""
		self.type = ""
		self.intentional = ""
		self.elevation = ""
		self.aspect = ""
		self.comments = ""
		self.cause = ""

	def print(self):
		print("Size " + self.size)
		print("Type: " + self.type)
		print("Intentional: " + self.intentional)
		print("Elevation: " + self.elevation)
		print("Aspect: " + self.aspect)
		print("Comments: " + self.comments)
		print("Cause: " + self.cause)

