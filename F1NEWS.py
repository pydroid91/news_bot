from bs4 import BeautifulSoup
import requests

F1NEWS_headings = []
F1NEWS_links = []

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'}

def parse_news():
    url = 'https://www.f1news.ru/'
    src = requests.get(url=url, headers=headers).text
    soup = BeautifulSoup(src, 'lxml')

    for news in soup.find_all('a', class_='b-news-list__title')[:5]:

        F1NEWS_headings.append(news.text)
        link = news.get('href')

        if 'https://www.f1news.ru/' not in link:
            F1NEWS_links.append('https://www.f1news.ru' + link)
        else:
            F1NEWS_links.append(link)

    return F1NEWS_headings, F1NEWS_links
