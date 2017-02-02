# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 20:03:08 2017

@author: gaurav
"""

from django.conf.urls import url,patterns

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    urlpatterns = patterns('myapp.views',
    url(r'^list/$', 'list', name='list'),
)

]
