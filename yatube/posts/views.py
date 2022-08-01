from django.shortcuts import render, get_object_or_404

from .models import Post, Group


def index(request):
    """
    Обработать запрос перехода на главную страницу.
    """
    # Шаблон
    template = 'posts/index.html'
    # Записи из БД
    posts: Post = Post.objects.all()[:10]

    context: dict = {
        'posts': posts,
        'date_format': Post.date_format,
    }
    return render(request, template, context)


def group_posts(request, slug):
    """
    Обработать запрос перехода на страницу с записями сообщества.
    """
    # Шаблон
    template = 'posts/group_list.html'
    # Сообщество
    group: Group = get_object_or_404(Group, slug=slug)
    # Записи из БД
    posts: Post = group.posts.all()[:10]

    context: dict = {
        'group': group,
        'posts': posts,
        'date_format': Post.date_format,
    }
    return render(request, template, context)
