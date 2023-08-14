from django.db import models

from django.contrib.auth.models import User
# Create your models here.
 
class Departman(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Personel(models.Model):

    TITLE = (
        ("Team Lead", "LEAD"),
        ("Mid Lead", "MID"),
        ("Juinor", "JUN"),
    )

    GENDER = (
        ("Female", "F"),
        ("Male", "M"),
        ("Other", "O"),
    )

    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=50)
    title = models.CharField(max_length=10, choices=TITLE)
    gender = models.CharField(max_length=6, choices=GENDER)
    salary = models.PositiveIntegerField(default=30000)
    start_date = models.DateTimeField(auto_now_add=True)
    departman = models.ForeignKey(Departman, on_delete=models.SET_NULL, null=True, related_name='personels')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return f"{self.first_name} - {self.last_name} - {self.title}"