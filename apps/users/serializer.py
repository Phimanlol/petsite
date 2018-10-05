# -*- coding: utf-8 -*-
from rest_framework.serializers import ModelSerializer

from .models import Users


class UsersSerializer(ModelSerializer):
    class Meta:
        model = Users
        fields = ('last_time', 'gender', 'mobile', 'category')