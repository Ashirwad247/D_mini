from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_activity, name='add_activity'),
    path('activity/<int:pk>/', views.activity_detail, name='activity_detail'),
    path('activity/edit/<int:pk>/', views.edit_activity, name='edit_activity'),
     path('activity/delete/<int:pk>/', views.delete_activity, name='delete_activity'),
    
]
