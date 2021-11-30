from django.db import models

class AddEmployee (models.Model):
    emp_name = models.CharField(max_length=100)
    emp_id = models.CharField(max_length=10)
    emp_designation = models.CharField(max_length=50)
    emp_age = models.CharField(max_length=10)
    emp_email = models.CharField(max_length=50)
    class Meta:
        db_table='Employee'