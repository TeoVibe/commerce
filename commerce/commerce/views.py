from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .forms import LoginForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
user = authenticate(username=username, password=password)
if user is not None:
    login(request, user)
    return redirect('home')
else:
    # display error message
    pass
else:
    form = LoginForm()
    return render(request, 'login.html', {'form': form})

