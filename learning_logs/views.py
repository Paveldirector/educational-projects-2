from django.shortcuts import render

# Create your views here.

def index(request):
    """домашняя страница приложения learning_logs"""
    return render(request, 'learning_logs/index.html')

