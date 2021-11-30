from django.shortcuts import render
from ventunotech.models import AddEmployee
from django.contrib import messages
from django.http import HttpResponse

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
    view = "template_two"
    # return render(request, "employee.html", {'name': view})
    return render(request, 'list-employees.html')

def deleteEmployee(request):
    view = "template_two"
    # return render(request, "employee.html", {'name': view})
    return render(request, 'delete-employee.html')

def updateEmployee(request):
    view = "template_two"
    # return render(request, "employee.html", {'name': view})
    return render(request, 'update-employee.html')           