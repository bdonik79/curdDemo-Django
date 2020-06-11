from django.db import models

# Create your models here.

class   products(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, default='')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Position(models.Model):
    title = models.CharField(max_length=60)

    def __str__(self):
        return self.title

class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=3)
    phone = models.CharField(max_length=15)
    position = models.ForeignKey(Position,on_delete=models.CASCADE)