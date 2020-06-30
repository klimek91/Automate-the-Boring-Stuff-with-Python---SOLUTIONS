import requests, bs4, os

os.makedirs("images", exist_ok=True)
category = input("Please enter Your category ")
link = "https://imgur.com/search/score?q={}+image".format(category)

headers = {'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
res = requests.get(link, headers=headers)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'lxml')
postEl = soup.select('.image-list-link img')
for i in range(10): #downloading first 10 images
    img = postEl[i].attrs['src']
    imgUrl = "https:" + img
    imgName = os.path.basename(imgUrl)

    res = requests.get(imgUrl, headers=headers)
    res.raise_for_status()

    if not os.path.exists(os.path.join("images", imgName)):
        print("Downloading {} .. ".format(imgName))
        file = open(os.path.join("images", imgName), 'wb')
        for chunk in res.iter_content(100000):
            file.write(chunk)
        file.close()