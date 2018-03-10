# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.http import HttpResponse
from django.http import JsonResponse
from models import codeModel
import os,sys
# Create your views here.
class CodeBase(ModelForm):
    class Meta:
        model=codeModel
        fields=['codeHeader','codeMain','pbName','pbStat','diff', 'ips1','ips2','ips3','ips4','ops1','ops2','ops3','ops4']

def all_list(request,template_name='data.html'):
    all_objects=codeModel.objects.all()
    codeData={}
    codeData['codeData']=all_objects
    return render(request,template_name,codeData)

def create_new(request,template_name='index.html'):
    form=CodeBase(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('all_list')
    return render(request,template_name,{'form':form})

def updateCode(request,pk,template_name='newUpdate.html'):
    codeAtPk=get_object_or_404(codeModel,pk=pk)
    updatedCode=CodeBase(request.POST or None,instance=codeAtPk)
    if updatedCode.is_valid():
        updatedCode.save()
        return redirect('all_list')
    return render(request,template_name,{'codeAtPk':updatedCode})

def getCodeForUpdate(request):
    Cpk=request.GET.get('pk')
    getCode=get_object_or_404(codeModel,pk=Cpk)
    return JsonResponse({'codeHeader':getCode.codeHeader,'codeMain':getCode.codeMain})


def deletePb(request,pk,template_name='data.html'):
    codeAtPk=get_object_or_404(codeModel,pk=pk)
    if request.method=='GET':
        codeAtPk.delete()
        return redirect('all_list')
    return render(request,template_name,{'objects':codeAtPk})

def getOutput(request):
    os.system("touch output1.txt output2.txt output3.txt output4.txt input1.txt input2.txt input3.txt input4.txt error.txt")
    codeHeader = request.GET.get("codeHeader")
    codeMain = request.GET.get("codeMain")
    ips1=request.GET.get('ips1')
    ips2=request.GET.get('ips2')
    ips3=request.GET.get('ips3')
    ips4=request.GET.get('ips4')
    wholeCode=codeHeader+codeMain
    fp=open("input1.txt","w")
    fp.write(ips1)
    fp=open("input2.txt","w")
    fp.write(ips2)
    fp=open("input3.txt","w")
    fp.write(ips3)
    fp=open("input4.txt","w")
    fp.write(ips4)
    fp=open("test.c","w")
    fp.write(wholeCode)
    fp.close()
    os.system("gcc test.c 2> error.txt")
    fp=open("error.txt")
    error=fp.read()
    if fp.read()!="":
        return JsonResponse({'error':error,'ops1':"",'ops2':"",'ops3':"",'ops4':""})

    os.system("./a.out < input1.txt > output1.txt")
    fp=open("output1.txt","r")
    ops1=fp.read()
    os.system("./a.out < input2.txt > output2.txt")

    fp=open("output2.txt","r")
    ops2=fp.read()
    os.system("./a.out < input3.txt > output3.txt")

    fp=open("output3.txt","r")
    ops3=fp.read()
    os.system("./a.out < input4.txt > output4.txt")

    fp=open("output4.txt","r")
    ops4=fp.read()
    fp.close()
    return JsonResponse({'error':error,'ops1':ops1,'ops2':ops2,'ops3':ops3,'ops4':ops4})
