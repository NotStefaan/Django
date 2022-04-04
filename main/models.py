from turtle import title
from django.db import models


class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость дня'
        verbose_name_plural = 'Новости дня'
# Create your models here.
