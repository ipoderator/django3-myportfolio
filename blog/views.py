from django.shortcuts import render,get_object_or_404
from .models import Blog  # Импорт модели проекта блог


""" Функция отображения страницы блога"""
def all_blogs(request):
    blogs = Blog.objects.order_by('-date') # Сортировка объектов по дате
    return render(request, 'blog/all_blogs.html', {'blogs':blogs})


""" Функция отображает нужную страницу на сайте блога """
def datail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id) # Данная функция находит объект под нужным номером
    return render(request,'blog/detail.html')
     