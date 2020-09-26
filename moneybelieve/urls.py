from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'moneybelieve'

urlpatterns = [
    path('new/', login_required(views.New.as_view()), name='new'), # Portfolio 登録用
    # path('', login_required(views.Index.as_view()), name='index'), # Portfolio 登録制工事
    path('', views.Index.as_view(), name='index'), # Portfolio 登録制工事
    path("portfolio_list/", views.PortfolioListView.as_view(), name="portfolio_list"),
]