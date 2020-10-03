from django.contrib.auth import login
from django.contrib.auth.decorators import login_required # 追加
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.shortcuts import render, redirect

from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView, DetailView, UpdateView, CreateView, ListView, DeleteView # 追加
from django.urls import reverse_lazy
from django.urls import reverse

from .forms import PortfolioForm
from .models import Portfolio

#########################################
# FMP から API で各会社の情報を取得する処理  #
#########################################

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

def get_price(ticker):  # ticker から 現在価格 を得るための関数
    # https://www.financialmodelingprep.com/developer/docs/companies-key-stats-free-api/
    url = ("https://financialmodelingprep.com/api/v3/profile/" + ticker + "?apikey=" + apikey)
    return get_jsonparsed_data(url)[0]['price']

##############
# トップページ #
##############

class Index(TemplateView):
    template_name = 'pljudge/index.html'

#######################################
# ユーザが登録するポートフォリオに関する処理 #
#######################################

class PortfolioCreate(CreateView): # PortFolio 登録画面
    # 使うためテンプレートの指定
    template_name = 'pljudge/portfolio_create.html'
    # 使うformクラスの指定
    form_class = PortfolioForm
    # 成功時に飛ぶURLの指定
    success_url = reverse_lazy('pljudge:portfolio_list') # 登録成功時のリダイレクト先

    # 入力に問題がない場合現在ログインしているアカウントを投稿者として登録するための処理
    def form_valid(self, form):
        form.instance.investor_id = self.request.user.id
        return super(PortfolioCreate, self).form_valid(form) # 入力内容のチェック付き

class PortfolioUpdate(UpdateView):
    # https://noumenon-th.net/programming/2019/11/19/django-updateview/
    template_name = 'pljudge/portfolio_update.html'
    model = Portfolio
    fields = ['ticker', 'unit', 'avg_price', 'upper_price', 'lower_price']

    def get_success_url(self):
        return reverse('pljudge:portfolio_list')
    # success_url = reverse_lazy('pljudge:portfolio_list') # アップデート成功時のリダイレクト先
    
    # 入力に問題がない場合現在ログインしているアカウントを投稿者として登録するための処理
    def get_form(self):
        form = super(PortfolioUpdate, self).get_form()
        form.fields['ticker'].label = 'ticker'
        return form

class PortfolioListView(LoginRequiredMixin, ListView):
    model = Portfolio
    template_name = "pljudge/portfolio_list.html"
    
    def get_queryset(self):
        # https://qiita.com/uenosy/items/54136aff0f6373957d22
        id = self.request.user.id
        portfolio = Portfolio.objects.filter(investor_id=id)
        return Portfolio.objects.filter(investor_id=id)

class PortfolioListDetailView(LoginRequiredMixin, ListView):
    model = Portfolio
    template_name = "pljudge/portfolio_list_detail.html"
    
    def get_queryset(self):
        # https://qiita.com/uenosy/items/54136aff0f6373957d22
        id = self.request.user.id
        portfolio = Portfolio.objects.filter(investor_id=id)
        return Portfolio.objects.filter(investor_id=id)

class PortfolioDelete(DeleteView):
    # https://noumenon-th.net/programming/2019/11/20/django-deleteview/
    model = Portfolio
    template_name = "pljudge/portfolio_delete.html"
    success_url = reverse_lazy('pljudge:portfolio_list')