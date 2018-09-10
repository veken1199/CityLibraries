import requests
from lxml import html

url_uqam = 'https://mcgill.on.worldcat.org/search?datasource=library_web&search_field=all_fields&search=true&database=all&scope=wz%3A12129&func=find-b&find_code=WHD&find_code=WHD&find_code=WHD&q=&topLod=0&queryString={}&find=Go'
result_table_xpath = '//*[@id="brief_results"]/div[1]/ol'
title_xpath = '//*[@id="record_{}"]/div[1]/div[1]/div[1]/div/a/text()'
author_xpath = '//*[@id="record_{}"]/div[1]/div[1]/div[2]/div[2]/div[1]/div/span/span[2]/span/a/text()'
publisher_xpath = '//*[@id="exlidResult{}"]/td[4]/div[1]/div/h3[2]/text()'


def crawl(keyword, results):
    page =  requests.get(url_uqam.format(keyword)).content
    html_tree = html.fromstring(page)

    results_table = html_tree.xpath(result_table_xpath)
    response = []

    for i in range(0, len(results_table[0])):
        title = (''.join(results_table[0].xpath(title_xpath.format(i)))).strip()

        author= ', '.join(results_table[i].xpath(author_xpath.format(i)))
        publisher = ''.join(results_table[i].xpath(publisher_xpath.format(i)))

        response.append({'title': title,
                         'author': author,
                         'publisher': publisher})

    results.append({'uni': 'uqam',
                    'data': response})
    return results



