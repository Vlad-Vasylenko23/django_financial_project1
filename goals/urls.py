from django.urls import path
from . import views

app_name = "goals"

urlpatterns = [
    path('list/', views.goals_list, name='goals_list'),
    path('add/', views.add_goal, name='add_goal'),
    path("update/<int:goal_id>/", views.update_goal_progress, name="update_goal_progress"),
]
