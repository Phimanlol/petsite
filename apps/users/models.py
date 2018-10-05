# -*- coding: utf-8 -*-


from django.db import models

# Create your models here.

from django.db import models

# Create your models here.
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now


class Users(AbstractUser):
    Gender_Choices = (
        ('male',_('先生')),
        ('female',_('女士'))
    )

    User_Choices = (
        ('adopting',_('宠物领养')),
        ('having',_('宠物送养'))
    )

    name = models.CharField(max_length=30, null=True, blank=True, verbose_name="姓名")
    date_joined = models.DateTimeField(_('注册时间'), default=now)
    gender = models.CharField(choices=Gender_Choices,max_length=2)
    mobile = models.CharField(max_length=11,null=True, blank=True)
    category = models.CharField(choices=User_Choices,max_length=10)
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name=_("邮箱"))
    is_active = models.BooleanField(_('激活'),default=False)

    class Meta:
        verbose_name = _('用户')
        verbose_name_plural = _('用户')

    def __str__(self):
        return self.username

