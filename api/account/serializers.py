from rest_framework.serializers import ModelSerializer, CharField
from rest_framework.validators import ValidationError
from django.contrib.auth.password_validation import validate_password

from .models import User


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class SignUpSerializer(ModelSerializer):
    username = CharField(write_only=True, max_length=150)
    # password = CharField(write_only=True, max_length=150)
    # password2 = CharField(write_only=True, max_length=150)
    password2 = CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ["username", "password", "password2"]

        def validate(self, attrs):
            if attrs["password"] != attrs["password2"]:
                raise ValidationError({"password": "Password fields didn't match."})
            return attrs

        def create(self, validated_data):
            validated_data.pop("password2")
            user = User.objects.create_user(**validated_data)
            return user
