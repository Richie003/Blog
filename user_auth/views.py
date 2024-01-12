from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterForm

# Create your views here.
def RegisterUser(request):
    message = None
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('sign_in')
        else:
            message = 'Please fill in all the fields'
    context = {
        "form":form,
        "message":message
    }
    return render(request, 'sign_up.html', context)

def loginUser(request):
    message = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            message = "User with this username or password does not exist"
    context = {
        "message":message
    }
    return render(request, 'login.html')

def logoutUser(request):
    user = request.user
    logout(request, user)