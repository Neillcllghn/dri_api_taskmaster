from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Task
from .serializers import TaskSerializer, TaskDetailSerializer


class TaskList(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Task.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = TaskDetailSerializer
    queryset = Task.objects.all()
