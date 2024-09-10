from django import forms
from .models import Employee, Department, Role, Profile, Attendance, LeaveRequest
from businessapp.models import Company
from django.contrib.auth.models import User


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'company']

class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ['department','company','description','permissions']

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'employee_id' , 'department','role','company' , 'joining_date', 'salary']

class ProfileForm(forms.ModelForm):
    class Meta:
        model =Profile
        fields = ['user', 'department','role','company']

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = []

class LeaveRequestForm(forms.ModelForm):
    class Meta:
        model = LeaveRequest
        exclude = ['employee', 'approved']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['start_date'].widget = forms.TextInput(attrs={'type': 'date'})
            self.fields['end_date'].widget = forms.TextInput(attrs={'type': 'date'})