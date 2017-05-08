from django.conf.urls import url
from rest_framework.authtoken import views as token
from . import views as login 
urlpatterns = [
	url(r'^profile/',login.user_login.as_view(),name="login"),
]
