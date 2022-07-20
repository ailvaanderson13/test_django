from rest_framework.viewsets import ModelViewSet
from apps.core_api.models import Employee, Department
from apps.core_api.api.serializers import EmployeeSerializer, DepartmentSerializer


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer