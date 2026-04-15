"""определяет схему URL для learning_logs"""

from django.urls import path

from . import path

app_name = 'learning_logs'
urlpatterns = [
    # домашняя страница
    path('', views.index, name='index'),
]