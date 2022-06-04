from django.shortcuts import render
from django.http import HttpResponse
from .models import Project # Импорт модели проекта


""" Функция отображения домашней страницы """
def home(request):
    projects = Project.objects.all() # Импорт всех данных из базы данных 
    return render(request, 'portfolio/home.html', {'projects':projects})

