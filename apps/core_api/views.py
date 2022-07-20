from django.shortcuts import render
from . import models


def list_employes(request):
    page_title = "FUNCIONÁRIOS CADASTRADOS"
    employees = models.Employee.objects.all()

    context = {
        'page_title': page_title, 'employees': employees
    }

    return render(request, 'list_employees.html', context)
    