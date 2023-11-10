from django.shortcuts import render, redirect
from .models import Cafe
from .forms import CafeForm

def home(request):
    return render(request, 'cafes/index.html') #come back to the url paths

def add_cafe(request):
    if request == 'POST':
        form = CafeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    else:
        form = CafeForm()
    return render(request, 'cafes/add_cafe.html', {'form': form})

def cafes(request):
    cafes = Cafe.objects.all()
    return render(request, 'cafes/cafes.html', {'cafes': cafes})

