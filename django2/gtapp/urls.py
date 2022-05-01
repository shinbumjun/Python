# main urls.py로 부터 위임받은 urls
from django.urls import path
from gtapp import views

# 위임받음
urlpatterns = [
    path('insert', views.insertFunc), # get방식을 지웠기 때문에 insert 전부다 처리
    # path('insertok', views.insertokFunc), # get방식
]











