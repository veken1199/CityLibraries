import requests
from lxml import html

url_uqam = 'http://virtuose.uqam.ca/primo_library/libweb/action/dlSearch.do?institution=UQAM&vid=UQAM&group=GUEST&onCampus=false&fromSitemap=1&lang=fre&search_scope=upac&bulkSize=40&tab=default_tab&indx=1&displayField=title&displayField=creator&query=any,contains,{}'
result_table_xpath = '//*[@id="exlidResultsTable"]/tbody/tr'
title_xpath = '//*[@id="exlidResult{}"]/td[4]/div[1]/div/h2/text()'
composed_title_xpath = '//*[@id="exlidResult{}"]/td[4]/div[1]/div/h2/a/text()'
author_xpath = '//*[@id="exlidResult{}"]/td[4]/div[1]/div/h3[1]/text()'
publisher_xpath = '//*[@id="exlidResult{}"]/td[4]/div[1]/div/h3[2]/text()'


def crawl(keyword, results):
    page =  requests.get(url_uqam.format(keyword)).content
    html_tree = html.fromstring(page)

    results_table = html_tree.xpath(result_table_xpath)
    response = []

    for i in range(0, len(results_table)):
        title = (''.join(results_table[i].xpath(title_xpath.format(i)))).strip()
        if not title:
            title = (''.join(results_table[i].xpath(composed_title_xpath.format(i)))).strip()
        author= ''.join(results_table[i].xpath(author_xpath.format(i)))
        publisher = ''.join(results_table[i].xpath(publisher_xpath.format(i)))

        response.append({'title': title,
                         'author': author,
                         'publisher': publisher})

    results.append({'uni': 'uqam',
                    'data': response})
    return results



