from rest_framework import serializers

from .models import Todo


class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = (
            'id',
            'task',
            'priority',
            'descrpition',
            "is_done",
            'created_date',
            'updated_date',
        )