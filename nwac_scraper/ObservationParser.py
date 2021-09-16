from geopy.geocoders import Nominatim
from Observation import *

geolocator = Nominatim(user_agent="nwac_observations")

##will only search for locations in WA or Oregon
##Note - all oregon observations will be in Mt. Hood zone
geocodeWA = lambda query: geolocator.geocode("%s WA" % query)
geocodeOR = lambda query: geolocator.geocode("%s OR" % query)


def parse_table_row(td_list):
	
	date = td_list[0].text[0:9]
	observer_type = td_list[1].text
	region = td_list[2].text
	location_name = td_list[3].text
	avalanche = td_list[4].text.lower()
	signs_of_instability = td_list[5].text.lower()

	if (avalanche != "yes"):
		avalanche = "no"

	if (signs_of_instability != "yes"):
		signs_of_instability = "no"

	latitude = 0
	longitude = 0
	location = None
	if (region == "Mt Hood" or (region == "Other" and ("Oregon" in location_name.lower() or ", OR" in location_name.lower()))):
		location = geocodeOR(location_name)
	else:
		location = geocodeWA(location_name)
		

	if (location is not None):
		latitude = location.latitude
		longitude = location.longitude

	report_path = date + "_" + location_name.lower().replace(" ", "-")

	observation = Observation(date, observer_type, region, latitude, longitude, location_name, avalanche, signs_of_instability, report_path)
	
	return observation





