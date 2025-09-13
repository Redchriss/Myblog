from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # who owns the task
    title = models.CharField(max_length=200)  # task title
    description = models.TextField(blank=True)  # optional longer description
    completed = models.BooleanField(default=False)  # done or not
    created_at = models.DateTimeField(auto_now_add=True)  # when task was created

    def __str__(self):
        return self.title
