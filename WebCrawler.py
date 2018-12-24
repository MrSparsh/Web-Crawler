from urllib.request import *
from bs4 import BeautifulSoup


def spider():
    url = "https://store.steampowered.com/genre/Free%20to%20Play/#p=0&tab=TopSellers"
    source_code = urlopen(url)
    page_html = source_code.read()
    soup = BeautifulSoup(page_html, 'html.parser')
    for content_div in soup.findAll('div', {'class': 'tab_item_content'}):
        name_div = content_div.find('div', {'class': 'tab_item_name'})
        tags_div = content_div.find('div', {'class': 'tab_item_top_tags'})
        print('Game Name : '+name_div.string)
        print('Game Tags : ', end="")
        for span in tags_div.findAll('span'):
            print(span.string, end="")
        print('\n')


spider()
