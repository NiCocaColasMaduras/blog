from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm

# Create your views here.
def add_user(request):
    # получили данные. нужно сохранить юзера в базу
    if request.method == "POST":
        # получаем данные из формы
        user = UserForm(request.POST)
        if user.is_valid():
            user.save()
            return redirect('/')

    # это простой запрос, нужно показать форму
    else:
        form = UserForm()
        return render(request, "add_user.html", {"form": form})
