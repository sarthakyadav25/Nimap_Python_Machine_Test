from django.contrib.auth.models import User
from rest_framework import viewsets, status, generics, permissions
from rest_framework.views import APIView
from rest_framework.serializers import ModelSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Client, Project
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.reverse import reverse
from .serializers import (
    ClientSerializer,
    ProjectSerializer,
    ProjectCreateSerializer,
    RegisterSerializer
)
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
@permission_classes([AllowAny])
def api_root(request, format=None):
    return Response({
        'clients': reverse('clients-list', request=request, format=format),
        'projects': reverse('projects-list', request=request, format=format),
        'register': reverse('register', request=request, format=format),
        'token_obtain_pair': reverse('token_obtain_pair', request=request, format=format),
        'token_refresh': reverse('token_refresh', request=request, format=format),
    })

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save()

    @action(detail=True, methods=['post'], url_path='projects')
    def add_project(self, request, pk=None):
        client = self.get_object()
        serializer = ProjectCreateSerializer(data=request.data)
        if serializer.is_valid():
            project = serializer.save(client=client, created_by=request.user)
            project.users.set(serializer.validated_data['users'])
            return Response(ProjectSerializer(project).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(users=self.request.user)

    def get_serializer_class(self):
        if self.action == 'create':
            return ProjectCreateSerializer
        return ProjectSerializer

    def perform_create(self, serializer):
        client_id = self.request.data.get('client_id')
        client = Client.objects.get(id=client_id)
        serializer.save(created_by=self.request.user, client=client)
    
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer
