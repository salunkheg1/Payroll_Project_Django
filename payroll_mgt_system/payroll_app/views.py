from django.shortcuts import render
from .models import login


# Create your views here.
def index(request):
    return render(request, 'index.html')

#def login_m(request):
#    return render(request, 'login_m.html')

def login_m(request):
    log = login.objects.all()
  #  for log1 in log:
   #     print(log1.user_name)
    return render(request, 'login_m.html',{'log':log})

def company(request):
    return render(request, 'company.html')
def employee(request):
    return render(request, 'employee.html')

def salary(request):
    return render(request, 'salary.html')

def report(request):
    return render(request, 'report.html')






