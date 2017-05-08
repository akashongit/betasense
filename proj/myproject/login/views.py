# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
from rest_framework.authtoken import views
import datetime


# Create your views here.
class user_login(View):
	def get(self,request):
                if request.user.is_authenticated():
                        username = request.user.username
                        user= request.user
                        print(user.username)
                # if user:
                        # Is the account active? It could have been disabled.
                        # if user.is_active:
                                # If the account is valid and active, we can log the user in.
                                # We'll send the user back to the homepage.
                                # login(request, user)
                                # print(request.POST['username'],request.POST['password'],user.username)
                        now = datetime.datetime.now()        
                        # last_seen= lastlogin.objects.get_or_create(user=user,last_visit=now)
                        try:
                                last_seen= lastlogin.objects.get(user=user)
                                last_seen.last_visit=now
                        except DoesNotExist:
                                last_seen= lastlogin.objects.get_or_create(user=user,last_visit=now)
                        last_seen.save()
                        return HttpResponse("Welcome!!!")
                # else:
                                # An inactive account was used - no logging in!
                                # return HttpResponse("Your account is disabled.")
                else:
                        # Bad login details were provided. So we can't log the user in.
                        print("Invalid login details: {0}, {1}".format(username, password))
                        return HttpResponse("Invalid login details supplied.")
