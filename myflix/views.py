from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets, generics
from myflix.models import user, stream, lista
from myflix.serializers import (
    userSerializer,
    streamSerializer,
    listaSerializer,
    listaUserSerializer,
    listaStreamSerializer
)

# Create your views here.
class userViewSet(viewsets.ModelViewSet):
    queryset = user.objects.all()
    serializer_class = userSerializer

class streamViewSet(viewsets.ModelViewSet):
    queryset = stream.objects.all()
    serializer_class = streamSerializer

class listaViewSet(viewsets.ModelViewSet):
    queryset = lista.objects.all()
    serializer_class = listaSerializer

class listaUser(generics.ListAPIView):
    def get_queryset(self):
        queryset = lista.objects.filter(user_id=self.kwargs['pk'])
        return queryset

    serializer_class = listaUserSerializer

class listaStream(generics.ListAPIView):
    def get_queryset(self):
        queryset = lista.objects.filter(stream=self.kwargs['pk'])

    serializer_class = listaStreamSerializer