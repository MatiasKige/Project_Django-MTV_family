from django.db import models

# Create your models here.

class Familiar(models.Model):
    name=models.CharField(max_length=25, unique=True)
    edad=models.IntegerField()
    parentesco=models.CharField(max_length=15)
    fecha_ingreso=models.DateField(auto_now_add=True,null=True, blank=True)
