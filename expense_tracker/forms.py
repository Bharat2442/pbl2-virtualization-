from django import forms
from .models import Expense, Budget

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['title', 'amount', 'category', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'style': 'border: 1px solid #757575; border-radius: 5px; padding: 8px; width: 100%; box-sizing: border-box; outline: none; height: 38px;'}),
        }

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['total_budget']
        widgets = {
            'total_budget': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
        }
