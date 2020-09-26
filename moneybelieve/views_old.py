from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin # ログイン時のみ閲覧
# 以下を全て追加
from django.views import generic
from django.views.generic import TemplateView, ListView
from django.urls import reverse_lazy # TemplateView でページ遷移先を指定するクラス

from .models import Company, Fstatement

class IndexTemplateView(TemplateView):
    template_name = 'moneybelieve/index.html'

################
# CSV(Compnay) #
################
import csv

from django.views import generic
from .forms import CSVUploadForm

class CompanyImport(generic.FormView):
    template_name = 'moneybelieve/import.html'
    success_url = reverse_lazy('mobeybelieve:index')
    form_class = CompanyCSVUploadForm

    def form_valid(self, form):
        form.save()
        return redirect('moneybelieve:index')

def company_export(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="companys.csv"'
    # HttpResponseオブジェクトはファイルっぽいオブジェクトなので、csv.writerにそのまま渡せます。
    writer = csv.writer(response)
    for company in Company.objects.all():
        writer.writerow([company.pk, company.symbol, company.name])
    return response

#####################
# CSV (Fstatements) #
#####################




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

def get_company_data(symbol): # symbol からProfileを得るための関数
    url = ("https://financialmodelingprep.com/api/v3/profile/" + symbol + "?apikey=" + apikey)
    return get_jsonparsed_data(url)[0]

# Company 一覧
class CompanyList(generic.ListView):
    model = Company
    template_name = 'moneybelieve/company_list.html'
    paginate_by = 10
    
    # データを取得するときに行う処理を記述。シンボル名順で並び替え。
    def get_queryset(self): # ログインユーザに応じたポートフォリオを返す処理 # https://teratail.com/questions/190150
        # id = self.request.user.id
        company = Company.objects.all()[:10]
        for data in company:
            try:
                data.name = get_company_data(data.symbol)['companyName']
                data.industry = get_company_data(data.symbol)['industry']
                data.sector = get_company_data(data.symbol)['sector']
                data.logo = get_company_data(data.symbol)['image']
                data.save()
            except:
                pass
        return Company.objects.all()[:15]

class CompanyProfile(ListView):
    model = Company
    
    def get_queryset(self):
        company = Company.objects.all()[:1]
        for data in company:
            try:
                # data.name = get_company_data(data.symbol)['companyName']
                data.industry = get_company_data(data.symbol)['industry']
                data.sector = get_company_data(data.symbol)['sector']
                data.logo = get_company_data(data.symbol)['image']
                data.save()
            except:
                pass
        return Company.objects.all()[:1]
    template_name = 'moneybelieve/index.html'

class CompanyFstatements(ListView):
    template_name = 'moneybelieve/fstatements.html'