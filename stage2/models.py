from django.db import models


# Create your models here.
class Arithmetic(models.Model):
    operation_type = models.CharField(max_length=15)
    x = models.IntegerField()
    y = models.IntegerField()

    def __str__(self):
        return f"{self.x} {self.operation_type} {self.y}"
