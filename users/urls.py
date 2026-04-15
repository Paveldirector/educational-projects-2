"""определяет схемы URL для пользователей"""

from django.urls import path, include

app_name = 'users'
urlpatterns = [
    # включить URL авторизации по умолчанию
    path('', include('django.contrib.auth.urls')),
]