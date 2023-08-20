# Для применения Q-объектов их нужно импортировать:
from django.db.models import Q
from django.shortcuts import render

from ice_cream.models import IceCream

def index(request):
    template_name = 'homepage/index.html'
    # # Заключаем вызов методов в скобки
    # # (это стандартный способ переноса длинных строк в Python);
    # # каждый вызов пишем с новой строки, так проще читать код:
    # ice_cream_list = IceCream.objects.values(
    #         'id', 'title', 'description'
    #     ).filter(
    #         # Делаем запрос, объединяя два условия
    #         # через Q-объекты и оператор AND:
    #         (Q(is_published=True)
    #          & Q(is_on_main=True))
    #         | Q(title__contains='пломбир')
    #     ).order_by('title')[0:3]

    # ice_cream_list = IceCream.objects.all()
    ice_cream_list = IceCream.objects.values(
        'id', 'title', 'description'
    ).filter(
        # Проверяем, что
        is_published=True,  # Сорт разрешён к публикации;
        is_on_main=True,  # Сорт разрешён к публикации на главной странице;
        category__is_published=True  # Категория разрешена к публикации.
    )

    context = {
        'ice_cream_list': ice_cream_list,
    }
    return render(request, template_name, context)
