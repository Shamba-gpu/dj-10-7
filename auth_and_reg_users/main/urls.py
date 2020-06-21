"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path

import auth2.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth2.views.home, name='home'),
    path('signup/', auth2.views.SignupView.as_view(), name='signup'),
    path('login/', auth2.views.Login_View.as_view(), name='login'),
    path('logout/', auth2.views.Logout_View.as_view(), name='logout'),
]
