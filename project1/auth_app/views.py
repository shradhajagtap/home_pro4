from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect


@login_required(login_url="user_urls")
def user_login(request):
    template_name = "auth_app/login.html"
    if request.method == "POST":
        un = request.POST['un']
        pw = request.POST['pw']
        user = authenticate(username=un, password=pw)
        if user:
            login(request, user)
            return redirect("show_urls")
        else:
            return HttpResponse("Enter correct userid or password")
    return render(request, template_name)


def user_signup(request):
    template_name = "auth_app/signup.html"
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("user_urls")
    context = {"form": form}
    return render(request, template_name, context)


def user_logout(request):
    logout(request)
    return redirect("user_urls")


@login_required(login_url="user_urls")
def change_password(request):
    template_name = "auth_app/cpass.html"
    if request.method == "POST":
        old = request.POST['old']
        new = request.POST['new']
        user = request.user
        res = user.check_password(old)
        if res:
            user.set_password(new)
            user.save()
            return redirect("user_urls")
    return render(request, template_name)
