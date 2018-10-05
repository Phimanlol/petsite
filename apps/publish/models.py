# -*- coding: utf-8 -*-

from datetime import datetime


from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.utils.timezone import now


from pet.models import Pet
from users.models import Users

# Create your models here.

class Publish(models.Model):
    id = models.UUIDField(primary_key=True,editable=False)
    title = models.CharField(max_length=20, null=True, blank=True)
    desc = models.CharField(_('宠物描述'),max_length=500, null=True, blank=True)
    publish_time = models.DateField(_('发布时间'), default=now)
    pet = models.ManyToManyField(Pet, related_name='Publishs')
    user = models.ForeignKey(Users,verbose_name=_('宠物主人'), on_delete=models.CASCADE)
    province = models.CharField(_('省份'),max_length=10, null=True, blank=True)
    address = models.CharField(_('详细地址'),max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = _("领养信息")
        verbose_name_plural = _("领养信息")
        ordering=('-publish_time',)

    def __str__(self):
        return self.title


class comments(models.Model):
    content = models.CharField(max_length=200, null=True, blank=True)
    add_time = models.DateTimeField(default=now,editable=False)
    user = models.ForeignKey(Users,verbose_name=_('评论所属人'), on_delete=models.CASCADE)
    publish =models.ForeignKey(Publish,on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("评论")
        verbose_name_plural = _("评论")
        ordering = ['-add_time']

    def __str__(self):
        return self.content



