from django.shortcuts import render
from django .http import HttpResponse, response
from .models import Wine
# Create your views here.


#accede directamente a templates
#site pages
def inicio(request):
    return render(request, 'pages/index.html')
def about(request):
    return render(request, 'pages/about.html')
#crud pages
def wines(request):#agregando los objectos para mostrar en la vista
    wines = Wine.objects.all()
    return render(request, 'wine/crud.html', {'wines': wines})
def add_wine(request):
    return render(request, 'wine/create.html')
def edit(request):
    return render(request, 'wine/edit.html')

