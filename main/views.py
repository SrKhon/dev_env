from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories


def index(request):

    context = {
        "title": "HOME - Главная страница",
        "content": "Магазин мебели HOME",
    }
    return render(request, "main/index.html", context)


def about(request):
    context = {
        "title": "HOME - О нас",
        "content": "О нас",
        "text_on_page": "Текст о том какой классный этот интернет магазин.",
    }
    return render(request, "main/about.html", context)
