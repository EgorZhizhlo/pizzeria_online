from django.urls import path
from . import views


app_name = 'pizza'

urlpatterns = [
    path('', views.pizza_list, name='pizza_list'),
    path('<int:pk>', views.pizza_detail, name='pizza_detail')
]
