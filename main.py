import requests
from bs4 import BeautifulSoup as bs
from multiprocessing.pool import ThreadPool as Executor
import re

keyword = "미친"
MAX_WORKERS = 100

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

def get_sillok(url):
    try:
        response = requests.get(url)

        soup = bs(response.text, 'html.parser')
        soup.sup.clear()
        paragraph = soup.find('div', {'class': 'ins_view_pd'})
        paragraph = paragraph.find_all('p', {'class': 'paragraph'})

        final = ''
        for p in paragraph:
            final += p.text

        final = final.replace('              ', ' ').replace('        ', ' ').replace('  ', ' ')

        # python remove characters inside brackets
        final = re.sub(r'\([^)]*\)', '', final)
        final = re.sub(r'\[[^)]*\]', '', final)
        prev = ''

        for sentence in final.split('. '):
            if keyword in sentence:

                if prev != '':
                    longer = f'{prev}. {sentence}.'
                else:
                    longer = sentence

                if longer == '':
                    continue
                elif len(longer.encode("UTF-8")) <= 280:
                    print(longer.replace(keyword, BC.BOLD + BC.OKGREEN + keyword + BC.RESET))
                    break

                elif len(sentence.encode("UTF-8")) <= 280:
                    print(sentence.replace(keyword, BC.BOLD + BC.OKGREEN + keyword + BC.RESET) + '.')
                    break
            prev = sentence
    except:
        pass



if __name__ == "__main__":
    with open('result.txt') as f:
        urls = []
        for line in f:
            url = line.split('^')[4].replace('http://', 'https://').replace('\n', '')
            if url.startswith('https://'):
                urls.append(url)

        pool_size = min(len(urls), MAX_WORKERS)
        with Executor(pool_size) as executor:
            executor.map(get_sillok, urls)

    print(f'{BC.OKGREEN}Done.{BC.RESET}')