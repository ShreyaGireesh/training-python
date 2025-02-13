from django.db import models

# Create your models here.
class Students(models.Model):
    gender_choices = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    name = models.CharField(max_length=255, null=True)
    dob = models.DateField()
    gender = models.CharField(max_length=1, choices=gender_choices)
    address = models.TextField(blank=True, null=True)
    phone_no = models.CharField(max_length=15, blank=True, null=True)
    standard = models.CharField(max_length=10)
    age = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.name}:{self.standard}"