from __future__ import unicode_literals
from django.views.generic import TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.http import HttpResponse
from django.http import JsonResponse
from myadmin.models import codeModel
import json
# Create your views here.
class CodeBase(ModelForm):
    class Meta:
        model=codeModel
        fields=['codeHeader','codeMain','pbName','pbStat','diff', 'ips1','ips2','ips3','ips4','ops1','ops2','ops3','ops4']
def init_data(request,pk,template_name='editorpage.html'):
    data=codeModel.objects.get(pk=pk)
    return render(request,template_name,{'data':data})

def getCodeData(request):
    Cpk=request.GET.get('pk')
    getCode=get_object_or_404(codeModel,pk=Cpk)
    return JsonResponse({'codeHeader':getCode.codeHeader,'codeMain':getCode.codeMain})
