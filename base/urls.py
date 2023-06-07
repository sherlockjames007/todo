from . import views
from django.urls import path, include


app_name = 'base'
urlpatterns = [
    path('api/', include('base.api.urls')), # includes urls for api
    path('login/', views.login, name = 'login'), # url for login page
    path('register/', views.register, name = 'register'), # url for register page
    path('', views.home, name = 'home'), # url for home page
]