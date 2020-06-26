import requests, bs4

#link = "https://www.google.pl/search?&q=adam+malysz"

res = requests.get(link)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'lxml')
print(soup)
linkEl = soup.select('')
