from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from User.models import *
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.
def Dist(request):
    if 'adid' in request.session:
        dist=District.objects.all().order_by('district_name')
        if request.method=="POST":
            d=District.objects.filter(district_name__icontains=request.POST.get("txt_district"))
            if d:
                return render(request,"Admin/District.html",{'res':dist,'msg':"Data already exists"})
            else: 
                District.objects.create(district_name=request.POST.get("txt_district"))
                return render(request,"Admin/District.html",{'res':dist,'msg':"Data Inserted"})
        else:
            return render(request,"Admin/District.html",{'res':dist})
    else:
        return redirect("webguest:login")
    
def place(request):
    if 'adid' in request.session:
        dis=District.objects.all().order_by('district_name')
        pl=Place.objects.all()
        if request.method=="POST":
            d=Place.objects.filter(place_name__icontains=request.POST.get('txt_place'))
            if d:
                return render(request,"Admin/Place.html",{'dis':dis,'res':pl,'msg':"Data already exists"})
            else:
                di=District.objects.get(id=request.POST.get('sel_district'))
                Place.objects.create(district=di,place_name=request.POST.get('txt_place'))
                return render(request,"Admin/Place.html",{'dis':dis,'res':pl,'msg':"Data Inserted"}) 
        else:
            return render(request,"Admin/Place.html",{'dis':dis,'res':pl})
    else:
        return redirect("webguest:login")

def DelDist(request,did):
    dist=District.objects.get(id=did)
    dist.delete()
    return redirect("webadmin:district")

def EditDist(request,eid):
    if 'adid' in request.session:
        dist=District.objects.get(id=eid)
        if request.method=="POST":
            dist.district_name=request.POST.get('txt_district')
            dist.save()
            return redirect("webadmin:district")
        else:
            return render(request,"Admin/EditDistrict.html",{'res':dist})
    else:
        return redirect("webguest:login")


def DelPlace(request,did):
    pl=Place.objects.get(id=did)
    pl.delete()
    return redirect("webadmin:place")

def CaseType(request):
    if 'adid' in request.session:
        casetype=Casetype.objects.all().order_by('casetype_name')
        if request.method=="POST":
            d=Casetype.objects.filter(casetype_name__icontains=request.POST.get('txt_casetype'))
            if d:
                return render(request,"Admin/CaseType.html",{'res':casetype,'msg':"Data already exists"})
            else:
                Casetype.objects.create(casetype_name=request.POST.get("txt_casetype"))
                return render(request,"Admin/CaseType.html",{'res':casetype,'msg':"Data Inserted"})
        else:
            return render(request,"Admin/CaseType.html",{'res':casetype})
    else:
        return redirect("webguest:login")

def DelCaseType(request,did):
    pl=Casetype.objects.get(id=did)
    pl.delete()
    return redirect("webadmin:casetype")

def EditCaseType(request,eid):
    if 'adid' in request.session:
        c=Casetype.objects.get(id=eid)
        if request.method=="POST":
            c.casetype_name=request.POST.get('txt_casetype')
            c.save()
            return redirect("webadmin:casetype")
        else:
            return render(request,"Admin/EditCaseType.html",{'res':c})
    else:
        return redirect("webguest:login")

def AgencyList(request):
    if 'adid' in request.session:
        newagency=Agency.objects.filter(agency_vstatus=0)
        return render(request,"Admin/AgencyList.html",{'data':newagency})
    else:
        return redirect("webguest:login")

def AcceptedAgencyList(request):
    if 'adid' in request.session:
        newagency=Agency.objects.filter(agency_vstatus=1)
        return render(request,"Admin/AcceptedAgencyList.html",{'data':newagency})
    else:
        return redirect("webguest:login")

def RejectedAgencyList(request):
    if 'adid' in request.session:
        newagency=Agency.objects.filter(agency_vstatus=2)
        return render(request,"Admin/RejectedAgencyList.html",{'data':newagency})
    else:
        return redirect("webguest:login")

def AcceptAgency(request,did):
    ag=Agency.objects.get(id=did)
    ag.agency_vstatus=1
    agname=ag.agency_name
    agmail=ag.agency_mail
    ag.save()
    send_mail(
            'Respected '+agname,#subject
            'Admin has accepted your request, you can start your service in Mission Seeker',#body
            settings.EMAIL_HOST_USER,
            [agmail],    
    )
    return redirect("webadmin:agencylist")

def RejectAgency(request,did):
    ag=Agency.objects.get(id=did)
    ag.agency_vstatus=2
    agname=ag.agency_name
    agmail=ag.agency_mail
    ag.save()
    send_mail(
            'Respected '+agname,#subject
            'Admin has rejected you from Mission Seeker',#body
            settings.EMAIL_HOST_USER,
            [agmail],    
    )
    return redirect("webadmin:agencylist")

def DelAgency(request,did):
    pl=Agency.objects.get(id=did)
    pl.delete()
    return redirect("webadmin:rejectedagencylist")

def ViewComplaints(request):
    if 'adid' in request.session:
        data=Complaint.objects.filter(complaint_status=0)
        return render(request,"Admin/ViewComplaints.html",{'data':data})
    else:
        return redirect("webguest:login")

def ReplyComplaints(request,did):
    if 'adid' in request.session:
        if request.method=="POST":
            cmp=Complaint.objects.get(id=did)
            cmp.complaint_reply=request.POST.get("txt_details")
            cmp.save()
            return redirect("webadmin:viewcomplaint")
        else:
            return render(request,"Admin/ReplyComplaint.html")
    else:
        return redirect("webguest:login")

def MarkAsSolved(request,did):
    cmp=Complaint.objects.get(id=did)
    cmp.complaint_status='1'
    cmp.save()
    return redirect('webadmin:viewcomplaint')

def Home(request):
    if 'adid' in request.session:
        return render(request,"Admin/Home.html")
    else:
        return redirect("webguest:login")

def ViewFeedback(request):
    if 'adid' in request.session:
        data=Feedback.objects.all()
        return render(request,"Admin/ViewFeedback.html",{'data':data})
    else:
        return redirect("webguest:login")

def Logout(request):
    del request.session["adid"]
    return redirect("webguest:login")

def UserReport(request):
    if 'adid' in request.session:
        if request.method=="POST":
            frdate=request.POST.get('frdate')
            todate=request.POST.get('todate')
            data=User.objects.filter(user_regdate__gte=frdate,user_regdate__lte=todate)
            return render(request,"Admin/UserReport.html",{'data':data,'f':frdate,'t':todate}) 
        return render(request,"Admin/UserReport.html")
    else:
        return redirect("webguest:login")

def RequestReport(request):
    if 'adid' in request.session:
        ag=Agency.objects.all()
        return render(request,"Admin/RequestsReport.html",{'ag':ag})
    else:
        return redirect("webguest:login")

def ViewReport(request,did):
    if 'adid' in request.session:
        data=Req.objects.filter(agency_id=did).count()
        data2=Req.objects.filter(agency_id=did,request_status=1).count()
        data3=Req.objects.filter(agency_id=did,payment_status=2).count()
        return render(request,"Admin/ViewReport.html",{'data':data,'data2':data2,'data3':data3})
    else:
        return redirect("webguest:login")






    