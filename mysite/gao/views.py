# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
	return HttpResponse('<font color="red">my first word</font>')
	
def test(request):
	return HttpResponse(u'test测试文本地方撒尽快了解了')