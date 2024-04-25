from django.db import models
from django.contrib.auth.models import User

class Dream(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_recorded = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title
