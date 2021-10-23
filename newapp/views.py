from django.shortcuts import render
from django.shortcuts import render
from django.db.models import Max

from newapp.models import RegistrationModel, CertificateModel, RequestModel
from newapp.forms import RegistrationForm, CertificateForm, LoginForm

def registration(request):
    status = False

    if request.method == "POST":
        # Get the posted form
        registrationForm = RegistrationForm(request.POST)

        if registrationForm.is_valid():

            regModel = RegistrationModel()
            regModel.name = registrationForm.cleaned_data["name"]
            regModel.email = registrationForm.cleaned_data["email"]
            regModel.mobile = registrationForm.cleaned_data["mobile"]
            regModel.address = registrationForm.cleaned_data["address"]
            regModel.utype = registrationForm.cleaned_data["utype"]
            regModel.username = registrationForm.cleaned_data["username"]
            regModel.password = registrationForm.cleaned_data["password"]

            regModel.status = "yes"

            user = RegistrationModel.objects.filter(username=regModel.username).first()

            if user is not None:
                status = False
            else:
                try:
                    regModel.save()
                    status = True
                except:
                    status = False
    if status:
        return render(request, 'index.html', locals())
    else:
        response = render(request, 'registration.html', {"message": "User All Ready Exist"})

    return response

def addUser(request):
    status = False

    if request.method == "POST":
        # Get the posted form
        registrationForm = RegistrationForm(request.POST)

        if registrationForm.is_valid():

            regModel = RegistrationModel()
            regModel.name = registrationForm.cleaned_data["name"]
            regModel.email = registrationForm.cleaned_data["email"]
            regModel.mobile = registrationForm.cleaned_data["mobile"]
            regModel.address = registrationForm.cleaned_data["address"]
            regModel.utype = registrationForm.cleaned_data["utype"]
            regModel.username = registrationForm.cleaned_data["username"]
            regModel.password = registrationForm.cleaned_data["password"]

            regModel.status = "yes"

            user = RegistrationModel.objects.filter(username=regModel.username).first()

            if user is not None:
                status = False
            else:
                try:
                    regModel.save()
                    status = True
                except:
                    status = False
    if status:
        return render(request, 'addusers.html', {"message": "Success"})
    else:
        response = render(request, 'addusers.html', {"message": "User All Ready Exist"})

    return response

def login(request):
    uname = ""
    upass = ""
    if request.method == "GET":
        # Get the posted form
        loginForm = LoginForm(request.GET)

        if loginForm.is_valid():

            uname = loginForm.cleaned_data["username"]
            upass = loginForm.cleaned_data["password"]

            if uname == "admin" and upass == "admin":
                request.session['username'] = "admin"
                request.session['role'] = "admin"

                return render(request, 'adminhome.html', {})

        user = RegistrationModel.objects.filter(username=uname, password=upass, status="yes").first()

        if user is not None:
            request.session['username'] = uname
            request.session['role'] = user.utype

            if user.utype=="student":
                response = render(request, 'studenthome.html', {"username": uname})
            elif user.utype=="verifier":
                response = render(request, 'verifierhome.html', {"username": uname})
            elif user.utype=="university":
                response = render(request, 'universityhome.html', {"username": uname})

        else:
            response = render(request, 'index.html', {"message": "Invalid Credentials"})

    return response

def logout(request):
    try:
        del request.session['username']
    except:
        pass
    return render(request, 'index.html', {})

def activateAccount(request):

    status = False

    username = request.GET['username']
    status=request.GET['status']

    RegistrationModel.objects.filter(username=username).update(status=status)
    return render(request, 'adminhome.html', {"users": RegistrationModel.objects.all()})

def getUsers(request):

    if request.session["role"]=="admin":
        return render(request, "adminhome.html", {"users": RegistrationModel.objects.all()})
    else:
        users = RegistrationModel.objects.all()
        reqs = RequestModel.objects.all()
        results = []

        for user in users:

            status1 = "no"
            status2 = "no"

            for req in reqs:
                if user.username==req.studentid:
                    status1 = "yes"
                if user.username==req.studentid and req.userstatus in "yes":
                    status2 = "yes"

            user.rstatus = status1
            user.ustatus = status2

            results.append(user)

        return render(request, "verifierhome.html",{"users":results})

