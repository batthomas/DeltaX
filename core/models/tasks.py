from django.db import models


class Task(models.Model):
    task = models.TextField()
    approach = models.TextField()
    answer = models.TextField()
    tags = models.ManyToManyField("Tag", related_name="tasks")
    user = models.ForeignKey("UserProfile", related_name="tasks", on_delete=models.PROTECT)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
