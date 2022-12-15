from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('notes/<username>/', views.notes, name='notes'),#broken access control: users can see other users' notes using the address field
    path('login/', views.user_login, name='user_login'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='user_logout'),
]