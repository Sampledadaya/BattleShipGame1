# urls.py
from django.contrib import admin
from django.urls import path
from game import views  # Импортируем views из приложения game

urlpatterns = [
    path('admin/', admin.site.urls),  # Маршрут для административной панели
    path('', views.index, name='index'),  # Главная страница
    path('game/<int:game_id>/', views.game_view, name='game'),  # Страница игры
]
