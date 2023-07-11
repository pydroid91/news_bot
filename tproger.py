from bs4 import BeautifulSoup
import requests

TPROGER_links = []
TPROGER_headings = []

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'}

def parse_articles():

    url = 'https://tproger.ru/articles/'
    src = requests.get(url=url, headers=headers).text
    soup = BeautifulSoup(src, 'lxml')

    for article in soup.find_all('div', class_='article__main')[:5]:

        a = article.find('a', class_='article__link')

        heading = a.text.replace('\n', '')
        TPROGER_headings.append(heading)
        link = a.get('href')
        TPROGER_links.append(link)

    return TPROGER_headings, TPROGER_links
