from django.shortcuts import render,redirect
from eadmin.models import Product
from . models import Customer
from . models import Purchase

# Create your views here.
def master(request):
    return render(request,'user/master.html')
def home(request):
    products = Product.objects.all()
    return render(request,'user/home.html',{'product_list':products})
def productdetails(request,pid):
    msg = ""
    product_data = Product.objects.get(id = pid)

    if request.method == 'POST':
        
        product_id = request.POST['pid']
        item_exist = Purchase.objects.filter(product_id = product_id, customer_id = request.session['customer']).exists()
        if not item_exist:

             purchase_item = Purchase(product_id = product_id, customer_id = request.session['customer'])
             purchase_item.save()
             return redirect('eadmin:managepurchase')
        else:
            msg = 'Item alredy purchased'
  
    return render(request,'user/productdetails.html',{'product':product_data,'msg':msg})
def logout(request):
    return render(request,'user/logout.html')
