from django.shortcuts import render
from .models import MenuItem

from django.shortcuts import render
from .models import MenuItem

def menu_view(request):
    menu_items = MenuItem.objects.all()
    context = {
        'menu_items': menu_items,
    }
    return render(request, 'menu.html', context)

# from django.shortcuts import render

# # Create your views here.
# from django import template
# from .models import MenuItem

# from django import template


# register = template.Library()

# @register.inclusion_tag('menu_template.html')
# def draw_menu(menu_name, current_url):
#     menu_items = MenuItem.objects.filter(parent__isnull=True)
#     return {'menu_items': menu_items, 'current_url': current_url}

# from django.shortcuts import render


# def your_view(request):
#     main_menu = draw_menu('main_menu')
#     return render(request, 'menu_template.html', {'main_menu': main_menu})
