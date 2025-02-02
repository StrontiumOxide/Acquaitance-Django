from django.shortcuts import render
from django.http import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

def home_view(request):
    return render(
        request=request,
        template_name="home.html"
    )

def omlet(request):

    count = int(request.GET.get("count", 1))
    dish = DATA['omlet'].copy()

    for ing in dish:
        dish[ing] *= count

    context = {
        'recipe': dish,
        'dish': "Омлет"
    }

    return render(
        request=request,
        template_name='calculator/index.html',
        context=context
    )

def pasta(request):

    count = int(request.GET.get("count", 1))
    dish = DATA['pasta'].copy()

    for ing in dish:
        dish[ing] *= count

    context = {
        'recipe': dish,
        'dish': "Паста"
    }

    return render(
        request=request,
        template_name='calculator/index.html',
        context=context
    )

def buter(request):

    count = int(request.GET.get("count", 1))
    dish = DATA['buter'].copy()

    for ing in dish:
        dish[ing] *= count

    context = {
        'recipe': dish,
        'dish': "Бутер"
    }

    return render(
        request=request,
        template_name='calculator/index.html',
        context=context
    )