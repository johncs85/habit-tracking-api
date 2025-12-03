from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import HabitSerializer
from .models import Habit

class HabitList(generics.ListCreateAPIView):
    queryset = Habit.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = HabitSerializer # tell django what serializer to use

class HabitDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Habit.objects.all().order_by('id')
    serializer_class = HabitSerializer
