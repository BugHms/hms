from django.contrib import admin
from django.urls import path, include
# from django.conf.urls import url
from .views import *

urlpatterns = [
    path('', view),
    path('generate/<case_id>/', generate),
    path('do_generate/', doGenerate),
    path('delete/<id>/', delete),
    path('pay/', pay),
    path('medicines/', viewMedicine)
]