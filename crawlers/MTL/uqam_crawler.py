import logging
import requests
from lxml import html

from classes import LibraryResult, LibraryResultItem
from constants import CITIES
from crawlers.crawler_registery import register_crawler_decorator

url_uqam = 'http://virtuose.uqam.ca/primo_library/libweb/action/dlSearch.do?institution=UQAM&vid=UQAM&group=GUEST&onCampus=false&fromSitemap=1&lang=fre&search_scope=upac&bulkSize=40&tab=default_tab&indx=1&displayField=title&displayField=creator&query=any,contains,{}'
xpath_result_table = '//*[@id="exlidResultsTable"]/tbody/tr'
xpath_title = './/h2[@class="EXLResultTitle"]/a/text()'
xpath_composed_title = './/h2[@class="EXLResultTitle"]/text()'
xpath_author = './/h3[@class="EXLResultAuthor"]/text()'
xpath_item_link = './/h2[@class="EXLResultTitle"]/a/@href'
xpath_publisher = './/h3[@class="EXLResultFourthLine"]/text()'
xpath_status = './/p[@class="EXLResultAvailability"]/em/text()'
xpath_item_type = './/span[@class="EXLThumbnailCaption"]/text()'

logger = logging.getLogger()


@register_crawler_decorator(CITIES.MTL)
def crawl(keyword, results):
    """
     Crawler function to extract data from Uqam University Library.
     The data will be returned and will be appended to the results argument
     :param keyword:
     :param results:
     :return: Object: LibraryResult
     """
    response = []
    try:
        page = requests.get(url_uqam.format(keyword)).content
        page = html.fromstring(page)
        results_table = page.xpath(xpath_result_table)

        for result_item in results_table:
            title = (''.join(result_item.xpath(xpath_title))).strip()
            if not title:
                title = (''.join(result_item.xpath(xpath_composed_title))).strip()
            author = ''.join(result_item.xpath(xpath_author)).strip()
            publisher = ''.join(result_item.xpath(xpath_publisher)).strip()
            status = ''.join(result_item.xpath(xpath_status)).strip()
            item_type = ''.join(result_item.xpath(xpath_item_type)).strip()
            link = ''.join(result_item.xpath(xpath_item_link)).strip()

            response.append(LibraryResultItem(title, author, link, publisher=publisher))
    except Exception as e:
        logger.warning('While processing the html encountered the following error: {}'.format(e))

    results.append(LibraryResult('uqam', response))
    return results
