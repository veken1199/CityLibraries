import json, requests
from lxml import html
from bs4 import BeautifulSoup
import html5lib

url_concordia = 'http://encore.concordia.ca/iii/encore/plus/C__S{}__Orightresult__U?lang=eng&suite=def&size=40'

xpath_title_first = '//*[@id="recordDisplayLink2Component"]/text()'
xpath_author_first = '//*[@id="authorDisplayLinkComponent"]/text()'

xpath_title = '//*[@id="recordDisplayLink2Component_{}"]'
xpath_author = '//*[@id="authorDisplayLinkComponent_{}"]/text()'

xpath_author_no_link = 'div[2]/div/div[1]/text()'


def crawl(keyword, resutls):
    page = requests.get(url_concordia.format(keyword))

    html_tree = html.fromstring(page.content)
    parsed_html_tree = html_tree.xpath('//*[@id="mainContentArea"]')

    data = []

    # getting the first element
    if len(parsed_html_tree[0]):
        data.append({
            'title': ''.join((parsed_html_tree[0][0].xpath(xpath_title_first))).strip(),
            'author': ''.join((parsed_html_tree[0][0].xpath(xpath_author_first))).strip()
        })

    # getting the rest of the element
    for i in range(1, len(parsed_html_tree[0])):
        if len(parsed_html_tree[0][i]) != 0:
            title = ''.join((parsed_html_tree[0][i].xpath(xpath_title.format(i - 1) + '/text()'))).strip()
            author = (parsed_html_tree[0][i].xpath(xpath_author.format(i - 1)))

            if not author:
                author = (parsed_html_tree[0][i].xpath(xpath_author_no_link))
            author = ''.join(author).strip()

            data.append(json.dumps({'author': author, 'title': title}))
            print(i, '-', title, ': ', author, ': ')

    print(data)
    resutls.append({'concordia': data})