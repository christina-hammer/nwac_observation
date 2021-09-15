##nwac observation scraper
import requests
import bs4

url = "https://nwac.us/observations/?season=2021&search="
page = requests.get(url)

soup = bs4.BeautifulSoup(page.content, 'lxml')
table = soup.find(name='table', attrs={'id':'observations'})

print(table)