from django.urls import path
from . import views
app_name = "customer"
urlpatterns = [
   
    path('master',views.master,name='master'),
    path('home',views.home,name='home'),
    path('productdetails/<int:pid>',views.productdetails,name='productdetails'),
    path('logout',views.logout,name='logout'),
  

]
