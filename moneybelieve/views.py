from django.contrib.auth import login
from django.contrib.auth.decorators import login_required # 追加
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.shortcuts import render, redirect

from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView, DetailView, UpdateView, CreateView, ListView # 追加
from django.urls import reverse_lazy

from .forms import PortfolioForm
from .models import Portfolio

class New(CreateView): # PortFolio 登録画面
    # 使うためテンプレートの指定
    template_name = 'moneybelieve/new.html'
    # 使うformクラスの指定
    form_class = PortfolioForm
    # 成功時に飛ぶURLの指定
    success_url = reverse_lazy('moneybelieve:index') # 登録成功時のリダイレクト先

    # 入力に問題がない場合現在ログインしているアカウントを投稿者として登録するための処理
    def form_valid(self, form):
        form.instance.investor_id = self.request.user.id
        return super(New, self).form_valid(form) # 入力内容のチェック付き

# 投稿一覧
class Index(ListView):
    model = Portfolio
    template_name = 'moneybelieve/index.html'
    #  最大表示件数を設定しています 今回は100件
    paginate_by = 100
    # データを取得するときに行う処理を記述できる今回は投稿日を降順で並べる様にした
    queryset = Portfolio.objects.order_by('ticker').reverse() # Template 側で "object_list" という名前で取り出せるようになる

# ユーザーの Portfolio 一覧

class PortfolioListView(LoginRequiredMixin, ListView):
    model = Portfolio
    template_name = "moneybelive/portfolio_list.html"
    
    def get_queryset(self):
        id = self.request.user.id
        return Portfolio.objects.filter(investor_id=id)


# class PortfolioListView(LoginRequiredMixin, TemplateView):
#     template_name = "moneybelive/portfolio_list.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         id = self.request.user.id # ログインユーザのレコードに絞り込むため user_id を格納
#         context['rating'] = Portfolio.objects.filter(investor_id=id)
#         # ↑ここで呼び出したモデルの値をもとに、更に変数
#         # 例：Portfolio モデルの symbol というカラムに「ZM」という値が入っている場合は、そのレコードに対応する値として「1」を templateに表示させたい
#         return context