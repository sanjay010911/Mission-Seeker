from django.urls import path
from Agency import views 
app_name="webagency"
urlpatterns = [
    path('home/', views.Home,name="Home"),
    path('myprofile/', views.MyProfile,name="myprofile"),     
    path('editprofile/', views.EditProfile,name="editprofile"),
    path('changepass/', views.ChangePass,name="changepass"),
    path('requestlist/', views.RequestList,name="requestlist"),
    path('acceptrequest/<int:did>', views.AcceptRequest,name="acceptrequest"),
    path('rejectrequest/<int:did>', views.RejectRequest,name="rejectrequest"),
    path('acceptedrequestslist/', views.AcceptedRequestList,name="acceptedrequestslist"),
    path('rejectedrequestslist/', views.RejectedRequestList,name="rejectedrequestslist"),
    path('keyverification/<int:cid>',views.keyverification,name="keyverification"),
    path('chat/', views.chatuser,name="Chat-user"),
    path('loadchat/', views.loadchatuser,name="load-chat"),
    path('uploadreport/<int:did>',views.UploadReport,name="uploadreport"),
    path('logout/', views.Logout,name="logout"),
    path('chargeamt/<int:did>',views.ChargeAmount,name="chargeamt") 
]