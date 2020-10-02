from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'pljudge'

urlpatterns = [
    path('portfolio_create/', login_required(views.PortfolioCreate.as_view()), name='portfolio_create'), # Portfolio 登録用
    path('', views.Index.as_view(), name='index'), # Portfolio 登録成功時
    path("portfolio_list/", views.PortfolioListView.as_view(), name='portfolio_list'),
    path("portfolio_list_detail/", views.PortfolioListDetailView.as_view(), name='portfolio_list_detail'),
    path('<int:pk>/update/', views.PortfolioUpdate.as_view(), name='portfolio_update'),
    path('<int:pk>/delete/', views.PortfolioDelete.as_view(), name='portfolio_delete'),
]