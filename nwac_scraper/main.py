##nwac observation scraper
import requests
import bs4
from ObservationParser import *
import time
from CosmosHelper import *

def main():
	
	##todo: consider moving this to observation parser or another file
	url = "https://nwac.us/observations/?season=2021&search="
	page = requests.get(url)

	soup = bs4.BeautifulSoup(page.content, 'lxml')
	table = soup.find(name='table', attrs={'id':'observations'})

	rows = table.tbody.findAll('tr')
	
	#the date and location strings for an observation are used to form the unique id used to form the url w/ the report details
	#this is also important b/c need unique ID for db
	#if 2+ observations share a date and location, suffix is added to id of newer report
	#ex: "nwac.us/public-obs/12345678-location-name", "nwac.us/public-obs/12345678-location-name-2"
	#if multiple reports share a date/location, this dict. will count up how many so proper suffixes can be applied to the obs.id which is used to form the report url
	multiples = {}

	#table is in descending order by date 
	#need to compare w/ previous to see if date/location are same b/c it means id suffix needed
	prev_id = ""

	observations = []

	cosmos = CosmosHelper()

	for i in range(0, (len(rows) - 1)):
		
		row = rows[i].findAll('td')
		observation = parse_table_row(row)

		if (observation.id == prev_id):
			if (observation.id in multiples):
				multiples[observation.id] += 1
			else:
				#start at 2 b/c url suffix for multiples starts at 2
				multiples[observation.id] = 2

		prev_id = observation.id
		observations.append(observation)

	for observation in observations:

		id_val = observation.id

		if((id_val in multiples) and (multiples[id_val] > 1)):
			observation.id = id_val + "-" + str(multiples[id_val])
			multiples[id_val] -= 1

		observation = set_report_details(observation)
		cosmos.create_item(observation)


if __name__ == "__main__":
	main()


