"""
URL configuration for todo_list project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todolist.views import (
    GetTasksView,
    CreateTaskView,
    GetTaskByIdView,
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', GetTasksView.as_view(), name='get_tasks'),
    path('tasks/create/', CreateTaskView.as_view(), name='create_task'),
    path('tasks/<int:task_id>/', GetTaskByIdView.as_view(), name='get_task_by_id')
]
