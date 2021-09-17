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
	
	for i in range(12, 16):
		row = rows[i].findAll('td')
		
		obs = parse_table_row(row)

		obs = get_report_details(obs)

		obs.print()

if __name__ == "__main__":
	main()


