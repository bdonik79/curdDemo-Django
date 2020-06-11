from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee


# Create your views here.
def emp_list(request):
    context = {'emp_list':Employee.objects.all()}
    return render(request,"empview/emp_list.html", context)


def emp_insert(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request,"empview/emp_form.html",{'form': form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
        return redirect('emp_list')

def emp_del(request, id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('emp_list')