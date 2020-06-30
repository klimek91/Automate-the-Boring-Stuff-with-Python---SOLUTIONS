import requests, bs4, os

#category = input("Please enter Your category ")
#link = "https://imgur.com/search/score?q={}".format(category)
test = "https://imgur.com/search/score?q=football"
headers = {'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

res = requests.get(test, headers=headers)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'lxml')
postEl = soup.select('.image-list-link img')
img = postEl[0].attrs['src']
imgName = os.path.basename(img)
imgUrl = "https:" + img
