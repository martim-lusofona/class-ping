from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .forms import RegisterForm

def register_view(request):
    
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("/authentication/login/")
    
    context = {
        "form": form
    }

    return render(request, "authentication/register.html", context)

def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username = request.POST["username"],
            password = request.POST["password"]
        )
        if user:
            login(request, user)
            return redirect("/")
        else:
            context = {
                "error": "Invalid!",
            }
            return render(request, "authentication/login.html", context)
    
    return render(request, "authentication/login.html")

def logout_view(request):
    logout(request)
    return redirect("/")