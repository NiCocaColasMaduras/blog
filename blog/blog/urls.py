from django.urls import path
from login import views

urlpatterns = [
    path('', views.index),
    path('login/', views.login),
    path('logout/', views.logout_view),

    path('add_user/', views.add_user),
    path('users/', views.users),
    path('edituser/<int:id_user>', views.edit_user),
    path('deleteuser/<int:id_user>', views.delete_user),

    path('add_role/', views.add_role),
    path('roles/', views.roles),
    path('editrole/<int:id_role>', views.edit_role),
    path('deleterole/<int:id_role>', views.delete_role),

    path('page1/', views.for_authorized),
    path('page2/', views.for_director),
]