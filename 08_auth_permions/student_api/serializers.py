from rest_framework import serializers
from .models import Student, Path
import datetime


# class StudentSerializer(serializers.Serializer):
#     first_name = serializers.CharField(max_length = 30)
#     last_name = serializers.CharField(max_length=40)
#     number = serializers.IntegerField()
#     age = serializers.IntegerField()

#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.first_name = validated_data.get('first_name', instance.first_name)
#         instance.last_name = validated_data.get('last_name', instance.last_name)
#         instance.number = validated_data.get('number', instance.number)
#         instance.age = validated_data.get('age', instance.age)
#         instance.save()
#         return instance

class StudentSerializer(serializers.ModelSerializer):


    path = serializers.StringRelatedField()  # read_only
    path_id = serializers.IntegerField()

    class Meta:
        model = Student
        fields = ["id","first_name", "last_name","number", "path", "path_id"]
    

    

class PathSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Path
        fields = ('id','path_name')