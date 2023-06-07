# contains all the views for the application programming interface (api) of this project
# returns responses based on the type of request made by the user

from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import User, Tasks
from .serializers import TasksSerializer
from django.contrib.auth import authenticate, login, logout
from django.core.validators import validate_email
from rest_framework import status
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied


# api for logging in user
# takes the email and password as arguments
# tries to login user with the given credentials
# if an error occurs returns the appropriate response
# else logs in user with OK response
@api_view(['POST'])
def login_user(request):
    if request.user.is_authenticated:
        return Response('Invalid request', status = status.HTTP_400_BAD_REQUEST)
    data = request.data
    username = data.get('email')
    password = data.get('password')
    user = authenticate(username = username, password = password)    
    if user is not None:
        login(request._request, user)
        return Response('You are now logged in', status = status.HTTP_200_OK)
    return Response('Invalid credentials', status = status.HTTP_403_FORBIDDEN)



# api for registering new user
# takes the required credentials as arguments (email, password, first_name, last_name)
# tries to create a new user
# if something goes wrong returns an unsuccesful response
# else registers the new user with OK response
@api_view(['POST'])
def register_user(request):
    if request.user.is_authenticated:
        return Response('Invalid request', status = status.HTTP_400_BAD_REQUEST)
    data = request.data
    username = data.get('email')
    password = data.get('password')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    print(username, password, first_name, last_name)
    try:
        user = User.objects.create_user(
            username = username,
            password = password, 
            first_name = first_name,
            last_name = last_name,                       
        )
    except Exception as e:
        print(e)
        return Response('Invalid details', status = status.HTTP_403_FORBIDDEN)
    else:
        try:
            login(request, user)
        except Exception as e:
            print(e)
            return Response('Registration successful, internal server error, please try again later!!!!', status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response('Registration successful, logged in!!!!', status = status.HTTP_200_OK)



# logout user
@login_required
@api_view(['POST'])
def logout_user(request):
    if not request.user.is_authenticated:
        return Response('Invalid request', status = status.HTTP_400_BAD_REQUEST)
    try:
        logout(request._request)
    except:
        return Response('Internal server error, please try again!!!!', status = status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response('Logging out successful', status = status.HTTP_200_OK)


# home page
# returns the list of all the to-do tasks saved by the user
@login_required
@api_view(['GET'])
def home(request):    
    try:
        data = Tasks.objects.filter(user = request.user)
        res = TasksSerializer(data, many = True)
    except:
        return Response('Internal server error, please try again!!!!', status = status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response(res.data, status = status.HTTP_200_OK)


# saves the change in case the checkbox for a to-do task is toggled
@login_required
@api_view(['POST'])
def checkbox_toggle(request):
    data = request.data    
    try:
        t = Tasks.objects.get(id = data['task_id'])
        if (t.user != request.user):
            raise PermissionDenied('user doesnt owns the task')
        t.checked = data['checked']
        t.save()
    except:
        return Response('Invalid request', status = status.HTTP_400_BAD_REQUEST)
    else:
        return Response('checked value changed', status = status.HTTP_200_OK)


# delete task
@login_required
@api_view(['POST'])
def delete_task(request):
    data = request.data    
    try:
        t = Tasks.objects.get(id = data['task_id'])
        if (t.user != request.user):
            raise PermissionDenied('user doesnt owns the task')
        t.delete()
    except Exception as e:
        print(e)
        return Response('Invalid request', status = status.HTTP_400_BAD_REQUEST)
    else:
        return Response('task deleted', status = status.HTTP_200_OK)


# add new task
@login_required
@api_view(['POST'])
def add_task(request):
    data = request.data
    try:
        t = Tasks.objects.create(user = request.user, title = data['title'], description = data['description'])
    except:
        return Response('Invalid request', status = status.HTTP_400_BAD_REQUEST)
    else:
        return Response('task added', status = status.HTTP_200_OK)