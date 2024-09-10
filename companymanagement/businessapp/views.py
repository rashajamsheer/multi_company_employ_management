from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Company
from .forms import CompanyForm

# List companies
def company_list(request):
    companies = Company.objects.all()
    print(companies)
    return render(request, 'company_list.html', {'companies': companies})

# Create a new company
def company_create(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Company created successfully.')
            return redirect('businessapp:company_list')
    else:
        form = CompanyForm()
    return render(request, 'company_form.html', {'form': form})

# Update an existing company
def company_update(request, pk):
    company = get_object_or_404(Company, pk=pk)
    if request.method == 'POST':
        form = CompanyForm(request.POST, request.FILES, instance=company)
        if form.is_valid():
            form.save()
            messages.success(request, 'Company updated successfully.')
            return redirect('businessapp:company_list')
    else:
        form = CompanyForm(instance=company)
    return render(request, 'company_form.html', {'form': form})

# Delete a company
from django.shortcuts import render, redirect, get_object_or_404
from .models import Company


def company_delete(request, pk):
    company = get_object_or_404(Company, pk=pk)

    # Check for related records
    if (company.department_set.exists() or
            company.employee_set.exists() or
            company.profile_set.exists() or
            company.role_set.exists()):
        error_message = "Cannot delete this company because it has associated records."
        return render(request, 'company_delete.html', {'company': company, 'error_message': error_message})

    if request.method == 'POST':
        company.delete()
        return redirect('businessapp:company_list')

    return render(request, 'company_delete.html', {'company': company})


def index(request):
    return render(request, 'home.html')




