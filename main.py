import requests
from bs4 import BeautifulSoup as bs
import time

with open('result.txt') as f:
    # print each line
    for line in f:
        url = line.split('^')[4].replace('http://', 'https://')
        if url.startswith('http'):
            print(url)
            response = requests.get(url)
            soup = bs(response.text, 'html.parser')
            paragraph = soup.find_all('p', {'class': 'paragraph'})

            print(paragraph)
            # print(paragraph.text.replace('              ', ' '))
            time.sleep(1)

