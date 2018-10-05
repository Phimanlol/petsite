# -*- coding: utf-8 -*-

from rest_framework import serializers


from .models import Publish

class PublishSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    publish_time = serializers.CharField(read_only=True)
    class Meta:
        model = Publish
        fields = ('title', 'desc', 'publish_time', 'pet', 'user','id', 'privince_address', 'detail_address')
        read_only_fields = ('publish_time',)