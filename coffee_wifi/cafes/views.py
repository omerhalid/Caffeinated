from django.shortcuts import render, redirect
from .models import Cafe
from .forms import CafeForm

def home(request):
    return render(request, 'cafes/index.html')

def add_cafe(request):
    if request.method == 'POST':
        form = CafeForm(request.POST)
        if form.is_valid():
            form.save()
            print('saved')  # This will print to your console where the server is running.
            return redirect('home')
        else:
            print('Form is not valid')  # It's useful to know if the form didn't validate
            print(form.errors)  # Printing the form errors can help you debug
    else:
        form = CafeForm()
    return render(request, 'cafes/add.html', {'form': form})

def cafes(request):
    cafes = Cafe.objects.all()
    return render(request, 'cafes/cafes.html', {'cafes': cafes})

