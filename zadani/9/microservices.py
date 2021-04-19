import requests
import json

def posli_request(start):
    cookies = {
        'COOKIE_SUPPORT': 'true',
        'GUEST_LANGUAGE_ID': 'cs_CZ',
        'MPSV-UP-PRTL': '5ccba3d87f07ddf0bcacc5271313c459e451aaea085010c87585704ac5159b70fb3f0169',
        'MPSV-UP': '28d4a3da0dfcf1ea03933ae2b8f36fa8204ebe7a341ccd315b7417f2b5d372e52101d322',
        '_ga': 'GA1.2.352703446.1618822205',
        '_gid': 'GA1.2.832329041.1618822205',
        'JSESSIONID': 'CEFE830B67571BF04D4FC035BBE95C87',
        'LANG_ID': 'cs_CZ',
        'LFR_SESSION_STATE_20119': '1618848611850',
    }

    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
        'DNT': '1',
        'accept-language': 'cs',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36',
        'content-type': 'application/json',
        'accept': 'application/json',
        'x-client-session-id': 'B2E3EE39-400C-46C5-AED3-E067EA706111',
        'Origin': 'https://www.uradprace.cz',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.uradprace.cz/web/cz/volna-mista-v-cr',
    }

    data = '{"index":["volna-mista"],"pagination":{"start":' + str(start) + ',"count":10,"order":["-datumZmeny","-id"]},"aggs":{"sumField":{"sum":{"field":"volneMisto.pocetMist"}}},"query":{"must":[{"mustNot":[{"match":{"field":"zverejnovatVpmId","query":3721}}]},{"match":{"field":"stavVolnehoMistaId","query":3701}},{"should":[{"match":{"field":"expirace","query":null}},{"range":{"field":"expirace","gte":"2021-04-19"}}]},{"range":{"field":"pocetMist","gte":1}}]}}'
    response = requests.post('https://www.uradprace.cz/volna-mista/rest/volna-mista/dto/query', headers=headers, cookies=cookies, data=data)
    slovnik_kompletni = json.loads(response.text)
    seznam_mist = slovnik_kompletni["list"]
    return seznam_mist

vsechna_mista = []
for aktualni_start in range(0, 60, 10):
    seznam_mist = posli_request(aktualni_start)
    vsechna_mista = vsechna_mista + seznam_mist

soubor = open('pracovni_mista.json', 'w', encoding='utf-8')
json.dump(vsechna_mista, soubor)
soubor.close()

import pandas
pandas.load_json("pracovni_mista.json")
