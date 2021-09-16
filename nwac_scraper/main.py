##nwac observation scraper
import requests
import bs4
from ObservationParser import *


def main():
	
	url = "https://nwac.us/observations/?season=2021&search="
	page = requests.get(url)

	soup = bs4.BeautifulSoup(page.content, 'lxml')

	table = soup.find(name='table', attrs={'id':'observations'})

	rows = table.tbody.findAll('tr')
	
	for i in range(0, 1):
		row = rows[i].findAll('td')
		
		obs = parse_table_row(row)
		##obs = get_report(obs)
		obs.print()

##TODO: finish this method
def get_report(observation):

	page = requests.get("https://nwac.us/public-obs/" + observation.report_path)
	soup = bs4.BeautifulSoup(page.text, "lxml")

	print(soup)

	return observation

	

def fetch_page(url):
	

	return soup;

if __name__ == "__main__":
	main()


