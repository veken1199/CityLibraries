import logging

import requests
from lxml import html

from classes import LibraryResultItem, LibraryResult
from constants import CITIES
from crawlers.crawler_registery import register_crawler_decorator
from helpers import is_valid_book

base_url_concordia = 'http://encore.concordia.ca/{}'
url_concordia = 'https://encore.concordia.ca/iii/encore/plus/C__S{}__Ff%3Afacetmediatype%3Aa%3Aa%3ABooks%20%28PRINT%29%3A%3A__Orightresult__U__X0__Nv%40Booksc%40addfacetfilter%28SourceType%3ABooks%29g%40SourceTypen%40Source%20Type?lang=eng&suite=def'

xpath_results_table = './/*[@id="mainContentArea"]/div[@class="gridBrowseContent2 searchResult"]'
xpath_title_first = './/*[@id="recordDisplayLink2Component"]/text()'
xpath_author_first = './/*[@id="authorDisplayLinkComponent"]/text()'
xpath_link_first = './/*[@id="recordDisplayLink2Component"]/@href'
xpath_title = './/span[@class="title"]/a/text()'
xpath_author = './/div[@class="dpBibAuthor"]/a/text()'
xpath_link = './/span[@class="title"]/a/@href'
xpath_additional_title = './/span[@class="additionalFields customSecondaryText"]/text()'
type_xpath = './/span[@class="citations"]/text()'
xpath_author_no_link = 'div[2]/div/div[1]/text()'

logger = logging.getLogger()

@register_crawler_decorator(CITIES.MTL)
def crawl(keyword, results):
    """
    Crawler function to extract data from Concordia University Library.
    The data will be returned and will be appended to the results argument
    :param keyword:
    :param results:
    :return: Object: LibraryResult
    """
    response = []
    try:
        query_url = url_concordia.format(keyword)
        page = requests.get(query_url)
        html_tree = html.fromstring(page.content)
        results_table = html_tree.xpath(xpath_results_table)

        # getting the first element
        if len(results_table):
            title = ''.join((results_table[0].xpath(xpath_title_first))).strip()
            author = ''.join((results_table[0].xpath(xpath_author_first))).strip()
            link = base_url_concordia.format(''.join(results_table[0].xpath(xpath_link_first)).strip())
            response.append(LibraryResultItem(title, author, link))

        # getting the rest of the element
        for i in range(1, len(results_table)):
            title = ''.join(results_table[i].xpath(xpath_title.format(i - 1))).strip()
            author = ''.join(results_table[i].xpath(xpath_author)).strip()
            link = base_url_concordia.format(''.join(results_table[i].xpath(xpath_link)).strip())
            type = ''.join(results_table[i].xpath(type_xpath)).strip()

            if not author:
                author = ''.join(results_table[i].xpath(xpath_additional_title)).strip()

            if not author:
                author = ''.join(results_table[i].xpath(xpath_author_no_link)).strip()

            if is_valid_book(title, author):
                response.append(LibraryResultItem(title, author, link, query_url=query_url))

    except Exception as e:
        logger.warning('While processing the html encountered the following error: {}'.format(e))

    results.append(LibraryResult('concordia', response))
    return results
