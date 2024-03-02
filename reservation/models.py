from django.db import models

# Create your models here.

class Reservation(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    
    name = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    def __str__(self):
        return f"{self.name} on {self.date} at {self.time}"

