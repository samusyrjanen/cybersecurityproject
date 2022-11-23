from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/<str:account>/', views.notes, name='notes')
]