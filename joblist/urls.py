from django.urls import path
from . import views


urlpatterns = [
    path('', views.joblist, name='joblist'),
]

