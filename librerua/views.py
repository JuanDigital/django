from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpRequest

from .models import alumnos
from .forms import almForm
# Create your views here.

def inicio(request):
    #return HttpResponse('<h1>Bienvenido a Libres Pc</h1>')
     return render(request,'paginas/index.html')#direcciónando un docmumento html
def registro(request):
    formulario=almForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('registro') 
    return render(request,'CRUD/Registro.html',{'formulario':formulario})#direcciónando un docmumento html

def consulta (request):
    alms=alumnos.objects.all()
    print(alms)
    return render(request,'CRUD/Consulta.html',{'alms':alms})#direcciónando un docmumento html

