from django.shortcuts import render,redirect
from .models import Product
from common.models import Eadmin
from common.models import Customer
from customer.models import Purchase

# Create your views here.
def master(request):
    return render(request,'shop/master.html')
def home(request):
    return render(request,'shop/home.html')


def register(request):
    msg = ""
    if request.method == 'POST':
        p_name = request.POST['name']
        p_brand = request.POST['brand']
        p_rate = request.POST['rate']
        p_image = request.FILES['file']
        
        new_product = Product(name = p_name, brand = p_brand, rate = p_rate, image = p_image)
        new_product.save()
        msg = "Mobile Phone Registered Successfully"
    return render(request,'shop/register.html',{'message':msg})


def viewcustomer(request):
    
    cust_data = Customer.objects.filter(id = request.session['customer'])
    return render(request,'shop/viewcustomer.html',{'view-list':cust_data})



def managepurchase(request):
    product_data = Purchase.objects.all()
    return render(request,'shop/managepurchase.html',{'purchase_list':product_data})


def manageproduct(request):
    products = Product.objects.all()
    return render(request,'shop/manageproduct.html',{'product_list':products})


def logout(request):
    return render(request,'shop/logout.html')

def delete_purchase(request,id):
    purchase_item = Purchase.objects.get(product = id, customer = request.session['customer'])
 
    purchase_item.delete()
    return redirect('eadmin:managepurchase')

    