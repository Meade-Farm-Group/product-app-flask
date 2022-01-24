from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_tasks, name='user_tasks'),
]
