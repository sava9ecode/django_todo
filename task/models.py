from django.contrib.auth.models import User
from django.db import models

from category.models import Category


class Task(models.Model):
    user = models.ForeignKey(User, related_name="tasks", on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category, related_name="tasks", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
