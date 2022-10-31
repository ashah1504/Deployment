from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contacts', views.contacts, name='contacts'),
    path('post/', views.post, name='post'),
    path('tasks/', views.tasks, name='tasks'),
    path('taskadd/', views.taskadd, name='taskadd'),
    path('profile/', views.profile, name='profile'),
]
