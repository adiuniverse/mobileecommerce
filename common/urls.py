from django.urls import path
from . import views
app_name = "common"
urlpatterns = [
   
    path('master',views.master,name='master'),
    path('home',views.home,name='home'),
    path('customerregister',views.customerregister,name='customerregister'),
    path('customerlogin',views.customerlogin,name='customerlogin'),
    path('eadminregister',views.eadminregister,name='eadminregister'),
    path('eadminlogin',views.eadminlogin,name='eadminlogin'),

]
