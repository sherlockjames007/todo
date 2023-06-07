# this file is for creating the required serializers corresponding the models for the app
from rest_framework.serializers import ModelSerializer
from base.models import Tasks

# serializes the tasks model
class TasksSerializer(ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'