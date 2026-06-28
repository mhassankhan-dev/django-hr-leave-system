from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'), # Main page
    path('apply/', views.apply_leave, name='apply_leave'), # Apply karne ka page
]