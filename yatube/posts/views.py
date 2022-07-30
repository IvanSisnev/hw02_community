from django.shortcuts import render, get_object_or_404

from .models import Post, Group


def index(request):
    """
    Обработать запрос перехода на главную страницу.
    """
    # Шаблон
    template: str = 'posts/index.html'
    # Наименование закладки
    title: str = 'Последние обновления на сайте'
    # Заголовок страницы
    header_text: str = 'Последние обновления на сайте'
    # Записи из БД
    posts: Post = Post.objects.all()[:10]

    context: dict = {
        'title': title,
        'header': header_text,
        'posts': posts,
        'date_format': Post.date_format,
    }
    return render(request, template, context)


def group_posts(request, slug):
    """
    Обработать запрос перехода на страницу с записями сообщества.
    """
    # Шаблон
    template: str = 'posts/group_list.html'
    # Наименование закладки
    title: str = 'Записи сообщества'
    # Заголовок страницы
    header_text: str = 'Записи сообщества'
    # Сообщество
    group: Group = get_object_or_404(Group, slug=slug)
    # Записи из БД
    posts: Post = Post.objects.filter(group=group)[:10]

    context: dict = {
        'title': title,
        'header': header_text,
        'group': group,
        'posts': posts,
        'date_format': Post.date_format,
    }
    return render(request, template, context)
