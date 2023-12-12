
from django.urls import path


from .views import menu_view

urlpatterns = [
    path('', menu_view, name='your_view_name'),
]
