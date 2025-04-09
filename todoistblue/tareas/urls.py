from django.urls import path
from .views import (
    ActividadListView,
    ActividadCreateView,
    ActividadUpdateView,
    ActividadDeleteView,
)

urlpatterns = [
    path("", ActividadListView.as_view(), name="actividad_list"),
    path("crear/", ActividadCreateView.as_view(), name="actividad_create"),
    path("editar/<int:pk>/", ActividadUpdateView.as_view(), name="actividad_update"),
    path("borrar/<int:pk>/", ActividadDeleteView.as_view(), name="actividad_delete"),
]
