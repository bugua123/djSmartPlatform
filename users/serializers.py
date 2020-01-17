from rest_framework import serializers
from django.contrib.auth.models import User

from users.models import UserInfo, UserToken


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ('user_type','username', 'password')

class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserToken
        fields = ('user', 'token')