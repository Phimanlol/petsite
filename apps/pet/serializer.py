# -*- coding: utf-8 -*-
import rest_framework.serializers as serializer

from .models import Pet

class PetsSerializer(serializer.ModelSerializer):
    class Meta:
        model = Pet
        fields = ('id', 'age', 'owner', 'type', 'adopted', 'size')




