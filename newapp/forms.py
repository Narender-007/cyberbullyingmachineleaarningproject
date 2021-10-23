from django.forms import Form, CharField, IntegerField, ImageField, PasswordInput


class RegistrationForm(Form):

    username =CharField(max_length=50)
    name = CharField(max_length=50)
    password =CharField(max_length=50)
    email =CharField(max_length=50)
    mobile =CharField(max_length=50)
    address =CharField(max_length=50)
    utype =CharField(max_length=50)

class LoginForm(Form):
    username = CharField(max_length=100)
    password = CharField(widget=PasswordInput())

class CertificateForm(Form):

    certificate =ImageField()
    filetype =CharField(max_length=50)
    studentid =CharField(max_length=50)