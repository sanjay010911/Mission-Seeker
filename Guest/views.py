from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from django.core.mail import send_mail
from django.conf import settings
import random

from cryptography.fernet import Fernet

# Create your views here.

def Home(request):
    return render(request,"Guest/home.html")

def Ajaxplace(request):
    dis=District.objects.get(id=request.GET.get('disd'))
    pl=Place.objects.filter(district=dis)
    return render(request,"Guest/AjaxPlace.html",{'pl':pl})

def UserReg(request):
    dis=District.objects.all()
    #dist=User.objects.all()
    if request.method=="POST":
        d=User.objects.filter(user_mail=request.POST.get("txt3"))
        if d:
            return render(request,"Guest/UserRegistration.html",{'res':dis,'msg':"User already exists"})
        else: 
            genwrite_key()
            key = call_key()
            str1=key.decode()
            User.objects.create(user_name=request.POST.get("txt1"),user_contact=request.POST.get("txt2"),user_mail=request.POST.get("txt3"),place_id=request.POST.get("txt_place"),user_photo=request.FILES.get("file1"),user_pass=request.POST.get("txt4"),user_address=request.POST.get("txt5"),key=key)
            send_mail(
                'Welcome To Mission Seeker '+request.POST.get("txt1"), #subject
                "\r Respected Sir/Madam Your Encryption Key is "+str1,#body
                settings.EMAIL_HOST_USER,
                [request.POST.get("txt3")],

            )
            return render(request,"Guest/UserRegistration.html",{'res':dis,'msg':"Successfully Registered"})
    else:
        return render(request,"Guest/UserRegistration.html",{'res':dis})
    
def AgencyReg(request):
    dis=District.objects.all()
    cs=Casetype.objects.all()
    if request.method=="POST":
        d=Agency.objects.filter(agency_mail=request.POST.get("txt_mail"))
        if d:
            return render(request,"Guest/AgencyReg.html",{'res':dis,'cs':cs,'msg':"Agency already exists"})
        else:
            genwrite_key()
            key = call_key()
            str1=key.decode()
            Agency.objects.create(agency_name=request.POST.get("txt_name"),agency_contact=request.POST.get("txt_contact"),agency_mail=request.POST.get("txt_mail"),place_id=request.POST.get("txt_place"),agency_proof=request.FILES.get("file1"),agency_photo=request.FILES.get("file2"),agency_pass=request.POST.get("txt_pass"),agency_address=request.POST.get("txt_address"),casetype_id=request.POST.get("sel_casetype"),key=key)
            send_mail(
                'Welcome To Mission Seeker '+request.POST.get("txt_name"), #subject
                "\r Respected Sir/Madam Your Encryption Key is "+str1,#body
                settings.EMAIL_HOST_USER,
                [request.POST.get("txt_mail")],
            )
            return render(request,"Guest/AgencyReg.html",{'res':dis,'cs':cs,'msg':"Successfully Registered"})
    else:
        return render(request,"Guest/AgencyReg.html",{'res':dis,'cs':cs})

def Login(request):
    if request.method=="POST":
        agencycount=Agency.objects.filter(agency_mail=request.POST.get('txt_mail'),agency_pass=request.POST.get('txt_pass'),agency_vstatus=1).count()
        usercount=User.objects.filter(user_mail=request.POST.get('txt_mail'),user_pass=request.POST.get('txt_pass')).count()
        admincount=admin.objects.filter(admin_mail=request.POST.get('txt_mail'),admin_pass=request.POST.get('txt_pass')).count()
        if agencycount > 0:
            agency=Agency.objects.get(agency_mail=request.POST.get('txt_mail'),agency_pass=request.POST.get('txt_pass'),agency_vstatus=1)
            request.session['agid']=agency.id
            request.session['agname']=agency.agency_name
            return redirect('webagency:Home')
        elif usercount > 0:
            user=User.objects.get(user_mail=request.POST.get('txt_mail'),user_pass=request.POST.get('txt_pass'))
            request.session['ugid']=user.id
            request.session['uname']=user.user_name
            return redirect('webuser:Home')
        elif admincount > 0:
            ad=admin.objects.get(admin_mail=request.POST.get('txt_mail'),admin_pass=request.POST.get('txt_pass'))
            request.session['adid']=ad.id
            request.session['admail']=ad.admin_mail
            return redirect('webadmin:Home')
        else:
            return render(request,"Guest/Login.html",{'msg':"Invalid E-Mail Or Password"})
    return render(request,"Guest/Login.html")

def GoBack(request):
    return redirect("webguest:home")

def ForgotPass(request):
    if request.method=="POST":
        u=User.objects.filter(user_mail=request.POST.get('txt_email')).count()
        a=Agency.objects.filter(agency_mail=request.POST.get('txt_email')).count()
        if u>0 or a>0:
            otp=(random.randint(100000,999999))
            request.session["otp"]=otp
            request.session["femail"]=request.POST.get('txt_email')
            send_mail(
                'Respected Sir/Madam '+" ",#subject
                "Your Otp is"+str(otp),#body
                settings.EMAIL_HOST_USER,
                [request.POST.get('txt_email')],
            )
            return redirect('webguest:validateotp')
        else:
            return render(request,"Guest/ForgotPassword.html",{'msg':"Mail Not Exit!!"})
    else:
        return render(request,"Guest/ForgotPassword.html")

def ValidateOtp(request):
    if request.method=="POST":
        otp=request.POST.get("txt_otp")
        ce=str(request.session["otp"])
        if otp==ce:
            return redirect("webguest:createpass")
        else:
            return render(request,"Guest/ValidateOTP.html",{'msg':"Enter Valid OTP"})
    return render(request,"Guest/ValidateOTP.html")

def CreatePass(request):
    if request.method=="POST":
        if request.POST.get("txt_pass")==request.POST.get("txt_confirm"):
            usercount=User.objects.filter(user_mail=request.session["femail"]).count()
            agencycount=Agency.objects.filter(agency_mail=request.session["femail"]).count()
            if usercount>0:
                user=User.objects.get(user_mail=request.session["femail"])
                user.user_pass=request.POST.get("txt_pass")
                user.save()
                return redirect("webguest:login")
            elif agencycount>0:
                agency=Agency.objects.get(agency_mail=request.session["femail"])
                agency.agency_pass=request.POST.get("txt_pass")
                agency.save()
                return redirect("webguest:login")
        else:
            return render(request,"Guest/CreatePassword.html",{'msg':"Passwords not same"})
    else:
        return render(request,"Guest/CreatePassword.html")




def genwrite_key():
    key = Fernet.generate_key()
    with open("pass.key", "wb") as key_file:
        key_file.write(key)

def call_key():
    return open("pass.key", "rb").read()