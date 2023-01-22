from django.urls import path
from . import views
app_name = "eadmin"
urlpatterns = [
   
    path('master',views.master,name='master'),
    path('home',views.home,name='home'),
    path('register',views.register,name='register'),
    path('viewcustomer',views.viewcustomer,name='viewcustomer'),
    path('managepurchase',views.managepurchase,name='managepurchase'),
    path('manageproduct',views.manageproduct,name='manageproduct'),
    path('logout',views.logout,name='logout'),
    path('delete/<int:id>',views.delete_purchase,name='delete_purchase'),
   
]
