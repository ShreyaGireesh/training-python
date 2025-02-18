from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    dob = models.DateField()

    class Meta:
        abstract = True
    
    def __str__(self):
        return f"{self.name}"

class Employee(Person):
    employee_id = models.CharField(max_length=10, unique=True)
    is_active = models.BooleanField(default = True)

    def __str__(self):
        return f"{self.name}, Employee ID: {self.employee_id}"

class Manager(Employee):
    department = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Manager: {self.name}, Dept: {self.department}"

class Developer(Employee):
    programming_languages = models.CharField(max_length=200)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Developer: {self.name}, Languages: {self.programming_languages}"

class ActiveEmployee(Employee):
    class Meta:
        proxy = True  

    def is_active_employee(self):
        return self.is_active

class InactiveEmployee(Employee):
    class Meta:
        proxy = True  

    def is_inactive_employee(self):
        return not self.is_active
