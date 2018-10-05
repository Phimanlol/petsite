from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from utils.permissions import IsOwnerOrReadOnly
from .models import Pet


from .serializer import PetsSerializer


class PetsViewSet(viewsets.ModelViewSet):
    serializer_class = PetsSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        return Pet.objects.filter(user=self.request.user)


