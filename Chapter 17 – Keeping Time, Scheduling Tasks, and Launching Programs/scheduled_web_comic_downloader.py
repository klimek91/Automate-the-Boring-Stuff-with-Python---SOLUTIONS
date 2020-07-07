import requests, bs4, os

os.makedirs('comic', exist_ok=True)
headers = {'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

url = 'http://www.lefthandedtoons.com/'
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'lxml')
imgEl = soup.select(".comicimage")
imgUrl = imgEl[0].attrs['src']
imgName = os.path.basename(imgUrl)

resImg = requests.get(imgUrl, headers=headers)
resImg.raise_for_status()
img = open(os.path.join('comic', imgName), 'wb')
for chunk in resImg.iter_content(100000):
    img.write(chunk)
img.close()

prevEl = soup.select(".prev a")
prevUrl = url + (prevEl[0].attrs['href'].replace('/',''))
print(prevUrl)