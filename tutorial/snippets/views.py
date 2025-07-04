from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from .models import Snippet
from .serializers import SnippetSerializer

class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

from .permissions import IsOwnerOrReadOnly

from rest_framework import viewsets
from .models import Snippet
from .serializers import SnippetSerializer

class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer