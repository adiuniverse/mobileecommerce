from django.shortcuts import render,redirect
from . models import Customer
from .models import Eadmin

# Create your views here.
def master(request):
    return render(request,'client/master.html')
def home(request):
    return render(request,'client/home.html')



def customerregister(request):
    
    if request.method == 'POST':
        c_name = request.POST['fname']
        c_contact = request.POST['phone']
        c_email = request.POST['email']
        c_username = request.POST['username']
        c_password = request.POST['password']
        c_confirm = request.POST['confirm']
        new_customer = Customer(name = c_name, contact = c_contact, email = c_email,
                                username = c_username, password = c_password, confirm = c_confirm)
        new_customer.save()
    return render(request,'client/customerregister.html')



def customerlogin(request):
    msg = ""
    if request.method == 'POST':
        c_username = request.POST['username']
        c_password = request.POST['password']
        try:
             customer = Customer.objects.get(username = c_username, password = c_password)
             request.session['customer'] = customer.id
             return redirect('customer:home')
        except Exception as e:
            print(e)
            msg = "Customer Login Successfully"
    return render(request,'client/customerlogin.html',{'message':msg})


def eadminregister(request):
    if request.method == 'POST':
        e_name = request.POST['name']
        e_email = request.POST['email']
        e_username = request.POST['username']
        e_password = request.POST['password']

        new_eadmin = Eadmin(name = e_name, email = e_email, username = e_username, password = e_password)
        new_eadmin.save()
    return render(request,'client/eadminregister.html')


def eadminlogin(request):
    msg = ""
    if request.method == 'POST':
        e_username = request.POST['username']
        e_password = request.POST['password']
        try:
            eadmin = Eadmin.objects.get(username = e_username, password = e_password)
            request.session['eadmin'] = eadmin.id
            return redirect('eadmin:home')
        except Exception as e:
            print(e)
            msg = "eadmin Login Successfully"
    return render(request,'client/eadminlogin.html',{'message':msg})