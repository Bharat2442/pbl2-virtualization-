from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense
from .forms import ExpenseForm

from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense, Budget
from .forms import ExpenseForm, BudgetForm

def expense_list(request):
    expenses = Expense.objects.all()
    budget_obj = Budget.objects.first()
    if budget_obj:
        total_budget = budget_obj.total_budget
    else:
        total_budget = 0
    total_expenses = sum(expense.amount for expense in expenses)
    budget_left = total_budget - total_expenses
    total_transactions = expenses.count()
    context = {
        'expenses': expenses,
        'total_budget': total_budget,
        'budget_left': budget_left,
        'total_transactions': total_transactions,
    }
    return render(request, 'expense_tracker/expense_list.html', context)

def add_budget(request):
    budget_obj = Budget.objects.first()
    if request.method == 'POST':
        if budget_obj:
            form = BudgetForm(request.POST, instance=budget_obj)
        else:
            form = BudgetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        if budget_obj:
            form = BudgetForm(instance=budget_obj)
        else:
            form = BudgetForm()
    return render(request, 'expense_tracker/add_budget.html', {'form': form})

def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'expense_tracker/add_expense.html', {'form': form})

def expense_update(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'expense_tracker/add_expense.html', {'form': form})

def expense_delete(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == 'POST':
        expense.delete()
        return redirect('expense_list')
    return render(request, 'expense_tracker/expense_confirm_delete.html', {'expense': expense})

def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'expense_tracker/add_expense.html', {'form': form})

def expense_update(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'expense_tracker/add_expense.html', {'form': form})

def expense_delete(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == 'POST':
        expense.delete()
        return redirect('expense_list')
    return render(request, 'expense_tracker/expense_confirm_delete.html', {'expense': expense})
