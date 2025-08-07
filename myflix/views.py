from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from myflix.models import user, stream, lista
from myflix.serializers import userSerializer, streamSerializer, listaSerializer


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