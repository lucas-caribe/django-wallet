from django.urls import include, path
from . import views

urlpatterns = [
  path('welcome', views.welcome),
  path('expenses/', views.get_expenses),
]
