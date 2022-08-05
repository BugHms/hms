from django.urls import path, include
from django.conf.urls import url
from .views import *

urlpatterns = [
    path('', view),
    path('generate/', generate),
    path('do_generate/', doGenerate),
    url('close/<id>/', close),
    url(r'delete/<id>/', delete),
]