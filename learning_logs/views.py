from django.shortcuts import render
from .models import Topic

# Create your views here.

def index(request):
    """домашняя страница приложения learning_logs"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """выводит список тем"""
    topics = Topic.objects.order_by('data_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)