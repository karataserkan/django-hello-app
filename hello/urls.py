from django.conf.urls import url

from hello.views import *

urlpatterns = [
    url(r'hello/$', HomePageView),
    url(r'hello/test', TestPage),
]