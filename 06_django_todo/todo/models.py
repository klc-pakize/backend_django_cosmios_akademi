from django.db import models

# Create your models here.

class Todo(models.Model):

    PRIORITY = (
        (1, "HIGH"),  # db tutalacak olan kısım, kullanıcı görüntüliyeceği kısım
        (2, "MEDIUM"),
        (3, "LOW")
    )

    task = models.CharField(max_length=50)  # a
    descrpition = models.TextField(blank=True)
    priority = models.SmallIntegerField(choices=PRIORITY, default=3)
    is_done = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task
