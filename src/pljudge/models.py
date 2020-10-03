from django.db import models
from django.conf import settings # AUTH_USER_MODEL 参照用

#Decimalをインポート
from decimal import Decimal

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

def get_fgrowth(ticker):  # ticker から Financial Statement Growth
    # https://www.financialmodelingprep.com/developer/docs/company-financial-statement-growth-api/
    url = ("https://financialmodelingprep.com/api/v3/financial-growth/" + ticker + "?apikey=" + apikey)
    return get_jsonparsed_data(url)[0]

def get_fratio(ticker):  # ticker から Financial Ratios
    # https://www.financialmodelingprep.com/developer/docs/financial-ratio-free-api/
    url = ("https://financialmodelingprep.com/api/v3/ratios/" + ticker + "?apikey=" + apikey)
    return get_jsonparsed_data(url)[0]

#########
# Model #
#########

class Portfolio(models.Model):
    # 外部キーとしてaccounts.Userと紐付けするためのカラム
    investor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ticker = models.CharField(verbose_name='ティッカー', max_length=10)
    unit = models.IntegerField(verbose_name='保有数量', blank=True, null=True, default=0)
    price = models.DecimalField(verbose_name='現在価格', max_digits=10, decimal_places=2, blank=True, null=True, default=0.00)
    avg_price = models.DecimalField(verbose_name='平均取得単価', max_digits=10, decimal_places=2, blank=True, null=True, default=0.00)
    upper_price = models.DecimalField(verbose_name='利確ライン', max_digits=10, decimal_places=2, blank=True, null=True, default=0.00)
    lower_price = models.DecimalField(verbose_name='損切りライン', max_digits=10, decimal_places=2, blank=True, null=True, default=0.00)
    
    def __str__(self): 
        return str(self.ticker)  # Portfolio を呼び出されたら ticker を返す
    
    def company_name(self): # 会社名
        company_name = get_company_name(self.ticker)
        return str(company_name)

    def price(self): # 現在価格
        price = get_price(self.ticker)
        return str(price)

    #################
    # 利確・損切り判断 #
    #################

    def profit_or_loss(self):
        price = get_price(self.ticker)  # 現在価格を取得
        # price = Decimal(str(self.price))  # 現在価格を取得 (self でうまくいかない)
        profit_loss_unit = Decimal(price) - self.avg_price # 一株あたりの損益を計算（型はDecimal型に合わせる）
        profit_or_loss = profit_loss_unit * self.unit  # 保有数量分をかけ合わせて合計を算出する
        rounded_profit_or_loss = round(profit_or_loss, 2) # 最後に丸める
        return str(rounded_profit_or_loss)
    
    def fix_profit(self):
        price = get_price(self.ticker)  # 現在価格を取得
        to_fix_profit = Decimal(price) - self.upper_price  # 正なら利益確定させるべき
        if to_fix_profit > 0:
            return round(to_fix_profit, 2)
        
    def fix_loss(self):
        price = get_price(self.ticker)  # 現在価格を取得
        to_fix_loss = Decimal(price) - self.lower_price  # 負なら損切り確定させるべき
        if to_fix_loss < 0:
            return round(to_fix_loss, 2)
    #     return to_fix_loss
    
########
# Memo #
########

# User モデルの参照の仕方
# https://djangobrothers.com/blogs/referencing_the_user_model/    