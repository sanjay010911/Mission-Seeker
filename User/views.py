from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from User.models import *
from cryptography.fernet import Fernet
import datetime
# Create your views here.
def home(request):
    if 'ugid' in request.session:
        user=User.objects.get(id=request.session["ugid"]) 
        return render(request,"User/Homepage.html",{'data':user})
    else:
        return redirect("webguest:login")

def MyProfile(request):
    if 'ugid' in request.session:
        user=User.objects.get(id=request.session["ugid"])
        return render(request,"User/MyProfile.html",{'data':user})
    else:
        return redirect("webguest:login")

def EditProfile(request):
    if 'ugid' in request.session:
        user=User.objects.get(id=request.session["ugid"])
        if request.method=="POST":
            user.user_name=request.POST.get('txt_name')
            user.user_contact=request.POST.get('txt_contact')
            user.user_mail=request.POST.get('txt_mail')
            user.user_address=request.POST.get('txt_address')
            user.save()
            return render(request,"User/EditProfile.html",{'data':user,'msg':"Profile Updated"})
            #return redirect("webuser:myprofile")
        else:
            return render(request,"User/EditProfile.html",{'data':user})
    else:
        return redirect("webguest:login")

def ChangePass(request):
    if 'ugid' in request.session:
        if request.method=="POST":
            usercount=User.objects.filter(id=request.session["ugid"],user_pass=request.POST.get('txt_curr')).count()
            if usercount>0:
                if request.POST.get("txt_new")==request.POST.get("txt_confirm"):
                    user=User.objects.get(id=request.session["ugid"],user_pass=request.POST.get('txt_curr'))
                    user.user_pass=request.POST.get('txt_new')
                    user.save()
                    return render(request,"User/ChangePassword.html",{'msg':"Password Updated"})
                    return redirect("webuser:Home")
                else:
                    return render(request,"User/ChangePassword.html",{'msg':"New Password and Confirm Password Not Same"})
            else:
                return render(request,"User/ChangePassword.html",{'msg':"Current Password Incorrect"})
        else:
            return render(request,"User/ChangePassword.html")
    else:
        return redirect("webguest:login")

def Reques(request,did):
    if 'ugid' in request.session:
        disd=Agency.objects.get(id=did)
        disid=disd.casetype.id
        dis=Casetype.objects.get(id=disid)
        if request.method=="POST":
            Req.objects.create(request_details=request.POST.get("txt_details"),casetype=dis,request_date=datetime.datetime.now(),user_id=request.session["ugid"],agency_id=did)
            return redirect("webuser:viewreq")
        else:
            return render(request,"User/Request.html")
    else:
        return redirect("webguest:login")
    
def ViewReq(request):
    if 'ugid' in request.session:
        dis=Req.objects.filter(user_id=request.session["ugid"])
        return render(request,"User/ViewRequest.html",{'data':dis})
    else:
        return redirect("webguest:login")

def feedback(request):
    if 'ugid' in request.session:
        if request.method=="POST":
            Feedback.objects.create(feedback_details=request.POST.get("txt_address"),user_id=request.session["ugid"])
            return render(request,"User/Feedback.html",{'msg':"Feedback Submitted"})
        else:
            return render(request,"User/Feedback.html")
    else:
        return redirect("webguest:login")

def complaint(request):
    if 'ugid' in request.session:
        cmp=Complaint.objects.filter(user_id=request.session["ugid"])
        if request.method=="POST":
            Complaint.objects.create(complaint_title=request.POST.get("txt_title"),complaint_details=request.POST.get("txt_details"),user_id=request.session["ugid"])
            return render(request,"User/Complaint.html",{'cmp':cmp,'msg':"Complaint Submitted"})
        else:
            return render(request,"User/Complaint.html",{'cmp':cmp,})
    else:
        return redirect("webguest:login")

def SearchAgency(request):
    if 'ugid' in request.session:
        cs=Casetype.objects.all()
        dis=District.objects.all()
        ag=Agency.objects.filter(agency_vstatus=1)
        return render(request,"User/SearchAgency.html",{'dis':dis,'cs':cs,'ag':ag})
    else:
        return redirect("webguest:login")

