from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('allgames/', views.game_list_view, name='allgames'),
    path('test/', views.test, name='test'),
    path('games/json/', views.game_list_json, name='game_list_json'),
    # path('allgames/', views.allgames, name='allgames'),
]

