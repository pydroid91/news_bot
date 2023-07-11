from bs4 import BeautifulSoup
import requests

PANORAMA_LINKS = []
PANORAMA_HEADINGS = []

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'}

def parse_panorama():
    url = 'https://panorama.pub/'
    src = requests.get(url=url, headers=headers).text
    soup = BeautifulSoup(src, 'lxml')

    ul = soup.find_all('ul', class_='mt-4')[0]
    for li in ul.find_all('li')[:5]:

        link = li.find('a', class_='flex flex-row flex-nowrap mb-4 rounded-md hover:text-secondary hover:bg-accent/[.1]').get('href')
        PANORAMA_LINKS.append('https://panorama.pub' + link)

        heading = li.find('div', class_='pl-2 pr-1 text-sm basis-auto self-center').find('div').text
        PANORAMA_HEADINGS.append(heading)

    return PANORAMA_HEADINGS, PANORAMA_LINKS
