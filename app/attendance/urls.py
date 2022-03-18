from django.urls import include, path
from rest_framework import routers
from app.attendance import views
from app.attendance.views import EmpleadosList, RegistroViewSet, RegistroList, RegistroDetail

router = routers.DefaultRouter()
router.register(r'registros', views.RegistroViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/all', RegistroList.as_view()),
    path('api/empleados', EmpleadosList.as_view()),
    path('api/registro/<int:pk>/', RegistroDetail.as_view()),
]
