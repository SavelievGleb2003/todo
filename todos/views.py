from django.shortcuts import render
from rest_framework.generics import ListAPIView

from .serializers import TodoSerializers
from rest_framework import generics
from .models import Todo
# Create your views here.


class ListTodo(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers


class DetailTodo(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers