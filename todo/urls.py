from django.urls import path
from . import views

urlpatterns = [
    path('todo_list/',views.todo_list, name = 'todo_list'),
    path('update_todo/<int:pk>/',views.update_todo, name = 'update_todo'),
    path('todo_delete/<int:pk>/',views.todo_delete, name = 'todo_delete'),
]