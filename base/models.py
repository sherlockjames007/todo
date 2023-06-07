from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import validate_email

# Create your models here.


# the user model of this project
# inherits properties from the abstract user class
# more specifically the first_name, last_name and password properties have not been mentioned here since they have been inherited
class User(AbstractUser):
    username = models.EmailField(max_length = 500, unique = True, primary_key = True, null = False, validators = [validate_email])
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

# this model contains all the to-do tasks of the users
class Tasks(models.Model):
    user = models.ForeignKey(to = 'User', null = False, on_delete = models.CASCADE)
    title = models.CharField(max_length = 100, null = False)
    description = models.CharField(max_length = 500, null = False)
    checked = models.BooleanField(default = False)