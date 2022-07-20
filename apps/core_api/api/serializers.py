
from rest_framework.serializers import ModelSerializer
from apps.core_api.models import Department, Employee


class DepartmentSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = ('name', 'email', 'department', 'registration')

    def to_representation(self, obj):
        representation = dict()
        representation["email"] = obj.email
        representation["department"] = obj.department.name if obj.department else 'Nenhum'
        representation["registration"] = obj.registration
        return representation


