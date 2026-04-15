from django.shortcuts import render, redirect
from .models import Topic
from .forms import TopicForm

# Create your views here.

def index(request):
    """домашняя страница приложения learning_logs"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """выводит список тем"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """выводит одну тему и все ее записи"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    """определяет новую тему"""
    if request.method != 'POST':
        # данные не отправлялись; создается пустая форма
        form = TopicForm()
    else:
        # отправленны данные POST; обработать данные
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')
    
    # вывести пустую строку или недействующую форму
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)