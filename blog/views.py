from django.shortcuts import render, redirect
from .forms import PersonSignUpForm, PersonLoginForm, NewBlogPost


# Create your views here.


def homepage(request):
    return render(request, "homepage.html")


def login(request):
    form = PersonLoginForm()
    if form.is_valid():
        return redirect("homepage.html")
    context = {
        'form':form,
    }
    return render(request, "login.html",context)


def signup(request):
    form = PersonSignUpForm()
    context = {
        'form':form,
    }
    return render(request, "signup.html",context)


def profile(request):
    return render(request, "profile.html")


def newblog(request):
    form = NewBlogPost()
    context = {
        'form':form,
    }
    return render(request, "newpost.html", context)