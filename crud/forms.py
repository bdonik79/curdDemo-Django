from django import forms
from .models import Employee

# Create from here

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('fullname','phone','emp_code','position')
        labels = {
            'fullname': 'Employee Name',
            'emp_code': 'Employee ID',
            'phone': 'Phone number',
            'position': 'Designation'
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        self.fields['position'].empty_label  = "select"
        self.fields['emp_code'].required = False