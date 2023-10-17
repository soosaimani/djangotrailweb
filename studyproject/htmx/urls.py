from django.urls import path
from . import views

urlpatterns = [
    path('task_list/',views.task_list,name='task_list'),
    #path('toggle_task/<int:task_id>/',views.toggle_task,name='toggle_task'),
    path('clicked/',views.clicked,name='clicked')
]
