from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import SnackSerializer
from .models import Snack
from .permissions import ReadOnly

class PostSnack(generics.ListCreateAPIView):
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer

class RetrieveSnack(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (ReadOnly,)
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer