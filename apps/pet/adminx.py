# -*- coding: utf-8 -*-

import xadmin
from .models import Pet

class petAdmin(object):
    list_display = ['name', 'age', 'user', 'type', 'adopted', 'size', 'add_time']
    search_fields = ['name', ]
    list_editable = ["adopted", ]
    list_filter = ['name', 'age', 'user', 'type', 'adopted', 'size', 'add_time']

    class petInline(object):
        model = Pet
        style = 'tab'

    inlines = [petInline]