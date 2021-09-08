from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # в '' название стратовой страницы.
    # если пусто, то первая страница по умолчанию и будет стартовой

]
