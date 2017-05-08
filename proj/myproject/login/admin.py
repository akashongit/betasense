# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.models import Group
from .models import lastlogin

admin.site.unregister(Group)
# Register your models here.
class last_login(admin.ModelAdmin):
	list_display = ['__unicode__','last_visit',]
	class Meta:
		model = lastlogin

admin.site.register(lastlogin,last_login)		