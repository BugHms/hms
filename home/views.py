from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# import requests


# Create your views here.
@login_required()
def home(request):
    # response = requests.get("https://www.greetingsapi.com/random")
    # json_data = response.json()
    # # print(json_data)
    messages.add_message(request, messages.INFO, 'Welcome to The Hospital Portal.')
    return render(request, 'home/base.html', {'greetings': json_data})