def AjaxAgency(request):
    if request.GET.get('cid')!="":
        case=Casetype.objects.get(id=request.GET.get('cid'))
        if request.GET.get('pid')!="":
            ag=Agency.objects.filter(place=(Place.objects.get(id=request.GET.get('pid'))),casetype=case,agency_vstatus=1)
            return render(request,"User/AjaxAgency.html",{'agency':ag})
        elif request.GET.get('disd')!="":
            ag=Agency.objects.filter(place__district=(District.objects.get(id=request.GET.get('disd'))),casetype=case,agency_vstatus=1)
            return render(request,"User/AjaxAgency.html",{'agency':ag})
        else:
            ag=Agency.objects.filter(casetype=case,agency_vstatus=1)
            return render(request,"User/AjaxAgency.html",{'agency':ag})
    else:
        if request.GET.get('pid')!="":
            ag=Agency.objects.filter(place=(Place.objects.get(id=request.GET.get('pid'))),agency_vstatus=1)
            return render(request,"User/AjaxAgency.html",{'agency':ag})
        else:
            ag=Agency.objects.filter(place__district=(District.objects.get(id=request.GET.get('disd'))),agency_vstatus=1)
            return render(request,"User/AjaxAgency.html",{'agency':ag})
        
def keyverification(request,cid):
    if 'ugid' in request.session:
        request.session['did']=cid
        userid=User.objects.get(id=request.session['ugid'])
        K=userid.key
        #print(K)   
        if request.method=="POST":
            Key=request.POST.get('en_key')
            Key = Key.encode()
            #print(Key)
            if Key==K:
                print("Hai")
                return redirect('webuser:Chat-user')
            else:
                error="Key Incorrect!!"
                return render(request,"User/KeyVerification.html",{'msg':error})
        else:
            return render(request,"User/KeyVerification.html",)
    else:
        return redirect("webguest:login")
        
    
def chatuser(request):
    chatobj = Req.objects.get(id=request.session["did"])
    if request.method == "POST": 
        cied = request.POST.get("cid")
        # print(cied)
        ciedobj = Agency.objects.get(id=cied)
        key=ciedobj.key
        a=Fernet(key)
        '''key=bytes(key,'utf-8')
        print(key)
        with open("pass.key", "wb") as key_file:
            key_file.write(key)
        key=call_key()
        
        key=key.decode('utf-8')
        key=base64.urlsafe_b64encode(bytes(key,'utf-8'))
        print(key)
        a=Fernet(key)'''
        sobj = User.objects.get(id=request.session["ugid"])
        content = request.POST.get("msg")
        slog=content.encode()
        coded_slog=a.encrypt(slog)
        print("Encrypted")
        print(coded_slog)
        decoded_slog=a.decrypt(coded_slog)
        print("Decrypted")
        cont=decoded_slog.decode()
        print(cont)
        # print(cied)
        # print(content)
        Chat.objects.create(from_user=sobj, to_agency=ciedobj, content=coded_slog, from_agency=None, to_user=None)
        return render(request, 'User/Chat.html', {"chatobj": chatobj})
    else:
        return render(request, 'User/Chat.html', {"chatobj": chatobj})


def loadchatuser(request):
    cid = request.GET.get("cid")
    request.session["cid"] = cid
    cid1 = request.session["cid"]
    # print(cid1)
    # print(cid)
    shopobj=Agency.objects.get(id=cid)
    key=shopobj.key
    a=Fernet(key)
    # print(userobj)
    sid = request.session["ugid"]
    # print(sid)
    suserobj = User.objects.get(id=request.session["ugid"])
    key1=suserobj.key
    b=Fernet(key1)
    # chatobj1 = Chat.objects.filter(Q(to_user=suserobj) | Q(
    #     from_user=suserobj), Q(to_shop=shopobj) | Q(from_shop=shopobj))
    # print(chatobj1)  # send message
    # print(chatobj2)  # recived msg
    chatobj = Chat.objects.raw("select * from User_chat c inner join Guest_User u on (u.id=c.from_user_id) or (u.id=c.to_user_id) WHERE  c.from_agency_id=%s or c.to_agency_id=%s order by c.date", params=[(cid1), (cid1)])
    

    leh=(len(chatobj))
    #message=[0 for i in range(0,leh)]
    for i in range(0,leh):
        csid=int(cid)
        if chatobj[i].from_user_id==sid and chatobj[i].to_agency_id==csid:
            chatobj[i].content=a.decrypt(chatobj[i].content).decode()
        elif chatobj[i].to_user_id==sid and chatobj[i].from_agency_id==csid:
            chatobj[i].content=b.decrypt(chatobj[i].content).decode()
    #print(message)
    return render(request, 'User/Load.html', {"obj":chatobj, "sid": sid, "shop": shopobj, "userobj": suserobj})

     

def call_key():
    return open("pass.key", "rb").read()

def Logout(request):
    del request.session["ugid"]
    return redirect("webguest:login")

def ConfirmPayment(request,did):
    if 'ugid' in request.session:
        req=Req.objects.get(id=did)
        return render(request,'User/ConfirmPayment.html',{"data":req})
    else:
        return redirect("webguest:login")
    

def Payment(request,did):
    if request.method=="POST":
        r=Req.objects.get(id=did)
        r.payment_status='2'
        r.save()
        return redirect("webuser:viewreq")
        
    return render(request,'User/Payment.html')
    





        




