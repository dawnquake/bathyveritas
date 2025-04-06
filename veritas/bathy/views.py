from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')

def case_studies(request):
    return render(request, 'case_studies.html')

def benchmarking(request):
    return render(request, 'benchmarking.html')

def product_offering(request):
    return render(request, 'product_offering.html')

def contact_us(request):
    return render(request, 'contact_us.html')

def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
