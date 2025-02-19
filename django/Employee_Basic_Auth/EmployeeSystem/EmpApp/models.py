from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    dob = models.DateField()

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class Employee(Person):
    employee_id = models.CharField(max_length=10, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.employee_id}:{self.name}"