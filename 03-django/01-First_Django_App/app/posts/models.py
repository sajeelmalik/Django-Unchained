from django.db import models
from datetime import datetime

# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=200, blank=False)
    body = models.TextField()
    created_at = models.DateTimeField(default = datetime.now, blank=True)

    def __str__(self):
        """ Sensible string representation of Posts."""
        return "Post: " + self.title

    class Meta:
        verbose_name_plural = "Posts"