from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from publish.models import Publish
from utils.permissions import IsOwnerOrReadOnly

from .serializer import PublishSerializer




class PublishViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = PublishSerializer
    queryset = Publish.objects.all()



