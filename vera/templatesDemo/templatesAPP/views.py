from django.shortcuts import render
from templatesAPP.models import empleado
# Create your views here.

def empleadoData(request):
    empleados = empleado.objects.all()
    data = {'empleados':empleados}
    return render(request,'templatesApp/index.html',data)