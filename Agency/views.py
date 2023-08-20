from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import Agency,User
from User.models import *
from django.conf import settings
from django.core.mail import send_mail
from cryptography.fernet import Fernet
# Create your views here.
def Home(request):
    if 'agid' in request.session:
        ag=Agency.objects.get(id=request.session["agid"]) 
        return render(request,"Agency/Homepage.html",{'data':ag})
    else:
        return redirect("webguest:login")

def MyProfile(request):
    if 'agid' in request.session:
        agency=Agency.objects.get(id=request.session["agid"])
        return render(request,"Agency/MyProfile.html",{'data':agency})
    else:
        return redirect("webguest:login")

def EditProfile(request):
    if 'agid' in request.session:
        agency=Agency.objects.get(id=request.session["agid"])
        if request.method=="POST":
            agency.agency_name=request.POST.get('txt_name')
            agency.agency_contact=request.POST.get('txt_contact')
            agency.agency_mail=request.POST.get('txt_mail')
            agency.agency_address=request.POST.get('txt_address')
            agency.save()
            return redirect("webagency:myprofile")
        else:
            return render(request,"Agency/EditProfile.html",{'data':agency})
    else:
        return redirect("webguest:login")

def ChangePass(request):
    if 'agid' in request.session:
        if request.method=="POST":
            agencycount=Agency.objects.filter(id=request.session["agid"],agency_pass=request.POST.get('txt_curr')).count()
            if agencycount>0:
                if request.POST.get("txt_new")==request.POST.get("txt_confirm"):
                    agency=Agency.objects.get(id=request.session["agid"],agency_pass=request.POST.get('txt_curr'))
                    agency.agency_pass=request.POST.get('txt_new')
                    agency.save()
                    return render(request,"Agency/ChangePassword.html",{'msg':"Password Updated"})
                    return redirect("webagency:Home")
                else:
                    return render(request,"Agency/ChangePassword.html",{'msg':"New Password and Confirm Password Not Same"})
            else:
                return render(request,"Agency/ChangePassword.html",{'msg':"Current Password Incorrect"})
        else:
            return render(request,"Agency/ChangePassword.html")
    else:
        return redirect("webguest:login")

def RequestList(request):
    if 'agid' in request.session:
        newrequest=Req.objects.filter(request_status=0,agency_id=request.session["agid"])
        return render(request,"Agency/RequestList.html",{'data':newrequest})
    else:
        return redirect("webguest:login")

def AcceptedRequestList(request):
    if 'agid' in request.session:
        newrequest=Req.objects.filter(request_status=1)
        return render(request,"Agency/AcceptedRequestsList.html",{'data':newrequest})
    else:
        return redirect("webguest:login")

def RejectedRequestList(request):
    if 'agid' in request.session:
        newrequest=Req.objects.filter(request_status=2)
        return render(request,"Agency/RejectedRequestsList.html",{'data':newrequest})
    else:
        return redirect("webguest:login")

def AcceptRequest(request,did):
    ag=Req.objects.get(id=did)
    agname=ag.agency.agency_name
    uname=ag.user.user_name
    umail=ag.user.user_mail
    ag.request_status=1
    ag.save()
    send_mail(
            'Respected '+uname,#subject
             agname+' has accepted your case, you can now chat with them',#body
            settings.EMAIL_HOST_USER,
            [umail],    
    )
    return redirect("webagency:requestlist")

def RejectRequest(request,did):
    ag=Req.objects.get(id=did)
    ag.request_status=2
    ag.save()
    return redirect("webagency:requestlist")

def a_keyverification(request,cid):
    request.session['aid']=cid
    agnid=Agency.objects.get(id=request.session['agid'])
    K=agnid.keys
    print(K)   
    if request.method=="POST":
        Key=request.POST.get('en_key')
        Key = Key.encode()
        if Key==K:
            return redirect('agency:Chat-agency')
        else:
            error="Key Incorrect!!"
            return render(request,"Agency/KeyVerification.html",{'msg':error})
    else:
        return render(request,"Agency/KeyVerification.html")






def chat(request):
    # chatobj = Crime.objects.get(id=request.session["aid"])
    if request.method == "POST":
        cied = request.POST.get("cid")
        # print(cied)
        ciedobj = User.objects.get(id=cied)
        key=ciedobj.key
        a=Fernet(key)
        sobj = Agency.objects.get(id=request.session["agid"])
        content = request.POST.get("msg")
        slog=content.encode()
        encrypted=a.encrypt(slog)
        # print(cied)
        print(content)
        Chat.objects.create(
            from_agency=sobj, to_user=ciedobj, content=encrypted, from_user=None, to_agency=None)
        # return render(request, 'Agency/Chat.html', {"chatobj": chatobj})
    else:
        pass
        # return render(request, 'Agency/Chat.html', {"chatobj": chatobj})


