from django.db import models

# Create your models here.
from django.db.models import Model, ImageField


class RegistrationModel(Model):

    username=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    mobile=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    utype=models.CharField(max_length=50)
    status=models.CharField(max_length=50)

    class Meta:
        db_table = "registration"

class CertificateModel(Model):

    certificate =ImageField(upload_to="certificates")
    filetype = models.CharField(max_length=50)
    studentid = models.CharField(max_length=50)
    universityid = models.CharField(max_length=50)

    class Meta:
        db_table="certificates"

class RequestModel(Model):

    studentid = models.CharField(max_length=50)
    verifierid = models.CharField(max_length=50)
    userstatus = models.CharField(max_length=50)
    requeststatus = models.CharField(max_length=50)

    class Meta:
        db_table="requests"