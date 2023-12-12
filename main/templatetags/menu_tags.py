from django import template
from main.models import MenuItem

register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    active_url = request.path

    menu_items = MenuItem.objects.filter(name=menu_name)
    menu_html = ''

    for item in menu_items:
        menu_html += render_menu_item(item, active_url)

    return menu_html

def render_menu_item(item, active_url):
    active_class = 'active' if item.url == active_url else ''
    submenu_html = ''

    for child in item.children.all():
        submenu_html += render_menu_item(child, active_url)

    return f'<li class="{active_class}"><a href="{item.url}">{item.name}</a><ul>{submenu_html}</ul></li>'
