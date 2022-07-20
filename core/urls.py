from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers
from apps.core_api.api.viewsets import EmployeeViewSet, DepartmentViewSet
from rest_framework_swagger.views import get_swagger_view
from apps.core_api.views import list_employes

schema_view = get_swagger_view(title='IGS-API')

router = routers.DefaultRouter()
router.register(r'employee', EmployeeViewSet)
router.register(r'department', DepartmentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list_employes/', list_employes, name="list_employee"),
    path('', include(router.urls)),
]

urlpatterns += [
    url(r'', schema_view)
]