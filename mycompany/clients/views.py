from django.shortcuts import render, redirect
from .forms import ApplyForm
from .models import Apply

# Create your views here.

def home(request):
    context = {}
    return render(request, 'clients/home.html', context)


def about(request):
    context = {}
    return render(request, 'clients/about.html', context)

def services(request):
    context = {}
    return render(request, 'clients/services.html', context)

def contact(request):
    context = {}
    return render(request, 'clients/contact.html', context)


def apply(request):
    form = ApplyForm()
    if request.method == 'POST':
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'form': form}
    return render(request, 'clients/apply.html', context)