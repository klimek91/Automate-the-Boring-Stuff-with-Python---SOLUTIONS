#!python

import requests, bs4, os
os.makedirs('xkcd', exist_ok=True)
headers = {'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

url = "https://xkcd.com/"

while not url.endswith('/2300/'): #downloading only few images (You can change to url.endswith('#') to download all comics
    res = requests.get(url, headers=headers)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'lxml')
    imgEl = soup.select('#comic >img')
    img = imgEl[0].attrs['src']
    imgUrl = "https:" + img

    resIm = requests.get(imgUrl, headers=headers)
    resIm.raise_for_status()
    imgName = os.path.basename(img)

    print("Downloading {} ..".format(imgName))
    file = open(os.path.join('xkcd',imgName), 'wb')
    for chunk in resIm.iter_content(100000):
        file.write(chunk)
    file.close()

    prevEl = soup.select('a[rel = "prev"]')
    prevButton = prevEl[0].attrs['href']
    url = 'https://xkcd.com/' + prevButton

else:
    print("Comics database is updated")






