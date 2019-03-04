from django.db import models
from datetime import date
from django.contrib.auth.models import User


# user model (linked to form)
class FitnessModel(models.Model):
    username = models.CharField(max_length=20, default='')
    password = models.CharField(max_length=20, default='')
    calories = models.DecimalField(decimal_places=2, max_digits=5)
    date = models.DateField(default=date.today)
    userFK = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True )

    def __str__(self):
        return self.username
