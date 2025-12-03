from rest_framework import serializers 
from .models import Habit 

class HabitSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = Habit # tell django which model to use
        fields = ('id', 'name', 'description', 'category', 'start_date', 'end_date', 'completed', 'duration') # tell django which fields to include
