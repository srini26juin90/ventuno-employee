from django.shortcuts import render
from ventunotech.models import AddEmployee
from django.contrib import messages
from django.http import HttpResponse
from ratelimit.decorators import ratelimit
import pickle
import json

@ratelimit(key='ip', rate='5/m', method=['GET', 'POST'])
def addEmployee(request):
    if request.method == 'POST':
        if request.POST.get('emp_name') and request.POST.get('emp_email') and request.POST.get('emp_age') and request.POST.get('emp_designation'):
            saverecord = AddEmployee()
            saverecord.emp_name = request.POST.get('emp_name')
            saverecord.emp_email = request.POST.get('emp_email')
            saverecord.emp_age = request.POST.get('emp_age')
            saverecord.emp_designation = request.POST.get('emp_designation')
            saverecord.save()
            messages.success(request, 'Records saved successfully')
            return render(request, 'add-employee.html')
    else:
        return render(request, 'add-employee.html')        

# from django.shortcuts import render
# from django.http import HttpResponse
# # Create your views here.
def listEmployee(request):
    data = AddEmployee.objects.all()
    employee = {
        "employeeData": data
    }
    print(employee)
    
    return render(request, 'list-employees.html', employee)

def deleteEmployee(request):
    return render(request, 'delete-employee.html')

def updateEmployee(request):
    return render(request, 'update-employee.html')           