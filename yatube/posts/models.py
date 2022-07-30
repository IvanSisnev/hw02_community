"""
Модуль для создания классов моделей.
"""

from django.contrib.auth import get_user_model
from django.db import models

from django.urls import reverse

User = get_user_model()


class Post(models.Model):
    """
    Класс модели Post для создания и редактирования записей.
    """

    # Форматирование даты для вывода в шаблоны
    date_format = "j E Y"

    # Текст записи
    text = models.TextField()

    # Дата создания записи
    pub_date = models.DateTimeField(auto_now_add=True)

    # Автор
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='posts')

    # Сообщество
    group = models.ForeignKey('Group', on_delete=models.CASCADE,
                              related_name='groups', blank=True, null=True)

    class Meta:
        """
        Мета класс для сортировки.
        """
        ordering = ['-pub_date']


class Group(models.Model):
    """
    Класс модели Group для создания и редактирования сообществ.
    """

    # Наименование сообщества
    title = models.CharField(max_length=200)

    # Slug для URL
    slug = models.SlugField(unique=True)

    # Описание сообщества
    description = models.TextField()

    def __str__(self):
        """
        Вернуть стоку с наименованием сообщества.
        """
        return self.title

    def get_absolute_url(self):
        """
        Cоздать URL адрес
        """
        return reverse('group_list', args=self.slug)
