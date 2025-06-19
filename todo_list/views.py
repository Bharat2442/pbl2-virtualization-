from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.views import View
from django.db import transaction

from .models import Task
from .forms import PositionForm


class CustomLoginView(LoginView):
    template_name = 'todo_list/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')  # Redirect to task list after login


class RegisterPage(View):
    @method_decorator(login_required(login_url='login'))
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('tasks')
        form = UserCreationForm()
        return render(request, 'todo_list/register.html', {'form': form})

    @method_decorator(login_required(login_url='login'))
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('tasks')
        return render(request, 'todo_list/register.html', {'form': form})


@method_decorator(login_required(login_url='login'), name='dispatch')
class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'todo_list/task_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__icontains=search_input)

        context['search_input'] = search_input
        return context


@method_decorator(login_required(login_url='login'), name='dispatch')
class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'todo_list/task.html'


@method_decorator(login_required(login_url='login'), name='dispatch')
class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = '/'

    template_name = 'todo_list/task_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


@method_decorator(login_required(login_url='login'), name='dispatch')
class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = '/'

    template_name = 'todo_list/task_form.html'


@method_decorator(login_required(login_url='login'), name='dispatch')
class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = '/'
    template_name = 'todo_list/task_confirm_delete.html'

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class TaskReorder(View):
    @method_decorator(login_required(login_url='login'))
    def post(self, request):
        form = PositionForm(request.POST)
        if form.is_valid():
            positionList = form.cleaned_data["position"].split(',')
            with transaction.atomic():
                self.request.user.set_task_order(positionList)
        return redirect('/')
