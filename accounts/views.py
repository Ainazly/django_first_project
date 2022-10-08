from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def login_view(request):
    context = {}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username, '\n', password)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is None:
            context = {"error": "Something wrong!"}
        else:
            login(request, user)
            return redirect('/admin')
    return render(request, "accounts/login.html", context)


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('/login/')

    return render(request, "accounts/logout.html", {})


