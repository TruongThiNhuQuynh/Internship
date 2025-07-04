from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    owner = models.ForeignKey(
        'auth.User',
        related_name='quickstart_snippets',
        on_delete=models.CASCADE
    )
    class Meta:
        ordering = ['created']