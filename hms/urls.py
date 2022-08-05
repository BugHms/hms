"""hms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from loginmodule.views import logout, login

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('loginmodule/', include('loginmodule.urls')),
    # path('login/', login),
    # path('logout/', logout),
    # path('', include('home.urls')),
    # path('home/', include('home.urls')),
    # path('case/', include('case.urls')),
    # path('bill/', include('bill.urls')),
    # path('reports/', include('reports.urls')),
    # path('appointments/', include('appointments.urls')),

    #
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('home/', include('home.urls')),
    path('profile/', include('profiles.urls')),
    path('appointments/', include('appointments.urls')),
    path('case/', include('case.urls')),
    path('reports/', include('reports.urls')),
    path('bill/', include('bill.urls')),
	path('login/', login),
    path('logout/', logout),
    path('loginmodule/', include('loginmodule.urls'))
]
