from __future__ import unicode_literals
from django.views.generic import TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.http import HttpResponse
from django.http import JsonResponse
from myadmin.models import codeModel
# Create your views here.

def mainpage(request,template_name='mainpage.html'):
    all_objects=codeModel.objects.all()
    codeData={}
    codeData['codeData']=all_objects
    return render(request,template_name,codeData)
