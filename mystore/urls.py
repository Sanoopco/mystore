"""mystore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path

import mobile.views
from api import views
from mobile.views import MobileView
from mobile.views import MaxMobile
from mobile.views import MobileDetailsView
from mobapi import views as apiview

import api.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ap1/v1/tech/mobiles',apiview.MobileModelView.as_view()),
    path('ap1/v1/tech/mobiles/<int:mob_id>',apiview.MobileDetailModelView.as_view()),
    # path('morning',views.GoodMornnigView.as_view()),
    # path('wakeup',views.WakeUpView.as_view()),
    # path('gotowork',views.GoToWorkView.as_view()),
    # path('add',views.AddView.as_view()),
    # path("sub",views.SubtractionView.as_view()),
    # path("mul",views.MultiplicationView.as_view()),
    # path("checkprime",views.PrimeNoCheckView.as_view()),
    # path("factorial",views.FacorialView.as_view()),
    # path("multipleoftwo",views.MultipleOfTWO.as_view()),
    # path("mobiles/",MobileView.as_view()),
    # path("maxmobile",MaxMobile.as_view()),
    # path("mobiles/<int:mob_id>",MobileDetailsView.as_view())
]




