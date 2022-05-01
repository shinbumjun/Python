from django.urls import path
from mysurvey import views

urlpatterns = [
    path('survey', views.surveyView),
    path('surveyprocess', views.surveyProcess), # views로
    path('surveyshow', views.dataAnalysis),
]
