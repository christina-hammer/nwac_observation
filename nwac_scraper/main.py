##nwac observation scraper
import requests
import bs4
from ObservationParser import *


def main():
	
	##todo: consider moving this to observation parser or another file
	url = "https://nwac.us/observations/?season=2021&search="
	page = requests.get(url)

	soup = bs4.BeautifulSoup(page.content, 'lxml')
	table = soup.find(name='table', attrs={'id':'observations'})

	rows = table.tbody.findAll('tr')
	
	##TODO: instead of looping through and parsing twice, save the parsed table rows!!
	report_path_multiples = get_report_path_multiples(rows)

	for i in range(100, (len(rows) - 1)):
		
		row = rows[i].findAll('td')
		obs = parse_table_row(row)

		#duplicate check
		##update report path

		#step to add lat long 
		obs = get_report_details(obs)

		#obs.print()

def 


##check function naming convention
def get_report_path_multiples(rows):

	multiples = {}
	prev_report_path = ""

	for i in range(0, (len(rows) - 1)):
		
		row = rows[i].findAll('td')
		obs = parse_table_row(row)

		if (obs.report_path == prev_report_path):
			if (obs.report_path in multiples):
				multiples[obs.report_path]++
			else:
				multiples[obs.report_path] = 2

		prev_report_path = obs.report_path

	return multiples


if __name__ == "__main__":
	main()


