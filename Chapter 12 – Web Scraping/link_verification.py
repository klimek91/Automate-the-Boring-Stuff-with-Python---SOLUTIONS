import requests, bs4

headers = {'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

url = input("Enter URL to verify links in it: ")
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'lxml')
links = soup.select('a')


to_check = []

for link in links:
    url = link['href']
    if url.startswith('http'):
        to_check.append(url)
    elif url.startswith('//'):
        to_check.append('https:' + url)

good_links = []
bad_links = []

for link in to_check:
    result = requests.get(link)
    if result.status_code == 404:
        bad_links.append(link)
    else:
        good_links.append(link)