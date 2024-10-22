from django.urls import path
from . import views


app_name = 'pizza'

urlpatterns = [
    path('', views.pizza_list, name='list'),
    path('<int:pk>', views.pizza_detail, name='detail')
]