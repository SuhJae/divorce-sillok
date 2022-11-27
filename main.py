import requests
from bs4 import BeautifulSoup as bs
import time

with open('result.txt') as f:
    # print each line
    for line in f:
        url = line.split('^')[4].replace('http://', 'https://').replace('\n', '')
        if url.startswith('https://'):
            print(url)
            response = requests.get(url)

            soup = bs(response.text, 'html.parser')
            paragraph = soup.find('div', {'class': 'ins_view_pd'})
            paragraph = paragraph.find_all('p', {'class': 'paragraph'})

            for p in paragraph:
                print(p.text)

            time.sleep(5)
            print('')
