from django.urls import include, path
from . import views

urlpatterns = [
  path('welcome', views.welcome),
  path('getexpenses/', views.get_expenses),
  path('addexpense/', views.add_expense),
]
