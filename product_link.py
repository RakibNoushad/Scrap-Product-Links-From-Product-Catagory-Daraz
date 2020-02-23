import json
import requests
import time
import pandas as pd
from bs4 import BeautifulSoup


def get_page(url):
    response = requests.get(url)

    if not response.ok:
        print('Server responded:', response.status_code)
    else:
        soup = BeautifulSoup(response.text, 'lxml')
    return soup


def get_detail_data(soup):
    try:
        title = soup.find_all('script', {'type': 'application/ld+json'})
            #.join(str(soup.find('script')).split("\n"))
    except:
        title = ''

    try:
        pass
    except:
        pass
    f = open("link.txt", "a", encoding='utf-8')
    #f.write(headers+"\n")

    json_obj = json.loads(title[1].text)

    link_access = json_obj['itemListElement']
    for link_data in link_access:
        url = link_data['url']

        f.write(url+"\n")


def main():
    with open('typeLink.txt', 'r') as g:
        for line in g:
            try:
                url = g.readline()
                get_detail_data(get_page(url))
                time.sleep(3)
            except:
                print("Problem in url")

    #url = 'https://www.daraz.com.bd/smartphones/helio/?rating=1'

    #get_detail_data(get_page(url))


if __name__ == '__main__':
    main()