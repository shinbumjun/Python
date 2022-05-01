"""django2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views (1.요청에 대해서)
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views (2.)
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf (3.)
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from gtapp import views # 1) import가 되어야 한다
from gtapp.views import CallView # 2) import가 되어야 한다
from django.urls.conf import include # 3) [중요]


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.mainFunc), # 1) 요청명이 없을 경우, Function views
    path('abc/callget', CallView.as_view()), # 2) 링크를 눌렀을때, Class-based views
    path('member/', include('gtapp.urls')) # 3) member로 시작하는것 위임, Including another URLconf
] 














