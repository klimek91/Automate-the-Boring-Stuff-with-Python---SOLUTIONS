#!python

import requests, bs4, os
os.makedirs('xkcd', exist_ok=True)

headers = {'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

res = requests.get("https://xkcd.com/", headers=headers)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'lxml')
imgEl = soup.select('#comic >img')
img = imgEl[0].attrs['src']
imgUrl = "https:" + img

res = requests.get(imgUrl, headers=headers)
res.raise_for_status()
imgName = os.path.basename(img)

file = open(os.path.join('xkcd',imgName), 'wb')
for chunk in res.iter_content(100000):
    file.write(chunk)
file.close()