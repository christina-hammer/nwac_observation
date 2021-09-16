##nwac observation scraper
import requests
import bs4
from ObservationParser import *


def main():
	
	rows = get_observation_table_rows
	
	for i in range(0, 4):
		row = rows[i].findAll('td')
		
		obs = parse_table_row(row)
		obs.print()

def get_observation_table_rows():
	url = "https://nwac.us/observations/?season=2021&search="
	page = requests.get(url)

	soup = bs4.BeautifulSoup(page.content, 'lxml')
	table = soup.find(name='table', attrs={'id':'observations'})

	rows = table.tbody.findAll('tr')
	return rows

##TODO: finish this method
def get_report(report_url):
	report_url = "https://nwac.us/public-obs/" + report_path

	report_page = requests.get(report_url)
	##get report details


if __name__ == "__main__":
	main()


