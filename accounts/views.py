from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import User
from django.http import HttpResponse

def login_view(request):
    if request.user.is_authenticated:
        messages.info(request, "Вы уже вошли в систему. Сначала выйдите.")
        return redirect("index")
    if request.method == 'POST':
        uname = request.POST.get("username", "")
        passwd = request.POST.get("password", "")
        user = authenticate(username=uname, password=passwd)
        if user is not None:
            login(request, user)
            messages.success(request, "Вход выполнен успешно.")
            return redirect("index")
        else:
            messages.warning(request, "Неверное имя пользователя или пароль!")
    return render(request, "accounts/login.html")

@login_required(login_url='accounts:login')
def logout_view(request):
    logout(request)
    messages.info(request, "Вы успешно вышли из аккаунта!")
    return redirect("accounts:login")

def register_view(request):
    if request.user.is_authenticated:
        messages.info(request, "Вы уже вошли в систему.")
        return redirect("index")
    if request.method == 'POST':
        data = request.POST
        passwd1 = data.get("password1", "")
        passwd2 = data.get("password2", "")
        if passwd1 and (passwd1 != passwd2):
            messages.warning(request, "Пароли не совпадают.")
            return redirect("accounts:register")

        email, username, firstname = data.get("email"), data.get("username"), data.get("firstname")
        if not (email and username and firstname):
            messages.info(request, "Требуется указать адрес электронной почты, имя пользователя и имя.")
            return redirect("accounts:register")

        user = User.objects.filter(Q(email=email) | Q(username=username))
        if not user.exists():
            user = User(email=email, username=username, first_name=firstname)
            if lastname := data.get("lastname"):
                user.last_name = lastname
            user.set_password(passwd1)
            user.save()
            messages.success(request, "Пользователь создан успешно!")
            login(request, user)
            messages.success(request, "Вы вошли!")
            return redirect("index")

        messages.info(request, "Пользователь с такими данными уже существует")
        return redirect("accounts:register")

    return render(request, "accounts/register.html")