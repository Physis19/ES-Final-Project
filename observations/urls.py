from django.urls import path
from . import views

app_name = 'observations'

urlpatterns = [
    path('', views.observation_list, name='observation_list'),
    path('<int:pk>/', views.observation_detail, name='observation_detail'),
    path('create/', views.observation_create, name='observation_create'),
    path('<int:pk>/edit/', views.observation_update, name='observation_update'),
    path('<int:pk>/delete/', views.observation_delete, name='observation_delete'),
]
