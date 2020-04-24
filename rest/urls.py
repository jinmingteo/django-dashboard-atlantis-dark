from django.urls import path
from rest import views

urlpatterns = [
    path('workout/post', views.post_workout, name="workout_post"),
    path('participant/post', views.post_participant, name="participant_post")
]