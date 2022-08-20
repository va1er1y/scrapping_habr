import requests
import bs4
from pprint import  pprint

KEYWORDS = {'Читальный зал', 'Блог компании Журнал Хакер'}
def request(reference):
    HEADERS = {
        'Cookie': '_ym_uid=1639148487334283574; _ym_d=1639149414; _ga=GA1.2.528119004.1639149415; _gid=GA1.2.512914915.1639149415; habr_web_home=ARTICLES_LIST_ALL; hl=ru; fl=ru; _ym_isad=2; __gads=ID=87f529752d2e0de1-221b467103cd00b7:T=1639149409:S=ALNI_MYKvHcaV4SWfZmCb3_wXDx2olu6kw',
        'Accept-Language': 'ru-RU,ru;q=0.9',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Cache-Control': 'max-age=0',
        'If-None-Match': 'W/"37433-+qZyNZhUgblOQJvD5vdmtE4BN6w"',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
        'sec-ch-ua-mobile': '?0'}
    response = requests.get(reference, headers=HEADERS)
    return response.text

def maintance_habre_news():
    list_tema = set()
    urls = []
    answer_habr = request('https://habr.com/ru/all/')
    soup = bs4.BeautifulSoup(answer_habr, features='html.parser')
    head_titles = soup.find_all(class_='tm-article-snippet')
    for art in head_titles:
        list_tema.clear()
        tema = art.find_all(class_='tm-article-snippet__hubs-item')
        for i in tema:
            list_tema.add(i.find('a').text.strip())
        if list_tema & KEYWORDS:
            art_tag = art.find('h2').find('a')
            href = art_tag.attrs['href']
            url = 'https://habr.com' + href
            urls.append(url)
            print(art_tag.text, '--', url)
            print("----")
    return (urls)

def open_news(urls):
    for i in urls:
        answer_habr = request(i)
        soup = bs4.BeautifulSoup(answer_habr, features='html.parser')
        text_news = soup.find(class_='tm-article-presenter__content tm-article-presenter__content_narrow')
        news = (str(text_news.text).split('\n'))
        news = news[2:-1]
        print()
        print("_________________________________")
        pprint(news)
      


open_news(maintance_habre_news())
