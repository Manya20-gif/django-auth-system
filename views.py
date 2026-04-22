
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout


def home(request):
    return render(request, 'home.html')


def register(request):

    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            return redirect('/login/')

    return render(request, 'register.html', {'form': form})


def login_view(request):

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('/login/')
