from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Snack(models.Model):
    purchaser = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name