from django.urls import path, include
from django.conf.urls import url
from .views import *

urlpatterns = [
    path('', view),
    path('generate/', generate),
    path('do_generate/', doGenerate),
    path('change/<id>/', change),
    path('do_change/', doChange),
    path('delete/<id>/', delete),
]