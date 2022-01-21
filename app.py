import requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/chart/top/'
headers = {"Accept-Language": "en-US,en;q=0.5"}
r = requests.get(url, headers = headers)
soup = BeautifulSoup(r.text, 'html.parser')
data = soup.find("tbody", {"class" : "lister-list"})
data = data.find_all("tr")
for number in data: 
  content = number.find("td", {"class" : "titleColumn"}).text
  content = content.replace("\n", "")
  casts = number.find("td", {"class" : "titleColumn"}).find('a').get('title')
  casts = casts.replace(" (dir.)", "")
  imdb_rating = number.find("td", {"class" : "ratingColumn"}).text
  imdb_rating = imdb_rating.replace("\n", "")
  print("\n" + content + " ---------- " + imdb_rating + " ---------- " + casts)
  