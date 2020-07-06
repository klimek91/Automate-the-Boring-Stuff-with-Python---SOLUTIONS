import os, requests, bs4

os.makedirs('xkcd', exist_ok=True)
headers = {'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

url = "https://xkcd.com/"

res = requests.get(url, headers=headers)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'lxml')
imgEl = soup.select('#comic img')

imgUrl = 'https:' + imgEl[0].attrs['src']
imgName = os.path.basename(imgUrl)

resImg = requests.get(imgUrl, headers=headers)
resImg.raise_for_status()
imgFile = open(os.path.join('xkcd', imgName), 'wb')
for chunk in resImg.iter_content(100000):
    imgFile.write(chunk)
imgFile.close()