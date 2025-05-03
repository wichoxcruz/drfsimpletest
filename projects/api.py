from .models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_classes = [permissions.AllowAny] #se puede cambiar a is_authenticated para que solo usuarios autenticados puedan consultar al servidor
    serializer_class = ProjectSerializer