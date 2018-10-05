# -*- coding: utf-8 -*-
"""petSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# import admin

from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url, include

from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token

from publish.views import PublishViewSet
from pet.views import PetsViewSet
from apps import xadmin

router = routers.SimpleRouter()

router.register(r'publish', PublishViewSet, base_name='publish')
router.register(r'pets', PetsViewSet, base_name='pets')


urlpatterns = [
    url(r'xadmin/', xadmin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^', include(router.urls)),
    url(r'^api-token-auth/', obtain_jwt_token),
]
