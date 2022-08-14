import requests
import bs4
from pprint import  pprint

KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'Компьютерное железо']
def request(reference):
    response = requests.get(reference)
    return response.text

def maintance_habre_news():
    list_tema =[]
    urls = []
    answer_habr = request('https://habr.com/ru/all/')
    soup = bs4.BeautifulSoup(answer_habr, features='html.parser')
    head_titles = soup.find_all(class_='tm-article-snippet')
    for art in head_titles:
        tema = art.find_all(class_='tm-article-snippet__hubs-item')
        for i in tema:
            list_tema.append(i.find('a').text.strip())
        if set(list_tema) & set(KEYWORDS):
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
        text_news = soup.find(class_='article-formatted-body article-formatted-body article-formatted-body_version-1')
        news = (str(text_news.text).split("\r\n"))
        pprint(news)

open_news(maintance_habre_news())

