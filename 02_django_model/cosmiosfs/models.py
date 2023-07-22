from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    number = models.PositiveSmallIntegerField(blank=True, null=True)
    about = models.TextField(blank=True)
    email = models.EmailField()
    register_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    avatar = models.ImageField(blank=True, null=True, upload_to='student')

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ["-number"]
        verbose_name_plural = "Student-List"