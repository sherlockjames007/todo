# this file contains the urls for the application programming interface of this project
# all urls referring the api of this project start with "/base/api"

from . import views
from django.urls import path

urlpatterns = [
    path('login/', views.login_user, name = 'login'),
    path('register/', views.register_user, name = 'register'),
    path('home/', views.home, name = 'home'),
    path('logout/', views.logout_user, name = 'logout'),
    path('checkbox_toggle/', views.checkbox_toggle, name = 'checkbox_toggle'),
    path('add_task/', views.add_task, name = 'add_task'),
    path('delete_task/', views.delete_task, name = 'delete_task'),
]