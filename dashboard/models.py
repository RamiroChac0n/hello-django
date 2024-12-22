from django.db import models

# Create your models here.
class Professor(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True, null=False)
    age = models.IntegerField()

    def __str__(self):
        return self.name