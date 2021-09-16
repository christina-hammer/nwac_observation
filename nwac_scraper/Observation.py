#Observation class

class Observation:

	def __init__(self, date, observer_type, region, latitude, longitude, location_name, avalanche, signs_of_instability, report_url):
		self.date = date
		self.observer_type = observer_type
		self.region = region
		self.latitude = latitude
		self.longitude = longitude
		self.location_name = location_name
		self.avalanche = avalanche
		self.signs_of_instability = signs_of_instability
		self.report_path = report_path

		self.get_report()

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



