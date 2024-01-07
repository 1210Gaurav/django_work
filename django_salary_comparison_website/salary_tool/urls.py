from django.urls import path
from .views import compare_salary

urlpatterns = [
    path('salary/', compare_salary, name='compare_salary'),
]
