from django.contrib import admin
from django.urls import path, include
from todo_exptrack import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo_list.urls')),  # Root URL points to login page in todo_list.urls
    path('home/', views.home, name='home'),  # Landing page after login with two buttons
    path('todo/', include('todo_list.urls')),
    path('expenses/', include('expense_tracker.urls')),
]
