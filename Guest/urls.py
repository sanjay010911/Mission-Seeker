from django.urls import path
from Guest import views 
app_name="webguest"

urlpatterns = [
    path('',views.Home,name="home"),
    path('userreg/', views.UserReg,name="userreg"),
    path('ajaxplace/', views.Ajaxplace,name="Ajax-Place"),
    path('agencyreg/', views.AgencyReg,name="agencyreg"),
    path('login/', views.Login,name="login"),
    path('forgotpass/', views.ForgotPass,name="forgotpass"),
    path('validateotp/', views.ValidateOtp,name="validateotp"),
    path('createpass/', views.CreatePass,name="createpass"),
    path('goback/', views.GoBack,name="goback"),
    #path('Success/', views.success,name="Success"),
   
]