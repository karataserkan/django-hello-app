# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from github import Github
from django.template import loader

# Create your views here.
def UserPage(request):
	template = loader.get_template('user/userpage.html')
	g = Github("username", "password")
	repos = g.get_user().get_repos()
	return HttpResponse(template.render({'repos':repos}, request))
	
def Gist(request):
	template = loader.get_template('user/gists.html')
	g = Github()
	gists = g.get_user('karataserkan').get_gists()

	
	return HttpResponse(template.render({'gists':gists}, request))

