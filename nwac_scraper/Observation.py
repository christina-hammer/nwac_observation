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
		self.signs_of_instability = SignsOfInstability()
		self.comments = ""

	def print(self):
		print("Date: " + self.date)
		print("Obs Type: " + self.observer_type)
		print("Region: " + self.region)
		print("Latitude: " + str(self.latitude))
		print("Longitude: " + str(self.longitude))
		print("Location: " + self.location_name)
		print("Avalanche?: " + self.avalanche)
		print("Signs of instability?: " + self.signs_of_instability)
		print("report_path: " + self.report_path)
		print("")


class SignsOfInstability:

	def __init__(self):
		self.shooting_cracks = ""
		self.collapsing_or_whumpfing = ""

class Avalanche:

	def __init__(self):
		self.severity = 0
		self.type = ""
		self.intentional = ""
		self.elevation = ""
		self.aspect = ""
		self.comments = ""
		self.cause = ""

