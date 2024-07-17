from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Profile

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}, your account is created successfully.')
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form':form})


def logout_view(request):
    logout(request)

    return render(request, 'users/logout.html')

@login_required
def profilepage(request):
    context = {'request': request}
    return render(request, 'users/profile.html', context)