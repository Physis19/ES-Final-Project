from django.urls import path
from . import views

app_name = 'labs'

urlpatterns = [
    path('', views.lab_list, name='lab_list'),
    path('<int:pk>/', views.lab_detail, name='lab_detail'),
    path('create/', views.lab_create, name='lab_create'),
    path('<int:pk>/edit/', views.lab_update, name='lab_update'),
    path('<int:pk>/delete/', views.lab_delete, name='lab_delete'),
]