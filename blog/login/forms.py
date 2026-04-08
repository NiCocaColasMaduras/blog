from django import forms
from .models import User, Role

class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ['title']
        labels = {
            'title': 'Название',
        }

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['login', 'password', 'first_name', 'last_name', 'age', 'role']
        labels = {
            'login': 'Логин',
            'password': 'Пароль',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'age': 'Возраст',
            'role': 'Роль',
        }