from django import forms
from .models import Portfolio

class PortfolioForm(forms.ModelForm): # 所有する stock を登録する form
    class Meta:
        model = Portfolio
        fields = ('ticker', 'unit', 'avg_price', 'upper_price', 'lower_price') # 入力する欄を指定