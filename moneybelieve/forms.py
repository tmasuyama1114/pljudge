from django import forms
from .models import Portfolio

class PortfolioForm(forms.ModelForm): # 所有する stock を登録する form
    class Meta:
        model = Portfolio
        fields = ("ticker", ) # 入力する欄を指定