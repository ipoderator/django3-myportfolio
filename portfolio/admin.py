from django.contrib import admin
from .models import Project


# Регистрация моделей для админки
admin.site.register(Project)
