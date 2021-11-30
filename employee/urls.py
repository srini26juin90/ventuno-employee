from django.urls import path
from . import views

urlpatterns=[
    # path("",views.listEmployees,name="Employee"),
    path("EmployeeDetails",views.listEmployee,name="EmployeeDetails"),
    path("AddEmployee",views.addEmployee,name="addemployee"),
    path("UpdateEmployee",views.updateEmployee,name="UpdateEmployee"),
    path("DeleteEmployee",views.deleteEmployee,name="DeleteEmployee"),
]