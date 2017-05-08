# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.db import models

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

# Create your models here.

class lastlogin(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	last_visit = models.DateTimeField()

	def __str__(self):
		return self.user.username
	def __unicode__(self):
		return self.user.username
		
