from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from django.utils import timezone
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    due_date = serializers.DateField(required=False)
    updated_at = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def validate(self, data):
        if self.instance is None and data['due_date'] < timezone.now().date():
            raise serializers.ValidationError(
                "The date cannot be in the past when creating a task!")
        return data

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    class Meta:
        model = Task
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'category', 'title',
            'description', 'is_urgent', 'due_date', 'completed', 'is_owner',
            'profile_id', 'profile_image',
        ]


class TaskDetailSerializer(TaskSerializer):
    category = serializers.ReadOnlyField(source='category.id')
