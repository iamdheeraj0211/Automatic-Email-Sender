from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    dob = models.DateField()
    doj = models.DateField()


class EmailTemplate(models.Model):
    event_type = models.CharField(max_length=50)
    subject = models.CharField(max_length=200)
    content = models.TextField()


class EmployeeEvent(models.Model):
    EVENT_TYPES = (
        ('Birthday', 'Birthday'),
        ('Work Anniversary', 'Work Anniversary'))
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=50, choices=EVENT_TYPES)
    event_date = models.DateField()


class EmailLog(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)
