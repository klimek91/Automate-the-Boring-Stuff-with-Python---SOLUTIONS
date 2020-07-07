import requests, bs4, os

os.makedirs('comic', exist_ok=True)
headers = {'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

url = 'http://www.lefthandedtoons.com/'
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'lxml')

prevEl = soup.select(".prev a")
prevId = prevEl[0].attrs['href'].replace('/','')
prevUrl = url + prevId
mainUrl = str(int(prevId) + 1)

while True:
    resImg = requests.get(url + mainUrl, headers=headers)
    resImg.raise_for_status()
    soup = bs4.BeautifulSoup(resImg.text, 'lxml')
    imgEl = soup.select(".comicimage")
    imgUrl = imgEl[0].attrs['src']
    imgName = os.path.basename(imgUrl)
    if not os.path.exists(os.path.join('comic',imgName)):
        print("Downloading {}..".format(imgName))
        img = open(os.path.join('comic', imgName), 'wb')
        for chunk in resImg.iter_content(100000):
            img.write(chunk)
        img.close()
        mainUrl = str(int(mainUrl) - 1)
    else:
        print("Database is updated")
        break