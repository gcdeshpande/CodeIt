"""admin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from myadmin import views
urlpatterns = [
    url(r'^new$',views.create_new,name='create_new'),
    url(r'^$',views.all_list,name='all_list'),
    url(r'^updateExisting(?P<pk>\d+)$',views.updateCode,name='updateCode'),
    url(r'^getCodes$',views.getCodeForUpdate,name='getCodeForUpdate'),
    url(r'^delete(?P<pk>\d+)$',views.deletePb,name='deletePb'),
    url(r'^getOutput$',views.getOutput,name='getOutput'),
]
