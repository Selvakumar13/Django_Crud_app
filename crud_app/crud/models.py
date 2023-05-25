from django.db import models

class Task(models.Model):
    Status_choices=(
        ('Completed','Completed'),
        ('Pending','Pending'),
    )
    name=models.CharField(max_length=255)
    status=models.CharField(max_length=20, choices=Status_choices)

    def __str__(self):
        return self.name
