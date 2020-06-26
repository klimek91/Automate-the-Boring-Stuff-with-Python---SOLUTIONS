#!python

import requests, bs4, webbrowser, sys

if len(sys.argv) > 1:
    searched = '+'.join(sys.argv[1:])

    link = "https://www.google.pl/search?&q=" + searched

    headers = {'User-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

    res = requests.get(link, headers=headers)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'lxml')
    linkEl = soup.select(".r > a[href]")

    for i in range(3):
        webbrowser.open(linkEl[i].attrs['href'])
