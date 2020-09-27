from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseServerError
from .form import LoginForm
from django.contrib.auth import authenticate
from django.contrib.auth import login

# Create your views here.

def loginTest(request):
    if (request.method == "GET"):
        login_f = LoginForm()
        return render(request, "login.html", {"form": login_f})
    elif (request.method == "POST"):
        login_f = LoginForm(request.POST)
        if login_f.is_valid():
            cd = login_f.cleaned_data
            user = authenticate(
                username=cd['username'], password=cd['password'])
            if (user):
                login(request, user)
                return HttpResponse("login ok")
            else:
                return HttpResponse("Failed to login")
        else:
            return HttpResponse("Invalid data")
    return HttpResponseServerError("Unimplemented Method")