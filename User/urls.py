from django.urls import path
from User import views 
app_name="webuser"
urlpatterns = [
    path('Home/', views.home,name="Home"),
    path('myprofile/', views.MyProfile,name="myprofile"),     
    path('editprofile/', views.EditProfile,name="editprofile"),
    path('changepass/', views.ChangePass,name="changepass"),
    path('request/<int:did>', views.Reques,name="request"),
    path('feedback/', views.feedback,name="feedback"),
    path('complaint/', views.complaint,name="complaint"),
    path('searchagency/', views.SearchAgency,name="searchagency"),
    path('ajaxagency/', views.AjaxAgency,name="Ajax-Agency"),
    path('viewreq/', views.ViewReq,name="viewreq"),
    path('keyverification/<int:cid>',views.keyverification,name="keyverification"),
    path('chat/', views.chatuser,name="Chat-user"),
    path('loadchat/', views.loadchatuser,name="load-chat"),
    path('confirmpayment/<int:did>', views.ConfirmPayment,name="confirmpayment"),
    path('payment/<int:did>', views.Payment,name="payment"),
    path('logout/', views.Logout,name="logout"),  
]