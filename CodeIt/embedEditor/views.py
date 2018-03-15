from __future__ import unicode_literals
from django.views.generic import TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.http import HttpResponse
from django.http import JsonResponse
from myadmin.models import codeModel
import json,os
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

def getmyOutput(request,pk):
    data=codeModel.objects.get(pk=pk)
    os.system("touch output1.txt output2.txt output3.txt output4.txt input1.txt input2.txt input3.txt input4.txt error.txt")
    codeHeader = request.GET.get("codeHeader")
    codeMain = request.GET.get("codeMain")

    wholeCode=codeHeader+codeMain
    fp=open("input1.txt","w")
    fp.write(data.ips1)
    fp=open("input2.txt","w")
    fp.write(data.ips2)
    fp=open("input3.txt","w")
    fp.write(data.ips3)
    fp=open("input4.txt","w")
    fp.write(data.ips4)
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
    if ops1==data.ops1:
        flagResult1="svg/correct.svg"
    else:
        flagResult1="svg/wrong.svg"
    os.system("./a.out < input2.txt > output2.txt")

    fp=open("output2.txt","r")
    ops2=fp.read()
    if ops2==data.ops2:
        flagResult2="svg/correct.svg"
    else:
        flagResult2="svg/wrong.svg"
    os.system("./a.out < input3.txt > output3.txt")

    fp=open("output3.txt","r")
    ops3=fp.read()
    if ops3==data.ops3:
        flagResult3="svg/correct.svg"
    else:
        flagResult3="svg/wrong.svg"
    os.system("./a.out < input4.txt > output4.txt")

    fp=open("output4.txt","r")
    ops4=fp.read()
    if ops4==data.ops4:
        flagResult4="svg/correct.svg"
    else:
        flagResult4="svg/wrong.svg"
    fp.close()
    return JsonResponse({'error':error,'ips1':data.ips1,'ips2':data.ips2,'ips3':data.ips3,'ips4':data.ips4,'actualOutput1':data.ops1,'actualOutput2':data.ops2,'actualOutput3':data.ops3,'actualOutput4':data.ops4,'ops1':ops1,'ops2':ops2,'ops3':ops3,'ops4':ops4,'flagResult1':flagResult1,'flagResult2':flagResult2,'flagResult3':flagResult3,'flagResult4':flagResult4})
