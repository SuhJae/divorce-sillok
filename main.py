import requests
from bs4 import BeautifulSoup as bs

keyword = "이혼"

class BC:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'


with open('result.txt') as f:



    # print each line
    for line in f:
        url = line.split('^')[4].replace('http://', 'https://').replace('\n', '')
        if url.startswith('https://'):

            response = requests.get(url)

            soup = bs(response.text, 'html.parser')
            paragraph = soup.find('div', {'class': 'ins_view_pd'})
            paragraph = paragraph.find_all('p', {'class': 'paragraph'})

            final = ''
            for p in paragraph:
                final += p.text

            final = final.replace('              ', ' ')

            for sentence in (final.split('. ')):
                if keyword in sentence:
                    print(url)
                    print(sentence.replace(keyword, BC.BOLD + BC.OKGREEN + keyword + BC.RESET))
                    print('')
                    break
