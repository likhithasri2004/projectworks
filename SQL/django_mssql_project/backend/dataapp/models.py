from django.db import models

class Employees(models.Model):
    EmpID = models.IntegerField(primary_key=True, db_column='EmpID')
    EmpName = models.CharField(max_length=100, db_column='EmpName')
    Email = models.EmailField(db_column='Email')
    Salary = models.DecimalField(max_digits=10, decimal_places=2, db_column='Salary')
    JoinDate = models.DateField(db_column='JoinDate')
    IsActive = models.BooleanField(db_column='IsActive')

    class Meta:
        db_table = 'employees'
        managed = False
