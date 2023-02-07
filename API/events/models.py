from django.db import models

# Create your models here.
class Events(models.Model):
    Name = models.CharField(max_length=150)
    Date = models.DateField()  
    Title = models.CharField(max_length=150)
    Description = models.TextField(max_length=40000)
    Image = models.CharField(max_length=40000)
    Venue = models.CharField(max_length=150)
    Duration = models.CharField(max_length=150)






