from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth import logout
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            #user = form.save(commit=False)
            #user.is_staff = True
            user = form.save()
            login(request, user)
            return redirect('checkout')
    else:
        form = RegistrationForm()
    return render(request, 'account/register.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('checkout')
    else:
        form = AuthenticationForm()
    return render(request,'account/login.html',{'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

