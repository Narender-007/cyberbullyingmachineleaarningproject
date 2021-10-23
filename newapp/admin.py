

from django.contrib import admin

# Register your models here.
from .models import RegistrationModel, CertificateModel, RequestModel

admin.site.register(RegistrationModel)
admin.site.register(CertificateModel)
admin.site.register(RequestModel)
