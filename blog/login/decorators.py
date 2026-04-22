from django.shortcuts import redirect, render
from .models import User

def login_required(func):
    """
    Проверяет, вошёл ли пользователь в систему.
    Если нет – перенаправляет на страницу входа.
    """
    def wrapper(request, *args, **kwargs):
        if not request.session.get('user_id'):
            # Перенаправляем на login, если не авторизован
            return redirect('/login')
        return func(request, *args, **kwargs)
    return wrapper

def is_director(func):
    """
    Проверяет, является ли пользователь директором.
    Если нет — перенаправляет на страницу с ошибкой.
    """
    # сначала применяем login_required
    @login_required

    def wrapper(request, *args, **kwargs):
        # получаем пользователя и смотрим его роль
        id_user = request.session.get('user_id')
        user = User.objects.get(id=id_user)
        if user:
            if user.role.id == 1:
                return func(request, *args, **kwargs)
            else:
                message = 'Пользователь должен быть Директором'
        else:
            message = 'Пользователь не найден в базе'
        return render(request, 'error.html', {'message': message})
    return wrapper

def is_manager(func):
    """
    Проверяет, является ли пользователь менеджером.
    Если нет — перенаправляет на страницу с ошибкой.
    """
    # сначала применяем login_required
    @login_required

    def wrapper(request, *args, **kwargs):
        # получаем пользователя и смотрим его роль
        id_user = request.session.get('user_id')
        user = User.objects.get(id=id_user)
        if user:
            if user.role.id == 2:
                return func(request, *args, **kwargs)
            else:
                message = 'Пользователь должен быть Мене'
        else:
            message = 'Пользователь не найден в базе'
        return render(request, 'error.html', {'message': message})
    return wrapper