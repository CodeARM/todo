from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="list"),
    path('where/', views.where),
    path('when/', views.when),
    path('project/', views.project),
    path('area/', views.area),
    path('update_task/<str:pk>/', views.updateTask, name="update_task"),
    path('delete/<str:pk>/', views.deleteTask, name="delete"),

]