from django.shortcuts import render, redirect
from django .http import HttpResponse, response
from .models import Wine
from .forms import WineForm
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
    wi_form = WineForm(request.POST or None, request.FILES or None)
    if wi_form.is_valid():
        wi_form.save()
        return redirect('wines')
    return render(request, 'wine/create.html', {'wi_form':wi_form})

def edit(request):
    return render(request, 'wine/edit.html')

