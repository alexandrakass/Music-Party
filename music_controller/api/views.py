from django.shortcuts import render
from rest_framework import generics
from .serializers import RoomSerializer
from .models import Room
# Create your views here.

# #view a list of all the different rooms
# class RoomView(generics.CreateAPIView):
#     queryset = Room.objects.all()
#     serializer_class = RoomSerializer
    
class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    