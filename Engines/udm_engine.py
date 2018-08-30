import requests
import jwt

udm_jwt_url = 'http://atrium.umontreal.ca/primo_library/libweb/webservices/rest/v1/guestJwt/UM?isGuest=true&lang=fr_FR&targetUrl=http%253A%252F%252Fatrium.umontreal.ca%252Fprimo-explore%252Fsearch%253Fquery%253Dany%252Ccontains%252C{}%2526tab%253Ddefault_tab%2526search_scope%253DTout_sauf_articles%2526vid%253DUM%2526sortby%253Drank%2526lang%253Dfr_FR&viewId=UM'
udm_url = 'http://atrium.umontreal.ca/primo_library/libweb/webservices/rest/primo-explore/v1/pnxs?addfields=vertitle,title,collection,unititle,lds11,coverage,creator,contributor,edition,ispartof,lds08,creationdate,description,relation,publisher,lds22,lds23,lds24,lds25,lds02,lds12,subject,lds05,lds04,format,lds17,lds06,lds26,lds20,lds21,lds19,lds27,language,rights,identifier,type,lds13,lds30,lds31&getMore=0&inst=UM&lang=fr_FR&limit=40&offset=0&pcAvailability=true&q=any,contains,{}&qExclude=&qInclude=&rtaLinks=true&scope=Tout_sauf_articles&skipDelivery=Y&sort=rank&tab=default_tab&vid=UM'

def crawl(keyword, results):
    # Create jwt token:
    token = requests.get(udm_jwt_url.format(keyword))
    page = requests.get(udm_url.format(keyword), headers={'Authorization': 'Beaver ' + token.content.decode('UTF-8')})

    response = []
    for idx, record in enumerate(page.json()['docs']):
        record_data = record['pnx']['sort']
        response.append({'date': ''.join(record_data.get('creationdate', '')),
                         'title': ''.join(record_data.get('title', '')),
                         'author': ''.join(record_data.get('author', ''))})
    results.append({'uni': 'udm',
                    'data': response})