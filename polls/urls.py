from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_data', views.add_data, name='add_data'),
    path('get_datas', views.get_datas, name='get_datas'),
]