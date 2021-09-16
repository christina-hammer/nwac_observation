##nwac observation scraper
import requests
import bs4
from ObservationParser import *


def main():
	
	rows = get_observation_table_rows()
	
	for i in range(0, 4):
		row = rows[i].findAll('td')
		
		obs = parse_table_row(row)
		obs.print()

def get_observation_table_rows():
	page = fetch_page("https://nwac.us/observations/?season=2021&search=")

	table = page.find(name='table', attrs={'id':'observations'})

	rows = table.tbody.findAll('tr')
	return rows

##TODO: finish this method
def get_report(report_url, observation):
	
	report_page = fetch_page("https://nwac.us/public-obs/" + report_path)
	if (report_page != None):
		observedAvalanches = report_page.find()

	return observation

	


	##get report details

def fetch_page(url):
	url = "https://nwac.us/observations/?season=2021&search="
	page = requests.get(url)

	soup = None
	if (report_page.status_code < 300):
		soup = bs4.BeautifulSoup(report_page.content, 'lxml')

	return soup;

if __name__ == "__main__":
	main()