def loadchat(request):
    cid = request.GET.get("cid")
    request.session["cid"] = cid

    cid1 = request.session["cid"]
    # print(cid1)
    # print(cid)
    shopobj = User.objects.get(id=cid)
    key1=shopobj.key
    
    b=Fernet(key1)
    
    # print(userobj)
    sid = request.session["agid"]
    
    # print(sid)
    suserobj = Agency.objects.get(id=request.session["agid"])
    key=suserobj.keys
    a=Fernet(key)

    chatobj = Chat.objects.raw(
        "select * from User_chat c inner join Guest_newagency u on (u.id=c.from_agency_id) or (u.id=c.to_agency_id) WHERE  c.from_user_id=%s or c.to_user_id=%s order by c.date", params=[(cid1), (cid1)])
    
    leh=(len(chatobj))
    message=[0 for i in range(0,leh)]
    
    for i in range(0,leh):
        csid=int(cid)
        if chatobj[i].from_user_id==csid and chatobj[i].to_agency_id==sid:
            chatobj[i].content=a.decrypt(chatobj[i].content).decode()
        elif chatobj[i].to_user_id==csid and chatobj[i].from_agency_id==sid:
            chatobj[i].content=b.decrypt(chatobj[i].content).decode()
    # print(message)   
    lk=[0 for i in range(0,leh)]  
    for i in range(0,leh):
        lk[i]=i
    return render(request, 'Agency/Load.html', {"obj": chatobj, "sid": sid, "shop": shopobj, "userobj": suserobj,'content':message,'len':lk})

def keyverification(request,cid):
    if 'agid' in request.session:
        request.session['did']=cid
        userid=Agency.objects.get(id=request.session['agid'])
        K=userid.key
        #print(K)   
        if request.method=="POST":
            Key=request.POST.get('en_key')
            Key = Key.encode()
            #print(Key)
            if Key==K:
                print("Hai")
                return redirect('webagency:Chat-user')
            else:
                error="Key Incorrect!!"
                return render(request,"Agency/KeyVerification.html",{'msg':error})
        else:
            return render(request,"Agency/KeyVerification.html")
    else:
        return redirect("webguest:login")
        
    
def chatuser(request):
    chatobj = Req.objects.get(id=request.session["did"])
    if request.method == "POST": 
        cied = request.POST.get("cid")
        # print(cied)
        ciedobj = User.objects.get(id=cied)
        key=ciedobj.key
        a=Fernet(key)
        '''key=bytes(key,'utf-8')
        print(key)
        with open("pass.key", "wb") as key_file:
            key_file.write(key)
        key=call_key()nm,./
        
        key=key.decode('utf-8')
        key=base64.urlsafe_b64encode(bytes(key,'utf-8'))
        print(key)
        a=Fernet(key)'''
        sobj = Agency.objects.get(id=request.session["agid"])
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
        Chat.objects.create(from_agency=sobj, to_user=ciedobj, content=coded_slog, from_user=None, to_agency=None)
        return render(request, 'Agency/Chat.html', {"chatobj": chatobj})
    else:
      
        return render(request, 'Agency/Chat.html', {"chatobj": chatobj})


def loadchatuser(request):
    cid = request.GET.get("cid")
    request.session["cid"] = cid
    cid1 = request.session["cid"]
    ## print(cid1)
    ## print(cid)
    shopobj=User.objects.get(id=cid)
    key=shopobj.key
    a=Fernet(key)
    ## print(userobj)
    sid = request.session["agid"]
    ## print(sid)
    suserobj = Agency.objects.get(id=request.session["agid"])
    key1=suserobj.key
    b=Fernet(key1)
    ## chatobj1 = Chat.objects.filter(Q(to_user=suserobj) | Q(
    ##    from_user=suserobj), Q(to_shop=shopobj) | Q(from_shop=shopobj))
    ## print(chatobj1)  # send message
    ## print(chatobj2)  # recived msg
    chatobj = Chat.objects.raw("select * from User_chat c inner join Guest_Agency u on (u.id=c.from_agency_id) or (u.id=c.to_agency_id) WHERE  c.from_user_id=%s or c.to_user_id=%s order by c.date", params=[(cid1), (cid1)])
    

    leh=(len(chatobj))
    ##message=[0 for i in range(0,leh)]
    for i in range(0,leh):
        csid=int(cid)
        if chatobj[i].from_agency_id==sid and chatobj[i].to_user_id==csid:
            chatobj[i].content=a.decrypt(chatobj[i].content).decode()
        elif chatobj[i].to_agency_id==sid and chatobj[i].from_user_id==csid:
            chatobj[i].content=b.decrypt(chatobj[i].content).decode()
    ##print(message)
    return render(request, 'Agency/Load.html', {"obj":chatobj, "sid": sid, "shop": shopobj, "userobj": suserobj})

def call_key():
    return open("pass.key", "rb").read()

def UploadReport(request,did):
    if 'agid' in request.session:
        if request.method=="POST":
            ag=Req.objects.get(id=did)
            agname=ag.agency.agency_name
            uname=ag.user.user_name
            umail=ag.user.user_mail
            cs=ag.casetype.casetype_name
            ag.report=request.FILES.get('file1')
            ag.save()
            send_mail(
            'Respected '+uname,#subject
             agname+' has generated the report for your '+cs+' case '+',you can download it by signing in to Mission Seeker',#body
            settings.EMAIL_HOST_USER,
            [umail],    
    )
            return redirect("webagency:chargeamt",did)
        else:
            return render(request,"Agency/UploadReport.html")
    else:
        return redirect("webguest:login")
    
def Logout(request):
    del request.session["agid"]
    return redirect("webguest:login")

def ChargeAmount(request,did):
    if 'agid' in request.session:
        if request.method=="POST":
            ag=Req.objects.get(id=did)
            ag.amount=request.POST.get('txt_amt')
            ag.save()
            return redirect('webagency:acceptedrequestslist')
        return render(request,"Agency/ChargeAmount.html")
    else:
        return redirect("webguest:login")