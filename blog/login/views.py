from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import User, Role
from .forms import UserForm, RoleForm
from .decorators import login_required, is_director

def index(request):
    # если в сессии сохранён пользователь - переходим на главную страницу
    if request.session.get('user_id'):
        # получим объект пользователя по его id
        u_id = request.session.get('user_id')
        u = User.objects.get(id=u_id)

        # переходим на главную страницу и передаем туда логин
        return render(request, 'index.html', {'user': u})
    
    # пользователь неавторизован - переходим на форму входа
    else:
        return redirect('/login/')

#====================================
# Авторизация
#====================================

# страница только для авторизованных
@login_required
def for_authorized(request):
    return render(request, 'page_for_authorized.html')

# страница только для директора
@login_required
def for_director(request):
    return render(request, 'page_for_director.html')

# страница только для менеджера
@login_required
def for_manager(request):
    return render(request, 'page_for_manager.html')

def login(request):
    # это get-запрос. нужно показать пустую форму
    if request.method == "GET":
        return render(request, 'login.html')
    
    # пришли данные. значит нужно проверить логин/пароль
    else:
        login = request.POST.get('login')
        password = request.POST.get('pas')

        # проверим что пользователь с таким логином вообще существует
        try:
            user = User.objects.get(login=login)
        except User.DoesNotExist:
            return redirect('/login')

        # пользователь есть. проверим его пароль
        if password != user.password:
            return redirect('/login')

        # сохраним данные пользователя в сессию
        request.session['user_id'] = user.id
        request.session['login'] = user.login
        return redirect('/')

# выйти из системы
def logout_view(request):
    # очистим все данные в сессии
    request.session.flush()
    return redirect('/login')

#====================================
# ПОЛЬЗОВАТЕЛИ
#====================================

# страница со списком ползователей
@login_required
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

            if not request.session.get('user_id'):
                # Перенаправляем на login, если не авторизован
                return redirect('/login')
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
        form = UserForm(instance=u)
        return render(request, "add_user.html", {"form": form})
    
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
        role = RoleForm(request.POST, instance=r)
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