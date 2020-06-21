from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.show, name='show'),
    path('creat', views.creat, name='creat'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('search', views.search, name='search'),
]