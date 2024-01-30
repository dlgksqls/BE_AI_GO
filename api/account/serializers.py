from rest_framework.serializers import ModelSerializer, CharField
from rest_framework.validators import ValidationError
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed

from .models import User


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

## 회원가입
class SignUpSerializer(ModelSerializer):
    username = CharField(write_only=True, max_length=150)
    password = CharField(write_only=True, max_length=128)  # Django 기본 User 모델의 비밀번호 최대 길이는 128자 입니다.
    password2 = CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ["username", "password", "password_check"]

    def validate(self, attrs):
        if attrs["password"] != attrs["password_check"]:
            raise ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        validated_data.pop("password_check")
        user = User.objects.create_user(**validated_data)
        return user
    
## 로그인
class LogInSerializer(serializers.Serializer):
    username = CharField(write_only=True, max_length=150)
    password = CharField(write_only=True, max_length=128)

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if user is None:
            if user is None:
                raise serializers.ValidationError("Invalid username or password.")
        if not user.is_active:
            raise serializers.ValidationError("User is not active.")
        return {'user': user}