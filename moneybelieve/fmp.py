############
# FMP API  #
############

import json
from urllib.request import urlopen
from django.conf import settings

apikey = getattr(settings, "APIKEY", None) # FMP の API　キー(setting.py に記載)

def get_jsonparsed_data(url): # API にアクセスしてレスポンスを得るための関数
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)

def get_company_data(symbol): # symbol からProfileを得るための関数
    url = ("https://financialmodelingprep.com/api/v3/profile/" + symbol + "?apikey=" + apikey)
    return get_jsonparsed_data(url)[0]

def get_company_industry(symbol): # symbol からProfileを得るための関数
    url = ("https://financialmodelingprep.com/api/v3/profile/" + symbol + "?apikey=" + apikey)
    return get_jsonparsed_data(url)[0]['industry']