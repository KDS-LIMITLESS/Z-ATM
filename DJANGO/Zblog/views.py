from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm



def register_user(request) -> RegisterForm:   
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('firstName')
            messages.success(request, f'Account created for {name}!')
            return redirect('/login/')
        error = form.errors
        return render(request, 'register.html', {"form": form})
    form = RegisterForm()
    return render(request, 'register.html', {"form": form})


def login_user(request) -> RegisterForm:
    login_form = AuthenticationForm()
    return render(request, "login.html", {"login_form": login_form})
