# -*- coding: utf-8 -*-
from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if not request.method in permissions.SAFE_METHODS:
            return request.user == obj.user