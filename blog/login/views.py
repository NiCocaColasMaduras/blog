from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import User, Role
from .forms import UserForm, RoleForm

def index(request):
    return render(request, 'index.html')

#====================================
# ПОЛЬЗОВАТЕЛИ
#====================================

# страница со списком ползователей
def users(request):
    # получим всех пользователей из базы
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})

def add_user(request):
    # получили данные. нужно сохранить юзера в базу
    if request.method == "POST":
        # получаем данные из формы
        user = UserForm(request.POST)
        if user.is_valid():
            user.save()
            return redirect('/users/')

    # это простой запрос, нужно показать форму
    else:
        form = UserForm()
        return render(request, "add_user.html", {"form": form})

# изменить пользователя
def edit_user(request, id_user):
    # получим пользователя, который нужно редактировать
    u = User.objects.get(id=id_user)

    # получили данные, нужно сохранить пользователя в базу
    if request.method == "POST":
        # получаем данные из формы
        user = UserForm(request.POST, instance=u)
        if user.is_valid():
            user.save()
            return redirect('/users')

    # это простой запрос, нужно показать форму
    else:
        UserForm = UserForm(instance=u)
        return render(request, "add_user.html", {"form": UserForm})
    
# удаление пользователя
def delete_user(request, id_user):
    # получим пользователя из базы данных
    user = User.objects.get(id=id_user)
    # удалим пользователя
    user.delete()
    # покажем сообщение
    return HttpResponse('<h1>Пользователь успешно удалён</h1><br><a href="/users" class="EmptyForm">На главную</a>')

#====================================
# РОЛИ
#====================================

# страница со списком ролей
def roles(request):
    # получим все роли из базы
    roles = Role.objects.all()
    return render(request, 'roles.html', {'roles': roles})

def add_role(request):
    # получили данные. нужно сохранить роль в базу
    if request.method == "POST":
        # получаем данные из формы
        role = RoleForm(request.POST)
        if role.is_valid():
            role.save()
            return redirect('/roles/')

    # это простой запрос, нужно показать форму
    else:
        form = RoleForm()
        return render(request, "add_role.html", {"form": form})
    
# изменить роль
def edit_role(request, id_role):
    # получим роль, который нужно редактировать
    r = Role.objects.get(id=id_role)

    # получили данные, нужно сохранить роль в базу
    if request.method == "POST":
        # получаем данные из формы
        role = UserForm(request.POST, instance=r)
        if role.is_valid():
            role.save()
            return redirect('/roles')

    # это простой запрос, нужно показать форму
    else:
        RoleForm = RoleForm(instance=r)
        return render(request, "add_role.html", {"form": RoleForm})
    
# удаление роли
def delete_role(request, id_role):
    # получим роль из базы данных
    role = Role.objects.get(id=id_role)
    # удалим роль
    role.delete()
    # покажем сообщение
    return HttpResponse('<h1>Роль успешно удалёна</h1><br><a href="/roles" class="EmptyForm">На главную</a>')