from django.urls import path
from Admin import views 
app_name="webadmin"
urlpatterns = [
    path('dist/', views.Dist,name="district"),
    path('deldist/<int:did>', views.DelDist,name="deldistrict"),
    path('editdist/<int:eid>', views.EditDist,name="editdistrict"),
    path('place/', views.place,name="place"),
    path('delplace/<int:did>', views.DelPlace,name="delplace"),
    path('casetype/', views.CaseType,name="casetype"),
    path('delcasetype/<int:did>', views.DelCaseType,name="delcasetype"),
    path('editcasetype/<int:eid>', views.EditCaseType,name="editcasetype"),
    path('agencylist/', views.AgencyList,name="agencylist"),
    path('accept/<int:did>', views.AcceptAgency,name="acceptagency"),
    path('reject/<int:did>', views.RejectAgency,name="rejectagency"),
    path('acceptedagencylist/', views.AcceptedAgencyList,name="acceptedagencylist"),
    path('rejectedagencylist/', views.RejectedAgencyList,name="rejectedagencylist"),
    path('delagency/<int:did>',views.DelAgency,name="delagency"),
    path('viewcomplaint/', views.ViewComplaints,name="viewcomplaint"),
    path('replycomplaint/<int:did>', views.ReplyComplaints,name="replycomplaint"),
    path('markassolved/<int:did>', views.MarkAsSolved,name="markassolved"),
    path('home/', views.Home,name="Home"),
    path('viewfeedback/', views.ViewFeedback,name="viewfeedback"),
    path('logout/',views.Logout,name="logout"),
    path('userreport/',views.UserReport,name="userreport"),
    path('requestreport/',views.RequestReport,name="requestreport"),
    path('viewreport/<int:did>',views.ViewReport,name="viewreport")
]