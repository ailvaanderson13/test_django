from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'


class Employee(models.Model):
    registration = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    department = models.ForeignKey(to=Department, on_delete=models.DO_NOTHING, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.registration} - {self.name}"

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'
