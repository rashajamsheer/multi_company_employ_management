from django.db import models
from django.contrib.auth.models import User
from businessapp.models import Company
from django.utils import timezone

class Department(models.Model):
    name = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

from django.contrib.auth.models import Permission
class Role(models.Model):
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    description = models.TextField(null=True, blank=True)
    permissions = models.ManyToManyField(Permission, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.department} - {self.description[:50]}"

class Employee(models.Model):
    name = models.CharField(max_length=255)
    employee_id = models.CharField(max_length=50, unique=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    joining_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.company.name} - {self.role}"


class Attendance(models.Model):
    employee = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    clock_in_time = models.DateTimeField(auto_now_add=True)
    clock_out_time = models.DateTimeField(null=True, blank=True)

    def clock_in(self):
        self.clock_in_time = timezone.now()
        self.save()

    def clock_out(self):
        self.clock_out_time = timezone.now()
        self.save()

    def __str__(self):
        return f"{self.employee.user.username} - {self.date} - In: {self.clock_in_time} Out: {self.clock_out_time}"

class LeaveRequest(models.Model):
    employee = models.ForeignKey(Profile, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Leave request by {self.employee.user.username} from {self.start_date} to {self.end_date}"