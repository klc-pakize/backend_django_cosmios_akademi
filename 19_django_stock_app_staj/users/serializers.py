from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework.authtoken.models import Token

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required = True,
            validators=[UniqueValidator(queryset=User.objects.all())]
                                   )
    
    password = serializers.CharField(
        write_only = True,
        required = True,
        validators = [validate_password],
        style = {"input_type": "password"}
    )

    password2 = serializers.CharField(
        write_only = True,
        required = True,
        style = {"input_type": "password"}
    )

    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "password",
            "password2",
            "token",
        ) 

    def get_token(self, obj):
        token = Token.objects.get(user = obj)
        return token.key

    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError(
                {"message": "Password fileds didnt match."}
            )
        return data

# data = {
#         "first_name" : "pakize",
#         "last_name": "kılıç",
#         "username": "pakize",
#         "email":"pa3kkizejcnj",
#         "password":"12345",
#         "password2": "12345"
# }

    def create(self, validated_data):
        password= validated_data.get('password')  # "password":"12345",
        validated_data.pop('password2')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user

# validated_data = {
#         "first_name" : "pakize",
#         "last_name": "kılıç",
#         "username": "pakize",
#         "email":"pa3kkizejcnj",
#         "password":"123fjkv rkljtbnln rtlnbrjgbnkjr45",
# }