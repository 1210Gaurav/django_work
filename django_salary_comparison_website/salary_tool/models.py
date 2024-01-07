from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=100)

class SalaryData(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    experience_years = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)
