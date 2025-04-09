from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Actividad

class ActividadListView(ListView):
    model = Actividad
    template_name = "tareas/actividad_list.html"
    context_object_name = "actividades"

class ActividadCreateView(CreateView):
    model = Actividad
    fields = ["titulo", "descripcion", "fecha_vencimiento", "completada"]
    template_name = "tareas/actividad_form.html"
    success_url = reverse_lazy("actividad_list")

class ActividadUpdateView(UpdateView):
    model = Actividad
    fields = ["titulo", "descripcion", "fecha_vencimiento", "completada"]
    template_name = "tareas/actividad_form.html"
    success_url = reverse_lazy("actividad_list")

class ActividadDeleteView(DeleteView):
    model = Actividad
    template_name = "tareas/actividad_confirm_delete.html"
    success_url = reverse_lazy("actividad_list")
