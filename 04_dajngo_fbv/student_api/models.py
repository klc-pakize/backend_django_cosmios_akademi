from django.db import models

# Create your models here.
class Path(models.Model):
    path_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.path_name}"
    

class Student(models.Model):
    path = models.ForeignKey(Path, on_delete=models.CASCADE, related_name='students')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    number = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"