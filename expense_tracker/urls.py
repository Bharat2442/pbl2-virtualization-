from django.urls import path
from .views import expense_list, add_expense, expense_update, expense_delete, add_budget

urlpatterns = [
    path('', expense_list, name='expense_list'),
    path('add/', add_expense, name='add_expense'),
    path('update/<int:pk>/', expense_update, name='expense_update'),
    path('delete/<int:pk>/', expense_delete, name='expense_delete'),
    path('budget/', add_budget, name='add_budget'),
]
