# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import Model
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _
from users.models import Users


# Create your models here.

class Pet(Model):
    name = models.CharField(max_length=10, null=True, blank=True)
    age = models.DurationField(max_length=20, null=True, blank=True)
    user = models.ForeignKey(Users,on_delete=models.CASCADE, verbose_name=_("用户"))
    type = models.CharField(max_length=3,
                            choices=(('cat',_('猫')),('dog',_('狗')))
                            )
    adopted = models.BooleanField(default=False)
    size = models.CharField(max_length=6,
                            choices=(("large",_("大型")),('medium',_('中等体型')),('small',_('小型')))
                            )
    add_time = models.DateField(default=now)

    class Meta:
        verbose_name = _("宠物")
        verbose_name_plural = _("宠物")
        ordering = ('-add_time',)


    def __str__(self):
        return self.name

