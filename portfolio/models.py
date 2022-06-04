from django.db import models


""" Класс по взаимодейсвию с базой данных """
class Project(models.Model):  
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True) # Параметр отрытия новой вкладки браузера


    def __str__(self) -> str:
        return self.title
        