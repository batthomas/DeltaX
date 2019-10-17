from django.db import models


class Tag(models.Model):
    tag = models.CharField(max_length=30, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.tag
