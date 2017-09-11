from rest_framework import viewsets
from dinosaurs.serializers import DinosaurSerializer
from dinosaurs.models import Dinosaur
from rest_framework import permissions


class DinosaurViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Dinosaur.objects.all()
    serializer_class = DinosaurSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

