from django.shortcuts import render
from django.http import HttpResponse
from statistics import median

from .models import SalaryData

def calculate_comparison_result(monthly_salary, median_salary):
    median_salary_float = float(median_salary)  # Convert median_salary to a float

    if monthly_salary < median_salary_float:
        return f"Your ${monthly_salary:.2f} monthly salary is {100 - (monthly_salary / median_salary_float) * 100:.2f}% below the median salary."
    else:
        return f"Your ${monthly_salary:.2f} monthly salary is {((monthly_salary / median_salary_float) - 1) * 100:.2f}% higher than the median salary."

def compare_salary(request):
    if request.method == 'POST':
        job_title = request.POST.get('job_title')
        monthly_salary = float(request.POST.get('monthly_salary'))
        experience_years = request.POST.get('experience_years')
        gender = request.POST.get('gender', None)

        queryset = SalaryData.objects.filter(job__title=job_title, salary__gte=monthly_salary)
        if experience_years:
            experience_years = int(experience_years) 
            queryset = queryset.filter(experience_years=experience_years)
        if gender:
            queryset = queryset.filter(gender=gender)

        salaries = [entry.salary for entry in queryset]
        if not salaries:
         
           comparison_result=f"For your ${monthly_salary:.2f} monthly salary we do not have data currently! Will update you after a while."
           context = {
                'comparison_result': comparison_result,
            }

            
        else:

            median_salary = median(salaries)

            comparison_result = calculate_comparison_result(monthly_salary, median_salary)

            context = {
                'monthly_salary': monthly_salary,
                'comparison_result': comparison_result,
            }
        return render(request, 'salary_tool/result.html', context)

    return render(request, 'salary_tool/form.html')
