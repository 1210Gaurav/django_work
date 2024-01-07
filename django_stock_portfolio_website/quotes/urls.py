from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('about/', views.about,name="about"),
    path('add_stock/', views.add_stock,name="add_stock"),
    path('delete/<int:stock_id>/<int:flag>/', views.delete,name="delete"),
    path('delete_stock/', views.delete_stock,name="delete_stock"),
]
