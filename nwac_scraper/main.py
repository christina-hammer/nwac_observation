##nwac observation scraper
import requests
import bs4
from geopy.geocoders import Nominatim


def main():
	url = "https://nwac.us/observations/?season=2021&search="
	page = requests.get(url)

	soup = bs4.BeautifulSoup(page.content, 'lxml')
	table = soup.find(name='table', attrs={'id':'observations'})

	rows = table.tbody.findAll('tr')

	geolocator = Nominatim(user_agent="nwac_observations")
	##will only search for locations in WA or Oregon
	##all oregon observations will be in Mt. Hood zone
	geocodeWA = lambda query: geolocator.geocode("%s WA" % query)
	geocodeOR = lambda query: geolocator.geocode("%s OR" % query)


	for i in range(0, 4):
		for td in rows[i].findAll('td'):
			print(td.text)

if __name__ == "main":
	main()


