from django.conf.urls import url

from git.views import *

urlpatterns = [
    url(r'git/user', UserPage),
]