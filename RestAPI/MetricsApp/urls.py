from django.urls import re_path
from MetricsApp import views

urlpatterns = [
    re_path(r'^metric$', views.dockermetricsApi),
    re_path(r'^metric/([0-9]+)$', views.dockermetricsApi)
]
