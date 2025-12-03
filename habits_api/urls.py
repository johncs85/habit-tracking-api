from django.urls import path
from . import views

urlpatterns = [
    path('api/habits', views.HabitList.as_view(), name='habit_list'), # api/habits will be routed to the HabitList view for handling
    path('api/habits/<int:pk>', views.HabitDetail.as_view(), name='habit_detail'), # api/habits will be routed to the HabitDetail view for handling
]
