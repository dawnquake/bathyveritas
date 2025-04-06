from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login as LOGIN
from .forms import FileSubmissionForm
from .models import SubmittedFile


def index(request):
    return render(request, 'index.html')

def case_studies(request):
    return render(request, 'case_studies.html')

def benchmarking(request):

    AllSubmittedFiles = SubmittedFile.objects.all()

    print(AllSubmittedFiles)

    return render(request, 'benchmarking.html', {'AllSubmittedFiles': AllSubmittedFiles})

def product_offering(request):
    return render(request, 'product_offering.html')

def contact_us(request):
    return render(request, 'contact_us.html')

def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            LOGIN(request, user)
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


@login_required
def submit_benchmark(request):
    if request.method == 'POST':
        form = FileSubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            submitted_file = form.save(commit=False)
            submitted_file.user = request.user  # Set the logged-in user
            submitted_file.filename = request.FILES['submitted_file'].name  # Set the filename
            submitted_file.save()
            return redirect('benchmarking')  # Redirect to a success page
    else:
        form = FileSubmissionForm()
    return render(request, 'submit_benchmark.html', {'form': form})
