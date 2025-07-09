from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_food, name='add_food'),
    path('delete/<int:id>/', views.delete_food, name='delete_food'),
    path('reset/', views.reset_day, name='reset_day'),]