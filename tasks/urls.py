from django.urls import path
from tasks import views

urlpatterns = [
    path('tasks/', views.TaskList.as_view()),
    path('tasks/<int:pk>/', views.TaskDetail.as_view()),
    path('incomplete-task-count/', views.IncompleteTaskCountView.as_view(),
         name='incomplete-task-count'),
    path('urgent-task-count/', views.UrgentTaskCountView.as_view(),
         name='urgent-task-count'),
]
