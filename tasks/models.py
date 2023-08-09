from django.db import models
from django.contrib.auth.models import User
from category.models import Category


class Task(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_urgent = models.BooleanField(default=False)
    due_date = models.DateField(null=False)
    completed = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at', '-is_urgent']

    def __str__(self):
        return self.title
