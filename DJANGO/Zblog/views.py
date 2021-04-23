from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import RegisterForm


def register_user(request) -> RegisterForm:   
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {name}!')
            return redirect('/login/')
        error = form.errors
        return render(request, 'register.html', {"form": form})
    form = RegisterForm()
    return render(request, 'register.html', {"form": form})


def index(request):
    return render(request, "index.html")
