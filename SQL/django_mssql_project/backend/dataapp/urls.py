from django.urls import path
from . import views

urlpatterns = [
    path('api/employees/', views.fetch_employees, name='fetch-employees'),
]