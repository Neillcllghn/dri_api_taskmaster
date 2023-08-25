from rest_framework import generics, permissions, filters
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Task
from .serializers import TaskSerializer, TaskDetailSerializer
from django_filters.rest_framework import DjangoFilterBackend


class TaskList(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Task.objects.all()
    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    search_fields = [
        'owner__username',
        'category__category_title',
        'title',
    ]
    filterset_fields = [
        'completed',
        'is_urgent',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = TaskDetailSerializer
    queryset = Task.objects.all()
