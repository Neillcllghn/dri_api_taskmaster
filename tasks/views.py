from rest_framework import generics, permissions, filters
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Task
from .serializers import TaskSerializer, TaskDetailSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class TaskList(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
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


class IncompleteTaskCountView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        incomplete_count = Task.objects.filter(
            owner=user, completed=False).count()
        return Response({'incomplete_task_count': incomplete_count},
                        status=status.HTTP_200_OK)


class UrgentTaskCountView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        urgent_count = Task.objects.filter(
            owner=user, completed=False, is_urgent=True).count()
        return Response({'urgent_task_count': urgent_count},
                        status=status.HTTP_200_OK)