def postCertificate(request):
    return render(request, "postcertificate.html", {"users":RegistrationModel.objects.all()})

def postCertificateAction(request):

    status = False

    certificateForm = CertificateForm(request.POST, request.FILES)

    if certificateForm.is_valid():
        certificateModel = CertificateModel()

        certificateModel.certificate = certificateForm.cleaned_data["certificate"]
        certificateModel.filetype = certificateForm.cleaned_data["filetype"]
        certificateModel.studentid = certificateForm.cleaned_data["studentid"]
        certificateModel.universityid = request.session['username']

        try:
            certificateModel.save()
            status = True
        except:
            status = False

    if status:
        response = render(request, 'postcertificate.html', {"message": "Certificate Posted Successfully"})
    else:
        response = render(request, 'postcertificate.html', {"message": "Certificate Upload Failed"})

    return response

def getCertificates(request):

    if request.session["role"]=="student":

        certificates = []

        for file in CertificateModel.objects.filter(studentid=request.session['username']):
            file.certificate = str(file.certificate).split("/")[1]

            certificates.append(file)

        return render(request, "viewcertificates.html", {"certificates": certificates})
    else:
        certificates = []

        for file in CertificateModel.objects.filter(universityid=request.session['username']):
            file.certificate = str(file.certificate).split("/")[1]
        certificates.append(file)
        return render(request, "viewcertificates.html", {"certificates": certificates})

def getStudentCertificates(request):
    studentid=request.GET['studentid']

    certificates = []

    for file in CertificateModel.objects.filter(studentid=studentid):
        file.certificate = str(file.certificate).split("/")[1]
    certificates.append(file)

    return render(request, "viewcertificatesbyverifier.html", {"certificates": certificates})

def deleteCertificate(request):
    CertificateModel.objects.filter(id=request.GET['certificateid']).delete()
    return render(request, "viewcertificates.html",
                      {"certificates": CertificateModel.objects.filter(universityid=request.session['username'])})

def sendRequest(request):

    status = False

    if request.method == "GET":

        requestModel = RequestModel()

        requestModel.studentid = request.GET['studentid']
        requestModel.verifierid = request.session["username"]
        requestModel.userstatus = "no"
        requestModel.requeststatus = "sent"

        try:
            requestModel.save()
            status = True
        except:
            status = False

    if status:

        users = RegistrationModel.objects.all()
        reqs = RequestModel.objects.all()
        results = []

        for user in users:

            status1 = "no"
            status2 = "no"

            for req in reqs:
                if user.username == req.studentid:
                    status1 = "yes"
                if user.username == req.studentid and req.userstatus in "yes":
                    status2 = "yes"

            user.rstatus = status1
            user.ustatus = status2

            results.append(user)

        return render(request, "verifierhome.html", {"users": results})

def viewRequests(request):

    if request.session["role"]=="student":
        return render(request, "viewrequests.html", {"requests": RequestModel.objects.filter(studentid=request.session['username'])})
    else:
        return render(request, "verifierhome.html", {"requests": RequestModel.objects.filter(verifierid=request.session['username'])})

def updateRequestStatus(request):

    status = False
    requestid = request.GET['requestid']
    status=request.GET['status']
    RequestModel.objects.filter(id=requestid).update(userstatus=status)
    return render(request, "viewrequests.html", {"requests": RequestModel.objects.filter(studentid=request.session['username'])})

def deleteRequest(request):

    RequestModel.objects.filter(id=request.GET['requestid']).delete()

    if request.session["role"]=="student":
        return render(request, "viewrequests.html", {"requests": RequestModel.objects.filter(studentid=request.session['username'])})
    else:
        return render(request, "verifierhome.html", {"requests": RequestModel.objects.filter(verifierid=request.session['username'])})


# Create your views here.
