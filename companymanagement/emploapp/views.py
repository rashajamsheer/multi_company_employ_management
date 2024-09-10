from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Employee, Department, Role, Profile, Attendance, LeaveRequest
from .forms import EmployeeForm, DepartmentForm, RoleForm, ProfileForm, AttendanceForm, LeaveRequestForm
from django.http import JsonResponse
# Create your views here.


# List all employees
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})



def employee_create(request):
    if request.method == 'POST':
        employee_form = EmployeeForm(request.POST, request.FILES)
        profile_form = ProfileForm(request.POST, request.FILES)

        if employee_form.is_valid() and profile_form.is_valid():
            employee = employee_form.save()
            profile = profile_form.save(commit=False)
            profile.user = request.user
            profile.employee = employee
            profile.save()

            return redirect('emploapp:employee_list')

    else:
        employee_form = EmployeeForm()
        profile_form = ProfileForm()

    return render(request, 'employee_form.html', {
        'employee_form': employee_form,
        'profile_form': profile_form
    })

from django.utils import timezone
def profile_view(request):
    profile = get_object_or_404(Profile, user=request.user)
    today = timezone.now().date()
    attendance_today = Attendance.objects.filter(employee=profile, date=today).first()
    leave_requests = LeaveRequest.objects.filter(employee=profile)

    return render(request, 'profile.html', {
        'profile': profile,
        'attendance_today': attendance_today,
        'leave_requests': leave_requests
    })


# Update an existing employee
def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('emploapp:employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employee_form.html', {'form': form})

# Delete an employee
def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('emploapp:employee_list')
    return render(request, 'employee_confirm_delete.html', {'employee': employee})


# Department CRUD
def department_list(request):
    department = Department.objects.all()
    return render(request, 'department_list.html', {'department': department})


def department_create(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('emploapp:department_list')
    else:
        form = DepartmentForm()
    return render(request, 'department_form.html', {'form': form})

def department_update(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('emploapp:department_list')
    else:
        form = EmployeeForm(instance=department)
    return render(request, 'department_form.html', {'form': form})

def department_delete(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        department.delete()
        return redirect('emploapp:department_list')
    return render(request, 'department_confirm_delete.html', {'department': department})

def role_list(request):
    roles = Role.objects.all()
    return render(request, 'role_list.html', {'roles': roles})

def role_create(request):
    if request.method == 'POST':
        form = RoleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('emploapp:role_list')
    else:
        form = RoleForm()
    return render(request, 'role_form.html', {'form': form})

def role_update(request, pk):
    role = get_object_or_404(Role, pk=pk)
    if request.method == 'POST':
        form = RoleForm(request.POST, instance=role)
        if form.is_valid():
            form.save()
            return redirect('emploapp:role_list')
    else:
        form = RoleForm(instance=role)
    return render(request, 'role_form.html', {'form': form})

def role_delete(request, pk):
    role = get_object_or_404(Role, pk=pk)
    if request.method == 'POST':
        role.delete()
        return redirect('emploapp:role_list')
    return render(request, 'role_confirm_delete.html', {'role': role})



def clock_in_view(request):
    profile = get_object_or_404(Profile, user=request.user)
    attendance = Attendance(employee=profile)
    attendance.clock_in()
    return redirect('profile')

def clock_out_view(request):
    profile = get_object_or_404(Profile, user=request.user)
    attendance = Attendance.objects.filter(employee=profile, clock_out_time__isnull=True).first()
    if attendance:
        attendance.clock_out()
    return redirect('profile')

from django.contrib import messages
def leave_request_view(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        form = LeaveRequestForm(request.POST)
        if form.is_valid():
            leave_request = form.save(commit=False)
            leave_request.employee = profile# Assign the current user's profile
            leave_request.save()# Save the leave request object
            messages.success(request, 'Leave request submitted successfully.')
            return redirect('emploapp:profile')
        else:
            print("Form is not valid.",form.errors)
            messages.error(request, "There was an error submitting your leave request. Please try again.")
    else:
        form = LeaveRequestForm()

    return render(request, 'leave_request_form.html', {'form': form})
