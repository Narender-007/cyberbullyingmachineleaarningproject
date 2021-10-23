"""newprjct URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.views.generic import TemplateView

from newapp.views import login, registration, logout, postCertificate, deleteCertificate, activateAccount, \
    getStudentCertificates, sendRequest, viewRequests, deleteRequest, getCertificates, addUser, getUsers, \
    postCertificateAction, updateRequestStatus

urlpatterns = [

    path('admin/', admin.site.urls),

    path('login', TemplateView.as_view(template_name = 'index.html'), name='login'),
    path('loginaction/', login, name='loginaction'),

    path('registration/', TemplateView.as_view(template_name='registration.html'), name='registration'),
    path('adduser/', TemplateView.as_view(template_name='addusers.html'), name='postcertificate'),

    path('regaction/', registration,name='regaction'),
    path('adduseraction/', addUser, name='adduser'),

    path('logout/',logout,name='logout'),
    path('activateaction/',activateAccount,name='activateaction'),
    path('viewusers/',getUsers,name='getUsers'),
    path('postcertificate/',postCertificate,name='postcertificate'),
    path('postcertificateaction/',postCertificateAction,name='certificateaction'),
    path('viewcertificates/',getCertificates,name='viewcertificates'),
    path('viewstudentcertificates/',getStudentCertificates,name='viewcertificates'),
    path('deletecertificate/',deleteCertificate,name='deletecertificate'),

    path('sendrequest/',sendRequest, name='requestaction'),
    path('viewrequests/',viewRequests, name='viewrequests'),
    path('deleterequest/', deleteRequest, name='deleterequest'),
    path('updaterequest/',updateRequestStatus, name='requestaction')


]
