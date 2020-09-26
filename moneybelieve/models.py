from django.db import models
from django.conf import settings # AUTH_USER_MODEL 参照用

# 'accounts.CustomUser'

############
# FMP API  #
############

import json
from urllib.request import urlopen
from django.conf import settings
apikey = getattr(settings, "APIKEY", None) # FMP の API　キー

def get_jsonparsed_data(url): # API にアクセスしてレスポンスを得るための関数
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)

def get_company_name(ticker):  # ticker から companyName を得るための関数
    # https://www.financialmodelingprep.com/developer/docs/companies-key-stats-free-api/
    url = ("https://financialmodelingprep.com/api/v3/profile/" + ticker + "?apikey=" + apikey)
    return get_jsonparsed_data(url)[0]['companyName']

def get_price(ticker):  # ticker から companyName を得るための関数
    # https://www.financialmodelingprep.com/developer/docs/companies-key-stats-free-api/
    url = ("https://financialmodelingprep.com/api/v3/profile/" + ticker + "?apikey=" + apikey)
    return get_jsonparsed_data(url)[0]['price']

def get_rating(ticker):  # ticker から Rating を得るための関数
    # https://www.financialmodelingprep.com/developer/docs/companies-rating-free-api/
    url = ("https://financialmodelingprep.com/api/v3/rating/" + ticker + "?apikey=" + apikey)
    return get_jsonparsed_data(url)[0]['rating']

def get_rating_score(ticker): # ticker から Rating Score を得るための関数
    # https://www.financialmodelingprep.com/developer/docs/companies-rating-free-api/
    url = ("https://financialmodelingprep.com/api/v3/rating/" + ticker + "?apikey=" + apikey)
    return get_jsonparsed_data(url)[0]['ratingScore']

def get_rating_recommendation(ticker):  # ticker から Rating Recommendation を得るための関数
    # https://www.financialmodelingprep.com/developer/docs/companies-rating-free-api/
    url = ("https://financialmodelingprep.com/api/v3/rating/" + ticker + "?apikey=" + apikey)
    return get_jsonparsed_data(url)[0]['ratingRecommendation']

#########
# Model #
#########

class Portfolio(models.Model):
    # 外部キーとしてaccounts.Userと紐付けするためのカラム
    investor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ticker = models.CharField(max_length=10)

    def __str__(self): 
        return str(self.ticker)  # Portfolio を呼び出されたら ticker を返す
    
    def company_name(self):
        company_name = get_company_name(self.ticker)
        return str(company_name)

    def price(self):
        price = get_price(self.ticker)
        return str(price)

    def rating(self):
        rating = get_rating(self.ticker)
        return str(rating)

    def rating_score(self):
        rating_score = get_rating_score(self.ticker)
        return str(rating_score)

    def rating_recommendation(self):
        rating_recommendation = get_rating_recommendation(self.ticker)
        return str(rating_recommendation)

########
# Memo #
########

# User モデルの参照の仕方
# https://djangobrothers.com/blogs/referencing_the_user_model/