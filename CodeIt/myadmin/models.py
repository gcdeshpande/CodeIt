# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse

from django.db import models

# Create your models here.
class codeModel(models.Model):
    Difficulty=(
        ('25','Easy'),
        ('50','Moderate'),
        ('100','Difficult'),
    )
    codeHeader=models.TextField(blank=True,null=True,default="newfasf")
    codeMain=models.TextField(blank=True,null=True,default="#inclide")
    pbName=models.CharField(max_length=255)
    pbStat=models.TextField()
    diff=models.CharField(max_length=4,choices=Difficulty,default='50')
    ips1=models.TextField(blank=True,null=True)
    ips2=models.TextField(blank=True,null=True)
    ips3=models.TextField(blank=True,null=True)
    ips4=models.TextField(blank=True,null=True)
    ops1=models.TextField(blank=False,null=False,default="0")
    ops2=models.TextField(blank=False,null=False,default="0")
    ops3=models.TextField(blank=False,null=False,default="0")
    ops4=models.TextField(blank=False,null=False,default="0")

    def __unicode__(self):
        return self.pbName

    def get_absolute_path(self):
        return reverse('edit',kwargs={'pk':self.pk})
