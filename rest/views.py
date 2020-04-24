from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.models import Participant
from app.serializers import ParticipantSerializer, WorkoutSerializer

# Create your views here.
@api_view(['POST'])
def post_participant(request):
    data = {'name': request.data.get('name'),
            'nickname': request.data.get('nickname'),
            'tele_id': request.data.get('tele_id'),
            'unit': request.data.get('unit'),
            'pes': request.data.get('pes'),
            'status': request.data.get('status')
            }

    serializer = ParticipantSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response("Participant Recorded.", status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def post_workout(request):
    participant = get_object_or_404(Participant, tele_id=request.data.get('tele_id')).pk
    data = {'participant': participant,
            'date': request.data.get('date'),
            'duration': request.data.get('duration'),
            'activity': request.data.get('activity'),
            'calories': request.data.get('calories')
            }

    serializer = WorkoutSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response("Workout Recorded.", status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


