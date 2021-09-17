from geopy.geocoders import Nominatim
from Observation import *
import requests
import bs4
from string import punctuation

geolocator = Nominatim(user_agent="nwac_observations")

##will only search for locations in WA or Oregon
##Note - all oregon observations will be in Mt. Hood zone
geocodeWA = lambda query: geolocator.geocode("%s WA" % query)
geocodeOR = lambda query: geolocator.geocode("%s OR" % query)


def parse_table_row(td_list):
	
	date = td_list[0].text[1:9]
	observer_type = td_list[1].text
	region = td_list[2].text
	location_name = td_list[3].text
	avalanche_reported = td_list[4].text.lower()
	signs_of_instability_reported = td_list[5].text.lower()

	if (avalanche_reported != "yes"):
		avalanche_reported = "no"

	if (signs_of_instability_reported != "yes"):
		signs_of_instability_reported = "no"

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

	report_path = get_report_path(location_name, date)

	observation = Observation(date, observer_type, region, latitude, longitude, location_name, avalanche_reported, signs_of_instability_reported, report_path)
	
	return observation

#forms end of url to get full observation report
#TODO: for duplicate location and dates, url adds number on the end
def get_report_path(location_name, date):
	report_path = date + "_"

	#strip trailing and leading whitespaces and punctuation (ex: Denny Mt. =should be=> Denny Mt)
	location_name = location_name.strip(punctuation).strip()

	#all non-leading, non-trailing whitespaces/punctuation should be - char
	#TODO: consider using a more compact/readble way to do this instead of the multiple replace statements
	location_name = location_name.lower().replace(" ", "-").replace(".", "-").replace("/","-")
	location_name = location_name.replace("(", "").replace(")", "")

	return report_path + location_name

#uses url path from date and location to get avalanche/soi details (if any) and observation notes
def get_report_details(observation):

	url = "https://nwac.us/public-obs/" + observation.report_path
	page = requests.get(url)

	soup = bs4.BeautifulSoup(page.text, "lxml")
	divs = soup.find_all('div')

	#There is only one section for each of these even if multiple triggered or observed avalanches occurred
	avalanche = None
	for d in divs:

		#this removes whitespaces/newlines/tabs
		field = ' '.join(d.get_text().split())

		#for the observation notes, will always be under the 'observations' header
		if("Observations" in field[0:12]):
			observation.notes = field[12:]
		elif("Triggered Avalanches" in field):
			avalanche = Avalanche()
			avalanche.cause = "triggered"
		elif("Observed Avalanches" in field):
			avalanche = Avalanche()
			avalanche.cause = "observed"
			avalanche.intentional = "No"
		else:
			#for most text lines will end up with observation report field in kv pair
			field_pair = field.split(": ", 1)

			if (len(field_pair) < 2):
				#some field titles have question mark insead of color (ex: Did you trigger the avalanche? Yes)
				field_pair = field_pair[0].split("? ")

			#last field for each avalanche (if any) is "comments"
			if ("Comments" in field_pair[0]):
				if(len(field_pair) > 1):
					avalanche.comments = field_pair[1]
				observation.avalanches.append(avalanche)
			elif (len(field_pair) > 1):
				if("cracks" in field):
					observation.signs_of_instability = SignsOfInstability()
					observation.signs_of_instability.shooting_cracks = field_pair[1]
				elif("collapsing" in field_pair[0]):
					observation.signs_of_instability.collapsing_or_whumpfing = field_pair[1]
				else:
					avalanche = assign_avalanche_value(field_pair[0], field_pair[1], avalanche)
			
	return observation

def assign_avalanche_value(key, val, avalanche):
	key = key.lower()
	if("type" in key):
		avalanche.type = val
	elif("size" in key):
		avalanche.size = val
	elif("intentional" in key):
		avalanche.intentional = val
	elif("elevation" in key):
 		avalanche.elevation = val
	elif("aspect" in key):
 		avalanche.aspect = val
	return avalanche



