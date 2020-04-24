from rest_framework import serializers
from app.models import Participant, Workout


class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = '__all__'


class WorkoutSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    class Meta:
        model = Workout
        fields = '__all__'